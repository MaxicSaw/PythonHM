import os

import requests
from dotenv import load_dotenv

load_dotenv()


def calculate_transaction_amount(transaction):
    try:
        # Проверка наличия обязательных полей
        if not transaction.get("operationAmount"):
            return None

        amount_str = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        # Парсим сумму
        try:
            amount = float(amount_str)
        except ValueError:
            return None

        # Для RUB сразу возвращаем сумму
        if currency == "RUB":
            return amount

        # Для неподдерживаемых валют
        if currency not in ["USD", "EUR"]:  # Добавьте другие валюты по необходимости
            return None

        # Получаем курс от API
        api_key = os.getenv("API_KEY")
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert",
            params={
                "from": currency,
                "to": "RUB",
                "amount": amount
            },
            headers={"apikey": api_key}
        )

        if response.status_code != 200:
            return None

        # Умножаем сумму на курс из API
        rate = response.json()["result"]
        return amount * rate

    except Exception:
        return None
