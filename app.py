from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = "8681196349:AAHt3SDMLHvQOshjo9Y4yzVagBghgWI06tY"
CHAT_ID = "7536971297"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        message = data.get('message', '🚨 নতুন ট্রেডিং সিগন্যাল!')
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        requests.post(telegram_url, json=payload)
        return "Success", 200
    return "Invalid Data", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
