class Product:
    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def reduce_stock(self, quantity):
        self.quantity_in_stock -= quantity

    def is_available(self, quantity):
        return quantity <= self.quantity_in_stock