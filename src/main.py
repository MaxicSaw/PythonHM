import csv
import json
import re
from datetime import datetime

import pandas as pd


def load_transactions_from_json(file_path):
    """
    Загружает список транзакций из JSON-файла
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_transactions_from_csv(file_path):
    """
    Загружает список транзакций из CSV-файла
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_transactions_from_xlsx(file_path):
    """
    Загружает список транзакций из XLSX-файла
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


def filter_transactions_by_status(transactions, status):
    """
    Фильтрует транзакции по статусу
    """
    return [t for t in transactions if t.get("state", "").lower() == status.lower()]


def sort_transactions_by_date(transactions, ascending=True):
    """
    Сортирует транзакции по дате
    """

    def get_date(transaction):
        date_str = transaction.get("date", "")
        try:
            # Пробуем разобрать дату с временем
            return datetime.strptime(date_str.split('T')[0], "%Y-%m-%d")
        except (ValueError, AttributeError):
            return datetime.min

    return sorted(transactions, key=get_date, reverse=not ascending)


def filter_transactions_by_currency(transactions, currency="руб."):
    """
    Фильтрует транзакции по валюте
    """
    return [t for t in transactions if
            currency.lower() in t.get("operationAmount", {}).get("currency", {}).get("name", "").lower()]


def filter_transactions_by_description(transactions, search_string):
    """
    Фильтрует транзакции по строке в описании
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def format_card_number(card_number):
    """
    Форматирует номер карты в вид XXXX XX** **** XXXX
    """
    if not card_number:
        return ""
    parts = card_number.split()
    if len(parts) >= 1 and len(parts[-1]) == 16 and parts[-1].isdigit():
        return f"{' '.join(parts[:-1])} {parts[-1][:4]} {parts[-1][4:6]}** **** {parts[-1][-4:]}"
    return card_number


def format_account_number(account_number):
    """
    Форматирует номер счета в вид **XXXX
    """
    if not account_number:
        return ""
    if isinstance(account_number, str):
        account_digits = ''.join(c for c in account_number if c.isdigit())
        if len(account_digits) >= 4:
            return f"**{account_digits[-4:]}"
    return account_number


def format_transaction(transaction):
    """
    Форматирует транзакцию в нужный вид для вывода
    """
    # Обработка даты
    date_str = transaction.get("date", "")
    try:
        date = datetime.strptime(date_str.split('T')[0], "%Y-%m-%d").strftime("%d.%m.%Y")
    except (ValueError, AttributeError):
        date = "Дата неизвестна"

    description = transaction.get("description", "Без описания")

    from_info = transaction.get("from", "")
    to_info = transaction.get("to", "")

    # Форматирование отправителя
    if isinstance(from_info, str):
        if "счет" in from_info.lower():
            from_info = f"Счет {format_account_number(from_info)}"
        else:
            from_info = format_card_number(from_info)

    # Форматирование получателя
    if isinstance(to_info, str):
        if "счет" in to_info.lower():
            to_info = f"Счет {format_account_number(to_info)}"
        else:
            to_info = format_card_number(to_info)

    # Получение суммы и валюты
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount", "Не указано")
    currency = operation_amount.get("currency", {}).get("name", "")

    # Формирование результата
    result = [
        f"{date} {description}",
        f"{from_info} -> {to_info}" if from_info else to_info,
        f"Сумма: {amount} {currency}",
        ""
    ]

    return "\n".join(result)


def main():
    """
    Основная функция, которая взаимодействует с пользователем и обрабатывает транзакции.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пожалуйста, выберите опцию (1/2/3): ")
    transactions = []

    if choice == "1":
        try:
            transactions = load_transactions_from_json("../data/operations.json")
            print("Для обработки выбран JSON-файл.")
        except FileNotFoundError:
            print("Файл не найден. Завершение работы.")
            return
    elif choice == "2":
        try:
            transactions = load_transactions_from_csv("transactions.csv")
            print("Для обработки выбран CSV-файл.")
        except FileNotFoundError:
            print("Файл не найден. Завершение работы.")
            return
    elif choice == "3":
        try:
            transactions = load_transactions_from_xlsx("transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл.")
        except FileNotFoundError:
            print("Файл не найден. Завершение работы.")
            return
    else:
        print("Некорректный ввод. Завершение работы.")
        return

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ")
        if status.upper() in statuses:
            transactions = filter_transactions_by_status(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status.upper()}".')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        transactions = sort_transactions_by_date(transactions, ascending=(order == "по возрастанию"))

    currency_choice = input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if currency_choice == "да":
        transactions = filter_transactions_by_currency(transactions)

    search_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower()
    if search_choice == "да":
        search_word = input("Введите слово для фильтрации: ")
        transactions = filter_transactions_by_description(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(format_transaction(transaction))


if __name__ == "__main__":
    main()