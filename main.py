class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.price = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item('IPhone 13 Pro', -1, 10)
item2 = Item('IPad Pro', 1099, 3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
