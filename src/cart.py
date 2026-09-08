from .exceptions import OutOfStockError, InvalidQuantityError

TAX_RATE = 0.075        # 7.5% VAT (Nigeria standard rate)
DISCOUNT_THRESHOLD = 10000
DISCOUNT_RATE = 0.10    # 10% discount if subtotal is above threshold


class Cart:
    def __init__(self):
        self.items = []   # list of (product, quantity) tuples

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero.")

        if not product.is_available(quantity):
            raise OutOfStockError(f"{product.name} is out of stock.")

        product.reduce_stock(quantity)
        self.items.append((product, quantity))

    def calculate_subtotal(self):
        subtotal = 0
        for product, quantity in self.items:
            subtotal += product.price * quantity
        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        if subtotal > DISCOUNT_THRESHOLD:
            return subtotal * DISCOUNT_RATE
        return 0

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        taxable_amount = subtotal - discount
        return taxable_amount * TAX_RATE

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        return subtotal - discount + tax