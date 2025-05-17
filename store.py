# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# - метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# - метод для обновления цены товара.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
        print(f"Магазин {self.name} по адресу {self.address} создан")

    def add_item(self, product_name, product_price):
        new_product = {product_name : product_price}
        self.items.update(new_product)
        print(f"Товар {product_name} с ценой {product_price} добавлен в магазине {self.name}")

    def del_item(self, product_name):
        product_price = self.items.pop(product_name, None)
        if product_price is None:
            print(f"Товар {product_name} не найден в магазине {self.name}")
        else :
            print(f"Товар {product_name} с ценой {product_price} удален в магазине {self.name}")

    def get_price(self, product_name):
        product_price = self.items.get(product_name, None)
        return product_price

    def set_price(self, product_name, product_price):
        if self.items.get(product_name) is None:
            print(f"Товар {product_name} не найден в магазине {self.name}")
        else :
            self.items[product_name] = product_price
            print(f"Цена товара {product_name} в магазине {self.name} обновлена - {product_price} руб.")

    def show_items(self):
        print(f"Список товаров в магазине {self.name}:")
        for key, value in self.items.items():
            print(key, value)

def get_store_price(store, name):
    price = store.get_price(name)
    if price is None:
        print(f"Товар {name} не найден в магазине {store.name}")
    else:
        print(f"Цена товара {name} - {price} руб. в магазине {store.name}")

store1 = Store("Store1", "Moscow, Tverskaya str.")
store2 = Store("Store2", "Moscow, Mohovaya str.")
store3 = Store("Store3", "Moscow, Malahitovaya str.")

store1.add_item("Product11", 1000)
store1.add_item("Product12", 2000)
store1.add_item("Product13", 3000)

store2.add_item("Product21", 4000)
store2.add_item("Product22", 5000)

store3.add_item("Product31", 6000)
store3.add_item("Product32", 7000)
store3.add_item("Product33", 8000)
store3.add_item("Product34", 9000)

store1.show_items()
store2.show_items()
store3.show_items()

get_store_price(store1, "Product11")
get_store_price(store1, "Product14")
store3.set_price("Product31", 6500)
get_store_price(store3, "Product31")

store3.del_item("Product35")
store3.del_item("Product33")

store3.show_items()
