# generators.py
def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, end):
    max_card_number = 9999999999999999
    start = max(0, start)
    end = min(end, max_card_number)

    for i in range(start, end + 1):
        card_number = str(i).zfill(16)  # Дополняем 0 до 16
        formatted_card_number = " ".join([card_number[i:i+4] for i in range(0, 16, 4)])
        yield formatted_card_number