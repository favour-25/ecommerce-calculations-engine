import unittest
from src.product import Product
from src.cart import Cart
from src.exceptions import OutOfStockError, InvalidQuantityError


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product = Product("Rice", 5000, 10)

    def test_add_item(self):
        self.cart.add_item(self.product, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.product.quantity_in_stock, 8)

    def test_add_item_negative_quantity_raises_error(self):
        with self.assertRaises(InvalidQuantityError):
            self.cart.add_item(self.product, -1)

    def test_add_item_out_of_stock_raises_error(self):
        with self.assertRaises(OutOfStockError):
            self.cart.add_item(self.product, 50)

    def test_calculate_subtotal(self):
        self.cart.add_item(self.product, 2)
        self.assertEqual(self.cart.calculate_subtotal(), 10000)

    def test_calculate_discount_applies_above_threshold(self):
        expensive_product = Product("Laptop", 15000, 5)
        self.cart.add_item(expensive_product, 1)
        self.assertEqual(self.cart.calculate_discount(), 1500)

    def test_calculate_discount_none_below_threshold(self):
        self.cart.add_item(self.product, 1)
        self.assertEqual(self.cart.calculate_discount(), 0)

    def test_no_discount_exactly_at_threshold(self):
        product = Product("Item", 10000, 1)
        self.cart.add_item(product, 1)
        self.assertEqual(self.cart.calculate_discount(), 0)

    def test_calculate_total(self):
        self.cart.add_item(self.product, 1)
        expected_total = 5000 + (5000 * 0.075)
        self.assertAlmostEqual(self.cart.calculate_total(), expected_total)


if __name__ == "__main__":
    unittest.main()