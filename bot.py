import os
import telebot
from telebot import types
from datetime import datetime

# ========== SECURE TOKEN HANDLING ==========
# Get from environment variables - NEVER hardcode tokens!
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_LINK = os.environ.get('CHANNEL_LINK', 'https://t.me/YourAccommodationDeals')

# Critical check: Exit if no token
if not BOT_TOKEN:
    print("❌ CRITICAL ERROR: BOT_TOKEN environment variable is not set!")
    print("💡 Set it in Render dashboard: Environment → Add BOT_TOKEN")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)
print("✅ Bot token loaded securely from environment variables")

# ========== SEO KEYWORD DATABASE ==========
SEO_KEYWORDS = {
    "primary": [
        "hotel discounts", "cheap accommodation", "budget hotels", 
        "hotel deals", "discount hotels", "affordable stays",
        "luxury hotel discounts", "vacation rental deals",
        "last minute hotel deals", "hotel booking discounts"
    ],
    "secondary": [
        "cheap hotel rooms", "discounted accommodation", 
        "hotel savings", "budget friendly hotels",
        "hotel promotions", "discount travel stays",
        "luxury stays cheap", "vacation discounts"
    ],
    "location": [
        "New York hotel deals", "Miami resort discounts",
        "Las Vegas hotel promotions", "Orlando accommodation discounts",
        "USA hotel discounts", "beach resort deals"
    ]
}

# ========== USER LOGGING ==========
def log_user(user_id, username, action="start"):
    """Log user activity securely"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Don't store sensitive info in production
        with open("activity.log", "a") as f:
            f.write(f"{timestamp} - User Action: {action}\n")
    except:
        pass

# ========== SEO-RICH RESPONSE GENERATOR ==========
def generate_seo_response(topic):
    """Generate SEO-optimized responses with keywords"""
    
    responses = {
        "nyc": {
            "title": "🏙️ **New York City Hotel Discounts - Find Cheap Hotels & Best Deals**",
            "content": """
💰 **EXCLUSIVE NYC HOTEL DISCOUNTS AVAILABLE:**

• **Times Square Hotel Deals**: From $89/night (Save up to 70%)
• **Manhattan Luxury Accommodation**: 60% Discount on 5-Star Stays
• **Budget Hotels New York**: Cheap Rooms from $49/night
• **Midtown Boutique Hotels**: 55% OFF Unique Stays

🔍 **POPULAR NYC AREAS FOR DISCOUNTED STAYS:**
Times Square Hotels | Midtown Manhattan Accommodation | Downtown Luxury Stays

💡 **SEO TIP**: Book directly for additional discounts on New York City hotels!
"""
        },
        "miami": {
            "title": "🌴 **Miami Beach Resort Discounts - Cheap Oceanfront Accommodation**",
            "content": """
💰 **EXCLUSIVE MIAMI BEACH RESORT DEALS:**

• **Oceanfront Hotel Discounts**: $99/night Beachfront Properties
• **South Beach Luxury Hotels**: 65% Discount on Premium Stays
• **Budget Miami Accommodation**: Affordable Rooms from $59/night
• **All-Inclusive Resort Packages**: 50% OFF Family Vacations

🏖️ **BEST DISCOUNT BEACH AREAS:**
South Beach Oceanfront Deals | Miami Beach Luxury Discounts | Downtown Miami Hotels

💡 **SEO TIP**: Search for "last minute Miami hotel deals" for extra savings!
"""
        },
        "luxury": {
            "title": "⭐ **Luxury Hotel Discounts - 5-Star Accommodation Deals & Promotions**",
            "content": """
💰 **EXCLUSIVE LUXURY HOTEL SAVINGS:**

• **5-Star Hotel Price Drops**: Up to 70% OFF Premium Properties
• **Boutique Luxury Stays**: 55% Discount on Unique Accommodation
• **Spa Resort Specials**: All-Inclusive Wellness Packages
• **Design Hotel Promotions**: Limited Time Luxury Deals

🏨 **TOP LUXURY BRANDS WITH DISCOUNTS:**
Four Seasons | Ritz-Carlton | Waldorf Astoria | St. Regis | Mandarin Oriental

💡 **SEO TIP**: Book luxury accommodation 60+ days early for best rates!
"""
        },
        "rentals": {
            "title": "🏠 **Vacation Rental Discounts - Cheap Apartment & Home Deals**",
            "content": """
💰 **EXCLUSIVE VACATION RENTAL SAVINGS:**

• **Beachfront Condo Deals**: 50% OFF Ocean View Properties
• **City Apartment Discounts**: 45% OFF Downtown Accommodation
• **Mountain Cabin Specials**: Affordable Getaway Rentals
• **Luxury Villa Promotions**: Private Pool Homes Discounted

🔑 **BEST RENTAL PLATFORMS FOR DISCOUNTS:**
Airbnb Promo Codes | VRBO Special Offers | Booking.com Vacation Rentals

💡 **SEO TIP**: Search "vacation rental discounts near me" for local deals!
"""
        },
        "budget": {
            "title": "💰 **Budget Hotel Discounts - Cheap Accommodation Under $50/Night**",
            "content": """
💰 **EXCLUSIVE BUDGET ACCOMMODATION DEALS:**

• **Economy Hotel Discounts**: Rooms from $29/night USA-Wide
• **Motel Special Rates**: 50-60% OFF Road Trip Stops
• **Hostel Bed Deals**: Dorm Accommodation from $15/night
• **Extended Stay Discounts**: Weekly/Monthly Rate Savings

🏨 **BUDGET HOTEL CHAINS WITH DISCOUNTS:**
Motel 6 | Red Roof Inn | Super 8 | Days Inn | Travelodge

💡 **SEO TIP**: Book budget hotels mid-week for cheapest rates!
"""
        }
    }
    
    return responses.get(topic, {
        "title": "🏨 **Accommodation Discounts - Best Hotel Deals & Cheap Stays**",
        "content": "Find exclusive discounts on hotels, resorts, and vacation rentals!"
    })

# ========== BOT COMMAND HANDLERS ==========
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "User"
    log_user(user_id, username, "started_bot")
    
    # SEO-optimized welcome message
    welcome_text = f"""🏨 **ACCOMMODATION DISCOUNTS BOT - Find Cheap Hotels & Best Deals**

👋 Welcome, {message.from_user.first_name}! I help you find **hotel discounts**, **cheap accommodation**, and **luxury stay deals** across the USA.

🔍 **POPULAR SEARCH KEYWORDS I COVER:**
• Hotel discounts & cheap stays
• Budget accommodation deals
• Luxury hotel promotions
• Vacation rental discounts
• Last minute hotel deals
• Extended stay savings

💰 **CURRENT DISCOUNT CATEGORIES:**

"""
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # SEO-optimized buttons with keywords
    markup.add(
        types.InlineKeyboardButton("🏙️ NYC Hotel Discounts", callback_data="seo_nyc"),
        types.InlineKeyboardButton("🌴 Miami Beach Deals", callback_data="seo_miami")
    )
    markup.add(
        types.InlineKeyboardButton("⭐ Luxury Hotel Deals", callback_data="seo_luxury"),
        types.InlineKeyboardButton("🏠 Vacation Rental Deals", callback_data="seo_rentals")
    )
    markup.add(
        types.InlineKeyboardButton("💰 Budget Hotel Deals", callback_data="seo_budget"),
        types.InlineKeyboardButton("🎰 Vegas Hotel Promos", callback_data="seo_vegas")
    )
    
    # Call-to-action buttons
    markup.add(types.InlineKeyboardButton("🔍 Search All Deals", callback_data="seo_all"))
    markup.add(types.InlineKeyboardButton("📢 Join Discount Channel", url=CHANNEL_LINK))
    
    # SEO footer
    footer = """

💡 **SEO TIPS FOR BEST DISCOUNTS:**
• Search "hotel discounts + [your city]"
• Use "last minute hotel deals" for urgent bookings
• Check "luxury hotel promotions" for premium stays
• Look for "vacation rental discounts" for group travel

Tap a category above to start saving! 💰"""

    bot.send_message(message.chat.id, welcome_text + footer, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(commands=['discounts'])
def show_discounts(message):
    log_user(message.from_user.id, "user", "viewed_discounts")
    
    discounts_text = """🔍 **ACCOMMODATION DISCOUNT CATEGORIES - SEO OPTIMIZED**

🏨 **HOTEL DISCOUNT TYPES:**

1. **Last Minute Hotel Deals**
   - Same day booking discounts
   - Urgent accommodation savings
   - Emergency stay promotions

2. **Early Bird Hotel Discounts**
   - Advance booking specials
   - 60+ day reservation savings
   - Seasonal rate guarantees

3. **Weekend Getaway Deals**
   - Friday-Sunday packages
   - Romantic escape discounts
   - Family weekend specials

4. **Extended Stay Discounts**
   - Weekly rate savings
   - Monthly accommodation deals
   - Long term stay promotions

5. **Loyalty Program Discounts**
   - Member exclusive rates
   - Points redemption deals
   - Elite status benefits

💡 **SEO SEARCH TIPS:**
Search: "[city] hotel discounts this weekend"
Search: "cheap last minute hotels near me"
Search: "luxury hotel promotions [month]"

Join our channel for daily discount alerts! 📢"""
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join for Exclusive Deals", url=CHANNEL_LINK))
    
    bot.send_message(message.chat.id, discounts_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(commands=['search'])
def search_deals(message):
    log_user(message.from_user.id, "user", "searched_deals")
    
    search_text = """🔍 **HOW TO SEARCH FOR ACCOMMODATION DISCOUNTS**

💡 **BEST SEO SEARCH TERMS:**

🏨 **For Hotel Discounts:**
• "hotel discounts [city name]"
• "cheap hotels near [landmark]"
• "last minute hotel deals [city]"
• "budget accommodation [area]"
• "luxury hotel promotions [destination]"

🏠 **For Vacation Rentals:**
• "vacation rental discounts [location]"
• "cheap apartment rentals [city]"
• "beachfront condo deals [beach name]"
• "mountain cabin discounts [region]"

💰 **For Budget Stays:**
• "hotels under $50 [city]"
• "cheapest accommodation [destination]"
• "affordable stays [location]"
• "budget friendly hotels [area]"

📍 **Location-Specific Searches:**
• "New York City hotel discounts"
• "Miami Beach resort deals"
• "Las Vegas strip hotel promotions"
• "Orlando theme park hotel discounts"

🕒 **Timing-Based Searches:**
• "hotel deals this weekend"
• "summer accommodation discounts"
• "winter getaway promotions"
• "holiday hotel specials"

💎 **PRO SEO TIP:** Use specific dates for best results!
Example: "hotel discounts NYC December 15-20" """
    
    bot.send_message(message.chat.id, search_text, parse_mode='Markdown')

@bot.message_handler(commands=['keywords'])
def show_keywords(message):
    log_user(message.from_user.id, "user", "viewed_keywords")
    
    keywords_text = """🔑 **SEO KEYWORDS FOR ACCOMMODATION DISCOUNTS**

🏨 **PRIMARY KEYWORDS (High Volume):**
• hotel discounts
• cheap accommodation
• budget hotels
• hotel deals
• discount hotels
• affordable stays

⭐ **SECONDARY KEYWORDS (Medium Volume):**
• luxury hotel discounts
• vacation rental deals
• last minute hotel deals
• hotel booking discounts
• cheap hotel rooms
• discounted accommodation

💰 **MONEY-SAVING KEYWORDS:**
• hotel savings
• budget friendly hotels
• hotel promotions
• discount travel stays
• luxury stays cheap
• vacation discounts

📍 **LOCATION-BASED KEYWORDS:**
• New York hotel deals
• Miami resort discounts
• Las Vegas hotel promotions
• Orlando accommodation discounts
• USA hotel discounts
• beach resort deals

⏰ **TIMING KEYWORDS:**
• last minute deals
• weekend getaway discounts
• seasonal hotel promotions
• holiday accommodation deals
• summer hotel discounts
• winter stay specials

💡 **LONG-TAIL KEYWORDS (Specific):**
• "cheap hotels near Times Square"
• "luxury Miami Beach resorts discounts"
• "family friendly Orlando hotel deals"
• "romantic getaway hotel promotions"
• "business hotel discounts downtown"

Use these keywords when searching for the best deals! 🔍"""
    
    bot.send_message(message.chat.id, keywords_text, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = call.from_user.id
    action = call.data.replace('seo_', '')
    log_user(user_id, "user", f"clicked_{action}")
    
    response = generate_seo_response(action)
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join for Booking & Promo Codes", url=CHANNEL_LINK))
    
    # Add related searches
    if action == "nyc":
        markup.add(types.InlineKeyboardButton("🔍 Search: NYC Hotel Discounts", callback_data="seo_search_nyc"))
    elif action == "miami":
        markup.add(types.InlineKeyboardButton("🔍 Search: Miami Resort Deals", callback_data="seo_search_miami"))
    
    bot.send_message(call.message.chat.id, response["title"] + "\n" + response["content"], reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text.lower()
    
    # SEO keyword detection and response
    response_map = {
        "hotel": "🏨 Looking for **hotel discounts**? Try /start to see all categories!",
        "cheap": "💰 Want **cheap accommodation deals**? I've got exclusive discounts! Use /start",
        "discount": "💸 **Discount hotels** available! Tap /start to browse deals",
        "luxury": "⭐ **Luxury hotel promotions** waiting! Use /start to see premium deals",
        "rental": "🏠 **Vacation rental discounts** available! Check /start for options",
        "budget": "💳 **Budget hotel deals** under $50! Use /start to find cheap stays",
        "new york": "🏙️ **NYC hotel discounts** up to 70% OFF! Tap /start and select NYC",
        "miami": "🌴 **Miami resort deals** with beach access! Use /start and select Miami",
        "las vegas": "🎰 **Vegas hotel promotions** on the Strip! Use /start and select Vegas",
        "orlando": "🏰 **Orlando hotel discounts** near theme parks! Use /start and select Orlando"
    }
    
    response = "🏨 I help find **accommodation discounts**, **hotel deals**, and **cheap stays**! Try /start to begin."
    
    for keyword, reply in response_map.items():
        if keyword in user_text:
            response = reply
            break
    
    bot.reply_to(message, response, parse_mode='Markdown')

# ========== START THE BOT ==========
if __name__ == "__main__":
    print("=" * 50)
    print("🏨 ACCOMMODATION DISCOUNTS BOT")
    print("=" * 50)
    print("✅ Token loaded from environment variables")
    print("✅ SEO keywords database loaded")
    print("✅ Starting bot with polling...")
    print("=" * 50)
    
    # Start with polling
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"❌ Bot error: {e}")
        print("🔄 Restarting in 30 seconds...")
        import time
        time.sleep(30)
        # Restart
        exec(open(__file__).read())
