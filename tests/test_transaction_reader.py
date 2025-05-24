import csv
import pandas as pd
from typing import List, Union, Dict


def csv_to_list(file_path: str) -> List[Dict[str, str]]:
    """
    Читает CSV файл и возвращает список словарей.

    Args:
        file_path: Путь к CSV файлу

    Returns:
        Список словарей с данными из CSV. При ошибках возвращает пустой список.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except (FileNotFoundError, Exception):
        return []


def xlsx_to_list(file_path: str) -> List[List[Union[int, float, str]]]:
    """
    Читает XLSX файл и возвращает список списков (значения строк).

    Args:
        file_path: Путь к XLSX файлу

    Returns:
        Список списков с данными из Excel. При ошибках возвращает пустой список.
    """
    try:
        df = pd.read_excel(file_path)
        return df.values.tolist()
    except (FileNotFoundError, Exception):
        return []