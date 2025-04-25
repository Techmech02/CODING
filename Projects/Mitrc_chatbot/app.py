from flask import Flask, request, jsonify
from logic import find_answer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = find_answer(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
