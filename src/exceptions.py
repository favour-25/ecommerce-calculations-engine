class OutOfStockError(Exception):
    """Raised when trying to buy more than what's in stock."""
    pass


class InvalidQuantityError(Exception):
    """Raised when quantity is zero or negative."""
    pass