from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# ❌ Intentional vulnerability (for Gitleaks)
JWT_SECRET = "hardcoded-jwt-secret"

users = {
    "user1": {"password": "password123", "role": "user"},
    "admin": {"password": "admin123", "role": "admin"}
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if user and user["password"] == password:
        token = jwt.encode(
            {
                "user": username,
                "role": user["role"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            JWT_SECRET,
            algorithm="HS256"
        )
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/health")
def health():
    return "Auth service running"

if __name__ == "__main__":
    app.run(port=5001)
