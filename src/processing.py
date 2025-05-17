from typing import List, Dict, Any


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    '''Фильтрует список словарей по заданному значению поля "state".'''

    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    '''Сортирует список словарей по убыванию даты.'''

    return sorted(operations, key=lambda x: x.get("date", ""), reverse=reverse)
