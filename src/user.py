from .cart import Cart


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()