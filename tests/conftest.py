import json
import pytest


@pytest.fixture
def test_json(tmp_path):
    data = [
        {
            "name": "Телефоны",
            "description": "Смартфоны",
            "products": [{"name": "iPhone 13", "description": "128GB", "price": 80000, "quantity": 10}],
        }
    ]
    file = tmp_path / "test.json"
    file.write_text(json.dumps(data))
    return str(file)