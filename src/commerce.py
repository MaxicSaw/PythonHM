class Product:
    total_products = 0  # Атрибут класса для подсчета общего количества товаров

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_products += 1  # Увеличиваем счетчик товаров при создании нового


class Category:
    category_count = 0  # Атрибут класса для подсчета количества категорий
    product_count = 0  # Атрибут класса для подсчета общего количества товаров во всех категориях

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(products)  # Увеличиваем счетчик товаров