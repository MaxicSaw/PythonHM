import pytest
from src import masks


@pytest.mark.parametrize('value_card, expected_card', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('ffasfdasfasdvav', 'Номер карты введен не корректно')
])
def test_mask_number_card(value_card, expected_card):
    assert mask_account_card(value_card) == expected_card


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
