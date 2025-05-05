import pytest
from src import masks


@pytest.fixture
def get_mask_card_number(number_card: str) -> str:
    """Функцию маскировки номера банковской карты"""
    str_number_card = number_card
    masked = str_number_card[:6] + "*" * 6 + str_number_card[-4:]

    count = 0
    slice_masc = ""
    for i in masked:
        count += 1
        slice_masc += i
        if count % 4 == 0:
            slice_masc += " "

    return slice_masc[0:19]


def mask_account_card(number_card: str) -> str:
    if not number_card or not isinstance(number_card, str):
        raise ValueError("Ошибка ввода. Ожидается строка с номером карты или счета.")

    number = "".join(filter(str.isdigit, number_card))

    if len(number) == 16 or len(number) == 19:
        masked_number = masks.get_mask_card_number(number)
    elif len(number) >= 20:
        masked_number = masks.get_mask_account(number)
    else:
        return 'Номер карты введен не корректно'

    return masked_number
