from flask import Flask, request, jsonify
from calendar_helper import create_event

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ GPT Calendar Assistant 正常運作中"

@app.route("/add-event", methods=["POST"])
def add_event():
    data = request.get_json()
    title = data.get("title")
    start = data.get("start")
    end = data.get("end")

    if not title or not start or not end:
        return jsonify({"error": "缺少參數"}), 400

    result = create_event(title, start, end)
    return jsonify({"status": "success", "event": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
