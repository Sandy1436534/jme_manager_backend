from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Health check route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Backend is running"})

# Submit route (optional test/demo route)
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    return jsonify({"message": "Data received", "data": data})

# Dummy login data
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "emp1": {"password": "emp123", "role": "employee"}
}

work_entries = []

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = users.get(data.get("username"))
    if user and user["password"] == data.get("password"):
        return jsonify({"status": "success", "role": user["role"]})
    return jsonify({"status": "fail"}), 401

@app.route("/work/add", methods=["POST"])
def add_work():
    data = request.json
    work_entries.append(data)
    return jsonify({"status": "success", "data": data})

@app.route("/work/list", methods=["GET"])
def list_work():
    return jsonify({"entries": work_entries})

@app.route("/employee/list", methods=["GET"])
def list_employees():
    return jsonify([{"name": name, "role": details["role"]} for name, details in users.items()])

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the port from environment
    app.run(host="0.0.0.0", port=port, debug=True)