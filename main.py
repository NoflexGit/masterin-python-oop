import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def get_items_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_items=0):
        super().__init__(name, price, quantity)

        assert broken_items >= 0, f"Broken items {broken_items} is not greater or equal to zero!"

        self.broken_items = broken_items


phone1 = Phone('Iphone 5s', 299, 1, 0)
print(phone1.name)
