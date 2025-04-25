import pytest


from typing import List, Dict


def filter_by_state(info_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    '''Фильтрует список словарей по заданному значению поля "state".'''

    return [item for item in info_list if item.get("state") == state]


def sort_by_date(info_list: List[Dict]) -> List[Dict]:
    '''Сортирует список словарей по убыванию даты.'''

    return sorted(info_list, key=lambda item: item["date"], reverse=True)


@pytest.mark.parametrize("my_list, state, expected", [
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        "CANCELED",
        [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    )
])
def test_filter_by_state(my_list: list, state: str, expected: list) -> None:
    assert filter_by_state(my_list, state) == expected
