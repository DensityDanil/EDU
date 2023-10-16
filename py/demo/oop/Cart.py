class Cart:
    def __init__(self):
        self.items = [] #buffer size?

    def add_item(self, item_name, item_price):
        item = {"name": item_name, "price": item_price}
        self.items.append(item)
        print(f"{item_name} додано до корзини!")

    def remove_item(self, item_name):
        for item in self.items:
            if item["name"] == item_name:
                self.items.remove(item)
                print(f"{item_name} видалено з корзини!")
                return
        print(f"{item_name} не знайдено в корзині.")

    def calculate_total(self):
        total = sum(item["price"] for item in self.items)
        return total

    def display_cart(self):
        if not self.items:
            print("Корзина пуста")
        else:
            print("Ваша корзина містить:")
            for item in self.items:
                print(f"{item['name']} - ${item['price']}")

# Приклад використання
my_cart = Cart()

my_cart.add_item("Футболка", 15)
my_cart.add_item("Джинси", 30)
my_cart.add_item("Кросівки", 50)

my_cart.display_cart()

total_price = my_cart.calculate_total()
print(f"Загальна сума: ${total_price}")

my_cart.remove_item("Футболка")
my_cart.display_cart()

total_price = my_cart.calculate_total()
print(f"Загальна сума після видалення: ${total_price}")
