import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize('value_card, expected_card', [
    ('Visa 7000792289606361', 'Visa 7000 79** **** 6361'),
    ('Счет 12341234123412341234', 'Счет **1234')
])
def test_mask_number_card(value_card, expected_card):
    assert mask_account_card(value_card) == expected_card
