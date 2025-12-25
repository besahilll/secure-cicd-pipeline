from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

JWT_SECRET = "hardcoded-jwt-secret"  # same secret (intentional)

orders = {
    1: {"user": "user1", "item": "Laptop", "price": 1200},
    2: {"user": "admin", "item": "Server", "price": 5000}
}

@app.route("/orders/<int:order_id>")
def get_order(order_id):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        requesting_user = decoded.get("user")
    except Exception:
        return jsonify({"error": "Invalid token"}), 401

    # ❌ Intentional IDOR (no ownership check)
    return jsonify(orders.get(order_id, {}))

@app.route("/health")
def health():
    return "Orders service running"

if __name__ == "__main__":
    app.run(port=5002)
