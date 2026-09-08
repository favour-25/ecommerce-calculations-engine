# E-Commerce Calculations Engine (TDD Project)

## Project Overview
This project implements the core calculation logic for a shopping cart system,
built using Test-Driven Development (TDD). It covers Product, Cart, and User
classes, along with discount, tax, and total calculations, plus exception
handling for invalid quantities and out-of-stock items.

## Methodology
Test-Driven Development (TDD) was followed using Python's built-in `unittest`
framework. For each feature, a test was written first (Red), then the minimum
code needed to pass it was implemented (Green), following the Red-Green cycle.

## Project Structure
```
ecommerce_engine/
├── src/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── product.py
│   ├── cart.py
│   └── user.py
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_user.py
├── run_tests.py
└── README.md
```

## Classes
- **Product** — represents an item with a name, price, and stock quantity.
- **Cart** — holds products added by a user and calculates subtotal, discount, tax, and total.
- **User** — represents a customer who owns a cart.

## Business Rules
- **Tax Rate:** 7.5% (Nigeria standard VAT)
- **Discount:** 10% applied automatically if cart subtotal exceeds ₦10,000

## Exception Handling
- `InvalidQuantityError` — raised when a quantity of zero or less is added to the cart.
- `OutOfStockError` — raised when the requested quantity exceeds available stock.

## How to Run the Tests
From the `ecommerce_engine` folder, run:
```
python run_tests.py
```

## Test Results
All 12 unit tests pass successfully, covering:
- Product creation and stock reduction
- Cart item addition (valid and invalid cases)
- Discount and tax calculations
- Total calculation
- User creation

## Author
Ogungbemi Favour Eyiwumi
Matric No: CSC/2023/81184
Department of Computer Science, Federal University Oye-Ekiti (FUOYE)
