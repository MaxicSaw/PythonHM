import json
from src.commerce import Product, Category


def loader_data(filename):
    """
    Загружает данные из JSON файла и создает объекты Category и Product.
    Возвращает список объектов Category.
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories
