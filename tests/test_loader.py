import json
import pytest
from src.commerce import Category
from src.loader import loader_data


def test_load_data_success(test_json):
    """Проверка успешной загрузки данных"""
    categories = loader_data(test_json)

    assert len(categories) == 1
    assert categories[0].name == "Телефоны"
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "iPhone 13"


def test_counters_update(test_json):
    """Проверка обновления счётчиков"""
    Category.category_count = 0
    Category.product_count = 0

    loader_data(test_json)

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_file_not_found():
    """Проверка обработки отсутствия файла"""
    with pytest.raises(FileNotFoundError):
        loader_data("missing.json")


def test_invalid_json(tmp_path):
    """Проверка обработки невалидного JSON"""
    file = tmp_path / "bad.json"
    file.write_text("{invalid}")

    with pytest.raises(json.JSONDecodeError):
        loader_data(str(file))