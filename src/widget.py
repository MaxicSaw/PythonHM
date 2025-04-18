from src import masks
"""Функция вывода ошибки ввода номера карты"""


def mask_account_card(number_card: str) -> str:
    if not number_card or not isinstance(number_card, str):
        raise ValueError("Ошибка ввода. Ожидается строка с номером карты или счета.")

    number = "".join(filter(str.isdigit, number_card))
    name_card = "".join(filter(lambda x: not x.isdigit(), number_card)).strip()

    """Функция маскировки номера карты"""
    if len(number) in {16, 19}:
        masked_number = masks.get_mask_card_number(number)
    elif len(number) >= 20:
        masked_number = masks.get_mask_account(number)
    else:
        raise ValueError("Некорректный номер. Длина не соответствует картам или счетам.")

    return f"{name_card} {masked_number}".strip()


def get_date(datetime: str) -> str:
    """Функция вывода времени"""
    date_object = datetime[0:10].split("-")
    return ".".join(date_object[::-1])
