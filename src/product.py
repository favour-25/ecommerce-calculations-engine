class Product:
    def __init__(self, name, price, quantity_in_stock):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity_in_stock < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def reduce_stock(self, quantity):
        self.quantity_in_stock -= quantity

    def is_available(self, quantity):
        return quantity <= self.quantity_in_stock

    def __repr__(self):
        return f"Product({self.name!r}, price={self.price}, stock={self.quantity_in_stock})"