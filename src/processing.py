

from typing import List, Dict


def filter_by_state(info_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    '''Фильтрует список словарей по заданному значению поля "state".'''


    return [item for item in info_list if item.get("state") == state]


def sort_by_date(info_list: List[Dict]) -> List[Dict]:
    '''Сортирует список словарей по убыванию даты.'''


    return sorted(info_list, key=lambda item: item["date"], reverse=True)
