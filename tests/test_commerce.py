from src.commerce import Product, Category


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 50000, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000
    assert product.quantity == 10


def test_category_initialization():
    products = [Product("Телефон", "Смартфон", 50000, 10), Product("Ноутбук", "Игровой ноутбук", 100000, 5)]
    category = Category("Электроника", "Техника", products)
    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2
    assert isinstance(category.products[0], Product)


def test_products_count():
    initial_count = Product.total_products
    # flake8: noqa: F841
    product1 = Product("Товар1", "Описание1", 100, 1)
    product2 = Product("Товар2", "Описание2", 200, 2)
    assert Product.total_products == initial_count + 2


def test_categories_count():
    initial_count = Category.category_count
    products = [Product("Товар", "Описание", 100, 1)]
    category1 = Category("Категория1", "Описание1", products)
    category2 = Category("Категория2", "Описание2", products)
    assert Category.category_count == initial_count + 2
    assert Category.product_count >= 2  # Минимум 2 уникальных товара (по одному в каждой категории)