from typing import Any, Dict, List

from collections import Counter


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по заданному статусу.

    Args:
        operations (List[Dict[str, Any]]): Список операций, каждая операция представлена словарем.
        state (str): Статус, по которому нужно отфильтровать операции. По умолчанию "EXECUTED".

    Returns:
        List[Dict[str, Any]]: Список операций с заданным статусом.
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations (List[Dict[str, Any]]): Список операций, каждая операция представлена словарем.
        reverse (bool): True для сортировки в порядке убывания, False - в порядке возрастания.

    Returns:
        List[Dict[str, Any]]: Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=reverse)


def count_transactions_by_category(transactions: List[Dict[str, Any]],
                                   categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по заданным категориям.

    Args:
        transactions: Список словарей с транзакциями.
        categories: Список категорий для подсчета.

    Returns:
        Словарь с количеством транзакций по каждой категории.

    Example:
        transactions = [{"description": "Payment for services"},
                         {"description": "Grocery shopping"}]
        count_transactions_by_category(transactions, ["Payment", "shopping"])
        {'Payment': 1, 'shopping': 1}
    """
    if not transactions or not categories:
        return {}

    category_counts = Counter()
    descriptions = [tx.get("description", "").lower() for tx in transactions]

    for category in categories:
        category_lower = category.lower()
        category_counts[category] = sum(
            1 for desc in descriptions if category_lower in desc
        )

    return dict(category_counts)
