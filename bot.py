# bot.py
import telebot
from telebot import types

BOT_TOKEN = "8549761838:AAGNg3CH2TLZ1QO3frF7bAsCfZ0EjHrJnm4"  # ← Change this!
CHANNEL_LINK = "https://t.me/YourDiscountChannel"  # ← Your channel
LOG_FILE = "users.txt"

bot = telebot.TeleBot(BOT_TOKEN)

def log_user(user_id, username):
    entry = f"{user_id} - @{username}" if username else str(user_id)
    try:
        with open(LOG_FILE) as f:
            if entry not in f.read():
                with open(LOG_FILE, "a") as f:
                    f.write(entry + "\n")
    except:
        with open(LOG_FILE, "a") as f:
            f.write(entry + "\n")

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    log_user(user.id, user.username)
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Join Channel for Daily Deals", url=CHANNEL_LINK))
    markup.add(types.InlineKeyboardButton("See Latest Offers", url="https://t.me/YourDiscountChannel"))

    bot.reply_to(message, 
        "USA Cheap Stays Bot\n\n"
        "Save up to 70% on hotels, motels, Airbnb & hostels across the United States!\n\n"
        "Popular cities:\n"
        "• New York • Los Angeles • Miami • Las Vegas\n"
        "• Orlando • Chicago • San Francisco • Boston\n\n"
        "Join our channel below to get secret last-minute deals first!",
        reply_markup=markup, parse_mode="Markdown")

print("USA Cheap Stays Bot loaded!")
