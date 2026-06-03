[03/06/2026 08:15] Tatiana Msr: python-3.11.9
[03/06/2026 08:27] Tatiana Msr: import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bonjour ! Le bot fonctionne.")

async def run():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()  # keep alive

if name == "main":
    asyncio.run(run())
[03/06/2026 08:34] Tatiana Msr: import os
import requests
from flask import Flask, request

app = Flask(name)

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Bonjour ! Le bot fonctionne 🚀")

    return "ok"

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
