
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for demo
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

if __name__ == "__main__":
    app.run(debug=True)
    