import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            requests.post(f"{URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": "Bonjour ! Le bot fonctionne 🚀"
            })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
