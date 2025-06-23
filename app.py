// app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Backend is running"})

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    return jsonify({"message": "Data received", "data": data})

if __name__ == "__main__":
    app.run(debug=True)
