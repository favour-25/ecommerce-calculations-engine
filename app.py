import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request, render_template

from src.product import Product
from src.user import User
from src.exceptions import OutOfStockError, InvalidQuantityError

app = Flask(__name__)

# --- In-memory demo data (resets whenever the server restarts) ---
CATALOG = [
    Product("Rice (50kg bag)", 45000, 10),
    Product("Cooking Oil (5L)", 8500, 15),
    Product("Laptop", 350000, 5),
    Product("Phone", 180000, 8),
    Product("Bag of Beans", 12000, 20),
]

CURRENT_USER = User("Guest")


def product_to_dict(product, index):
    return {
        "id": index,
        "name": product.name,
        "price": product.price,
        "quantity_in_stock": product.quantity_in_stock,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify([product_to_dict(p, i) for i, p in enumerate(CATALOG)])


@app.route("/api/cart", methods=["GET"])
def get_cart():
    cart = CURRENT_USER.cart
    items = []
    for product, quantity in cart.items:
        items.append({
            "name": product.name,
            "price": product.price,
            "quantity": quantity,
            "line_total": product.price * quantity,
        })
    return jsonify({
        "items": items,
        "subtotal": cart.calculate_subtotal(),
        "discount": cart.calculate_discount(),
        "tax": cart.calculate_tax(),
        "total": cart.calculate_total(),
    })


@app.route("/api/cart/add", methods=["POST"])
def add_to_cart():
    data = request.get_json(silent=True) or {}
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if product_id is None or quantity is None:
        return jsonify({"error": "product_id and quantity are required."}), 400

    try:
        product_id = int(product_id)
        quantity = int(quantity)
        product = CATALOG[product_id]
    except (ValueError, IndexError):
        return jsonify({"error": "Invalid product_id."}), 400

    try:
        CURRENT_USER.cart.add_item(product, quantity)
    except (InvalidQuantityError, OutOfStockError) as e:
        return jsonify({"error": str(e)}), 400

    return get_cart()


@app.route("/api/cart/reset", methods=["POST"])
def reset_cart():
    CURRENT_USER.cart.items = []
    return jsonify({"message": "Cart cleared."})


if __name__ == "__main__":
    app.run(debug=False)