import csv
import json
import re

import pandas as pd


def load_transactions_from_json(file_path):  # type: ignore
    """
    Загружает список транзакций из JSON-файла
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_transactions_from_csv(file_path):  # type: ignore
    """
    Загружает список транзакций из CSV-файла
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_transactions_from_xlsx(file_path):  # type: ignore
    """
    Загружает список транзакций из XLSX-файла
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


def filter_transactions_by_status(transactions, status):  # type: ignore
    """
    Фильтрует транзакции по статусу
    """
    return [t for t in transactions if t.get("state", "").lower() == status.lower()]


def sort_transactions_by_date(transactions, ascending=True):  # type: ignore
    """
    Сортирует транзакции по дате
    """
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=not ascending)


def filter_transactions_by_currency(transactions, currency="руб."):  # type: ignore
    """
    Фильтрует транзакции по валюте
    """
    return [t for t in transactions if currency in t.get("amount", "").lower()]


def filter_transactions_by_description(transactions, search_string):  # type: ignore
    """
    Фильтрует транзакции по строке в описании
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def main() -> None:  # type: ignore
    """
    Основная функция, которая взаимодействует с пользователем и обрабатывает транзакции.
    Запрашивает пользователя о типе файла, фильтрует и сортирует транзакции
    по выбранным параметрам, а затем выводит итоговый список транзакций
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пожалуйста, выберите опцию (1/2/3): ")
    transactions = []

    if choice == "1":
        transactions = load_transactions_from_json("../data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = load_transactions_from_csv("transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = load_transactions_from_xlsx("transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
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

    search_choice = (
        input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower()
    )
    if search_choice == "да":
        search_word = input("Введите слово для фильтрации: ")
        transactions = filter_transactions_by_description(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(f"{transaction.get('date', 'Неизвестная дата')} {transaction.get('description', 'Без описания')}")
            print(f"Сумма: {transaction.get('amount', 'Не указано')}")
            print()


if __name__ == "__main__":
    main()