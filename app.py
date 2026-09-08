from flask import Flask, request, jsonify
from src.product import Product
from src.cart import Cart
from src.exceptions import InvalidQuantityError, OutOfStockError

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "E-Commerce Calculations Engine API is running.",
        "usage": "POST /calculate with JSON: {\"price\": 5000, \"stock\": 10, \"quantity\": 2}"
    })


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    price = data.get("price")
    stock = data.get("stock")
    quantity = data.get("quantity")

    product = Product("Item", price, stock)
    cart = Cart()

    try:
        cart.add_item(product, quantity)
    except InvalidQuantityError as e:
        return jsonify({"error": str(e)}), 400
    except OutOfStockError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "subtotal": cart.calculate_subtotal(),
        "discount": cart.calculate_discount(),
        "tax": round(cart.calculate_tax(), 2),
        "total": round(cart.calculate_total(), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)