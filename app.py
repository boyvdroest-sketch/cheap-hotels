# app.py
from flask import Flask
import threading
from bot import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "USA Cheap Stays Bot is LIVE! | Finding you the best hotel deals in USA"

def run_bot():
    print("Starting polling for @USACheapStaysBot...")
    bot.polling(none_stop=True, interval=0)

# Start bot in background when deployed
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
