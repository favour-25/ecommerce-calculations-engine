import unittest
from src.product import Product


class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Rice", 5000, 10)
        self.assertEqual(product.name, "Rice")
        self.assertEqual(product.price, 5000)
        self.assertEqual(product.quantity_in_stock, 10)

    def test_reduce_stock(self):
        product = Product("Rice", 5000, 10)
        product.reduce_stock(3)
        self.assertEqual(product.quantity_in_stock, 7)

    def test_is_available_true(self):
        product = Product("Rice", 5000, 10)
        self.assertTrue(product.is_available(5))

    def test_is_available_false(self):
        product = Product("Rice", 5000, 10)
        self.assertFalse(product.is_available(20))

    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            Product("Bad", -100, 5)

    def test_negative_stock_raises_error(self):
        with self.assertRaises(ValueError):
            Product("Bad", 100, -5)


if __name__ == "__main__":
    unittest.main()