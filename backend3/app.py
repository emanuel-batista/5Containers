from flask import Flask, jsonify
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    products = [
        {"id": 1, "name": "Teclado Mecanico", "price": 299.90},
        {"id": 2, "name": "Mouse Gamer", "price": 159.90},
        {"id": 3, "name": "Headset", "price": 219.90}
    ]

    return jsonify({
        "service": "backend3",
        "description": "API de produtos",
        "status": "ok",
        "environment": os.getenv("BACKEND3_ENV", "dev"),
        "items": products
    })
@app.route("/health")
def health():
    return jsonify({"status": "up"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)