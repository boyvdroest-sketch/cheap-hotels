import os
import telebot
from telebot import types
from datetime import datetime

# Environment variables for security
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_LINK = os.environ.get('CHANNEL_LINK', 'https://t.me/YourAccommodationDeals')
LOG_FILE = "users.txt"

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN not set!")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

def log_user(user_id, username, action="start"):
    try:
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {user_id} - {username} - {action}\n")
    except Exception as e:
        print(f"Logging error: {e}")

def get_seo_accommodation_deals(city="", deal_type=""):
    """Generate SEO-rich accommodation deals with discount keywords"""
    
    deals = {
        "nyc": {
            "title": "🏙️ **New York City Hotel Discounts - Up to 70% OFF Luxury Stays**",
            "deals": [
                "💰 **Times Square Hotels**: $89/night (Was $299)",
                "⭐ **5-Star Manhattan Luxury**: 60% Discount",
                "🏨 **Budget NYC Accommodation**: From $49/night",
                "🛏️ **Boutique Hotel Deals**: 55% OFF Midtown",
                "🌃 **NYC Vacation Rentals**: 50% OFF Apartments",
                "💎 **Last Minute Hotel Discounts**: Same Day Booking",
                "🔥 **Flash Sale**: Limited Time Only!"
            ]
        },
        "miami": {
            "title": "🌴 **Miami Beach Resort Discounts - Beachfront Deals Up to 65% OFF**",
            "deals": [
                "💰 **Oceanfront Resorts**: $99/night (Save $200)",
                "⭐ **Luxury Miami Hotels**: 60% Discount South Beach",
                "🏨 **Budget Miami Stays**: From $59/night",
                "🏝️ **Beach Hotel Specials**: 55% OFF Summer Deals",
                "🌅 **Waterfront Properties**: Discount Vacation Rentals",
                "💎 **All-Inclusive Resort Packages**: 50% OFF",
                "🔥 **Limited Time Beach Deals**"
            ]
        },
        "lasvegas": {
            "title": "🎰 **Las Vegas Strip Hotel Discounts - Casino Resort Deals Up to 75% OFF**",
            "deals": [
                "💰 **Strip Casino Hotels**: $69/night (Was $250)",
                "⭐ **5-Star Vegas Resorts**: 70% Discount",
                "🏨 **Budget Las Vegas**: From $39/night Downtown",
                "🎲 **Weekend Package Deals**: 65% OFF Shows + Room",
                "🏊 **Resort Hotel Specials**: Pool View Discounts",
                "💎 **VIP Suite Upgrades**: 50% OFF Luxury",
                "🔥 **Last Minute Vegas Deals**"
            ]
        },
        "orlando": {
            "title": "🏰 **Orlando Hotel Discounts Near Disney - Theme Park Deals Up to 60% OFF**",
            "deals": [
                "💰 **Disney Area Hotels**: $79/night (Save $120)",
                "⭐ **Family Resort Packages**: 55% Discount",
                "🏨 **Budget Orlando Stays**: From $49/night",
                "🎡 **Theme Park Hotel Bundles**: 50% OFF Tickets",
                "🏰 **Vacation Home Rentals**: 45% OFF Large Groups",
                "💎 **All-Inclusive Resorts**: Waterpark Access Included",
                "🔥 **Theme Park Season Deals**"
            ]
        },
        "all": {
            "title": "🇺🇸 **USA Hotel Discounts - Best Price Guarantee on All Accommodation**",
            "deals": [
                "💰 **Hotel Price Comparison**: Find Lowest Rates",
                "⭐ **Luxury Hotel Discounts**: Up to 70% OFF 5-Star",
                "🏨 **Budget Accommodation**: Cheap Stays From $29/night",
                "🏠 **Vacation Rental Deals**: 50% OFF Apartments",
                "🛏️ **Last Minute Bookings**: Same Day Hotel Discounts",
                "💎 **Extended Stay Discounts**: Weekly/Monthly Rates",
                "🔥 **Flash Sale Deals**: Limited Time Offers"
            ]
        }
    }
    
    if city in deals:
        return deals[city]
    return deals["all"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"
    log_user(user_id, username, "start")
    
    # SEO-rich welcome message
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Primary destinations with discount keywords
    markup.add(
        types.InlineKeyboardButton("🏙️ NYC Hotels 70% OFF", callback_data="seo_nyc"),
        types.InlineKeyboardButton("🌴 Miami Resorts 65% OFF", callback_data="seo_miami")
    )
    markup.add(
        types.InlineKeyboardButton("🎰 Vegas 75% OFF", callback_data="seo_lasvegas"),
        types.InlineKeyboardButton("🏰 Orlando 60% OFF", callback_data="seo_orlando")
    )
    markup.add(
        types.InlineKeyboardButton("🏠 Vacation Rentals", callback_data="seo_rentals"),
        types.InlineKeyboardButton("⭐ Luxury Hotels", callback_data="seo_luxury")
    )
    
    # Action buttons with SEO keywords
    markup.add(
        types.InlineKeyboardButton("💰 Price Comparison", callback_data="seo_comparison"),
        types.InlineKeyboardButton("🔥 Flash Sales", callback_data="seo_flash")
    )
    markup.add(types.InlineKeyboardButton("📢 Join Deals Channel", url=CHANNEL_LINK))
    
    welcome_text = f"""🏨 **ACCOMMODATION DISCOUNT FINDER - Best Hotel Deals USA** 

👋 Welcome, {message.from_user.first_name}! Find **discounted hotel rates**, **cheap vacation rentals**, and **luxury accommodation deals** across the United States.

💰 **EXCLUSIVE DISCOUNTS AVAILABLE:**
• Hotel Discounts Up to 75% OFF
• Luxury Resort Price Drops
• Budget Accommodation Specials
• Vacation Rental Promo Codes
• Last Minute Booking Deals
• Extended Stay Discounts

🏙️ **TOP DISCOUNT DESTINATIONS:**
• **New York City Hotels**: Times Square, Manhattan Luxury Discounts
• **Miami Beach Resorts**: Oceanfront Property Specials
• **Las Vegas Casino Hotels**: Strip Resort Price Cuts
• **Orlando Theme Park Hotels**: Disney Area Budget Stays

⭐ **WHY CHOOSE US:**
✅ Price Match Guarantee
✅ No Hidden Fees
✅ Free Cancellation Options
✅ Best Rate Guarantee
✅ 24/7 Customer Support

Tap a destination above for **exclusive discount codes**!"""

    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(commands=['discounts'])
def show_all_discounts(message):
    user_id = message.from_user.id
    log_user(user_id, "user", "discounts_command")
    
    discounts_text = """🔥 **ACCOMMODATION DISCOUNT TYPES - Limited Time Offers**

💰 **HOTEL DISCOUNT CATEGORIES:**

🏨 **BUDGET ACCOMMODATION DISCOUNTS:**
• Economy Hotels: From $29/night
• Motel Discounts: 50-60% OFF
• Hostel Special Rates: Dorm Bed Deals
• Extended Stay America: Weekly Rates

⭐ **LUXURY HOTEL DISCOUNTS:**
• 5-Star Hotel Price Drops: Up to 70% OFF
• Resort All-Inclusive Packages: 55% Discount
• Boutique Hotel Flash Sales: Limited Rooms
• Spa Resort Specials: Treatment Included

🏠 **VACATION RENTAL DISCOUNTS:**
• Apartment Rentals: 45% OFF Monthly
• Vacation Home Specials: Family Deals
• Condo Resort Discounts: Beachfront Properties
• Cabin Getaway Promotions: Mountain Retreats

🕒 **TIMING-BASED DISCOUNTS:**
• Last Minute Hotel Deals: Same Day Discounts
• Early Bird Specials: Book 60 Days Advance
• Weekend Getaway Packages: Friday-Sunday
• Seasonal Sales: Summer/Winter Promotions

💡 **PRO TIP**: Always check for **promo codes** and **member rates** for extra savings!"""

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🏙️ View NYC Hotel Discounts", callback_data="seo_nyc"))
    markup.add(types.InlineKeyboardButton("📢 Join for Promo Codes", url=CHANNEL_LINK))
    
    bot.send_message(message.chat.id, discounts_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(commands=['deals'])
def show_current_deals(message):
    user_id = message.from_user.id
    log_user(user_id, "user", "deals_command")
    
    deals_text = """🎯 **CURRENT ACCOMMODATION DEALS - Limited Time**

🔥 **FLASH SALE ACTIVE: 72-HOUR SALE**

🏨 **HOTEL CHAIN DISCOUNTS:**
• **Marriott Hotels**: 50% OFF + Free Breakfast
• **Hilton Properties**: 55% Discount + Late Checkout
• **Hyatt Hotels**: 60% OFF + Room Upgrade
• **IHG Hotels**: 45% OFF (Holiday Inn, Crowne Plaza)
• **Wyndham Resorts**: 50% Discount All Locations

🏠 **VACATION RENTAL PLATFORM DEALS:**
• **Airbnb Discounts**: 40% OFF First Booking
• **VRBO Specials**: 35% OFF Vacation Homes
• **Booking.com Promo**: Genius Level 2 Discounts
• **Expedia Packages**: Bundle & Save 30%

⭐ **LUXURY COLLECTION:**
• Four Seasons: 25% OFF Advance Purchase
• Ritz-Carlton: 30% Discount Resort Credits
• Waldorf Astoria: 35% OFF + $100 Credit
• St. Regis: Complimentary Night Offer

💰 **BUDGET OPTIONS:**
• Motel 6: From $49/night All Locations
• Red Roof Inn: 40% OFF Weekly Rates
• Super 8: $55/night Best Price Guarantee
• Days Inn: Free Cancellation + Discount"""

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🏨 Hotel Chains", callback_data="seo_chains"),
        types.InlineKeyboardButton("🏠 Vacation Rentals", callback_data="seo_rentals")
    )
    markup.add(types.InlineKeyboardButton("📢 Join for Booking Links", url=CHANNEL_LINK))
    
    bot.send_message(message.chat.id, deals_text, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = call.from_user.id
    
    if call.data.startswith('seo_'):
        option = call.data.replace('seo_', '')
        log_user(user_id, "user", f"clicked_{option}")
        
        if option in ["nyc", "miami", "lasvegas", "orlando"]:
            deal_info = get_seo_accommodation_deals(option)
            response_text = deal_info["title"] + "\n\n" + "\n".join(deal_info["deals"])
            
        elif option == "rentals":
            response_text = """🏠 **VACATION RENTAL DISCOUNTS - Apartments, Homes, Condos**

💰 **DISCOUNT VACATION RENTAL TYPES:**
• Beachfront Condos: 50% OFF Ocean Views
• Mountain Cabins: 45% Discount Getaways
• City Apartments: 40% OFF Downtown Locations
• Luxury Villas: 55% OFF Private Pools

🏡 **POPULAR RENTAL PLATFORM DEALS:**
• Airbnb: 40% OFF First Booking + Cleaning Fee Waived
• VRBO: 35% Discount + No Service Fees
• Booking.com Vacation Rentals: Genius Discounts
• HomeAway: Last Minute Rental Deals

⭐ **BENEFITS OF VACATION RENTALS:**
✅ More Space for Families/Groups
✅ Kitchen Facilities (Save on Dining)
✅ Privacy & Exclusive Use
✅ Local Neighborhood Experience
✅ Often Cheaper Than Hotels (Per Person)

💡 **TIP**: Book **weekly or monthly** for additional discounts!"""
        
        elif option == "luxury":
            response_text = """⭐ **LUXURY HOTEL DISCOUNTS - 5-Star Accommodation Deals**

🏨 **LUXURY HOTEL CATEGORIES:**
• 5-Star City Hotels: 60% OFF Rack Rates
• Beach Resorts: All-Inclusive Discounts
• Boutique Design Hotels: 55% OFF Unique Stays
• Spa Retreats: Treatment Package Deals

💰 **LUXURY CHAIN DISCOUNTS:**
• Four Seasons: Advance Purchase 25% OFF
• Ritz-Carlton: 30% Discount + Resort Credit
• St. Regis: 4th Night Free Promotions
• Waldorf Astoria: Suite Upgrade Offers
• Mandarin Oriental: Dining Credit Included

🎁 **LUXURY AMENITIES INCLUDED:**
✅ Butler Service
✅ Premium Toiletries
✅ High-End Dining
✅ Spa Access
✅ Concierge Services
✅ Luxury Transportation

💎 **BOOKING TIP**: Check for **"Secret Rates"** and **"Member Exclusive"** deals!"""
        
        elif option == "comparison":
            response_text = """💰 **HOTEL PRICE COMPARISON - Find Lowest Rates**

🔍 **COMPARE ACROSS ALL PLATFORMS:**
• Direct Hotel Website Rates
• Online Travel Agencies (OTAs)
• Membership Program Prices
• Package Deal Bundles

📊 **PRICE COMPARISON TOOLS:**
1. **Rate Comparison**: Check 10+ sites simultaneously
2. **Historical Pricing**: See price trends for your dates
3. **Price Alerts**: Get notified when prices drop
4. **Member Rate Checks**: Exclusive discount verification

🏨 **WHERE TO COMPARE:**
• Direct vs. Third-Party Rates
• Bundle Deals (Flight + Hotel)
• Last Minute vs. Advance Booking
• Flexible Date Pricing

💡 **MONEY-SAVING STRATEGY:**
1. Always check hotel website directly
2. Use incognito mode for searches
3. Clear cookies before checking rates
4. Consider package deals for extra savings
5. Book refundable rates when possible"""
        
        elif option == "flash":
            response_text = """🔥 **FLASH SALE ACCOMMODATION - 24-72 Hour Deals**

⏰ **CURRENT FLASH SALES:**
• 24-HOUR SALE: NYC Luxury Hotels 70% OFF
• 48-HOUR DEAL: Miami Beach Resorts 65% Discount
• 72-HOUR SPECIAL: Las Vegas Strip 75% OFF
• WEEKEND FLASH: Orlando Theme Park Hotels 60% OFF

🎯 **FLASH SALE FEATURES:**
✅ Limited Room Inventory
✅ Non-Refundable Rates (Lower Prices)
✅ Must Book Within Time Window
✅ Blackout Dates May Apply
✅ Additional Perks Included

🚨 **HOW TO CATCH FLASH SALES:**
1. Join our Telegram channel for instant alerts
2. Enable push notifications
3. Check daily at 9 AM EST (New sales launch)
4. Have payment ready for quick booking
5. Be flexible with travel dates

💎 **PRO TIP**: Flash sales often have **"Hidden City"** and **"Mystery Hotel"** deals with extra discounts!"""
        
        elif option == "chains":
            response_text = """🏨 **HOTEL CHAIN DISCOUNTS - Brand-Specific Deals**

🇺🇸 **MAJOR HOTEL CHAINS - EXCLUSIVE DISCOUNTS:**

**MARRIOTT BONVOY:**
• 50% OFF Participating Properties
• Free Night Certificates
• Elite Status Benefits
• Points Bonus Offers

**HILTON HONORS:**
• 55% Discount Advance Purchase
• Digital Key & Mobile Check-in
• Free Wi-Fi for Members
• Fifth Night Free on Points

**IHG HOTELS & RESORTS:**
• 45% OFF Holiday Inn, Crowne Plaza
• PointBreaks Discounts
• Accelerate Promotions
• Member Exclusive Rates

**HYATT WORLD:**
• 60% OFF Park Hyatt, Grand Hyatt
• Category 1-4 Free Night Awards
• Discoverist/Globalist Benefits
• Milestone Rewards

**WYNDHAM REWARDS:**
• 50% Discount All Brands
• Go Free Awards
• Late Checkout Privileges
• Suite Upgrade Opportunities

💡 **TIP**: Always join **loyalty programs** for best rates!"""
        
        # Add booking button
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📢 Join for Booking & Promo Codes", url=CHANNEL_LINK))
        markup.add(
            types.InlineKeyboardButton("💰 More Discounts", callback_data="seo_comparison"),
            types.InlineKeyboardButton("🔥 Flash Sales", callback_data="seo_flash")
        )
        
        bot.send_message(call.message.chat.id, response_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_id = message.from_user.id
    user_text = message.text.lower()
    
    # SEO keyword detection in user messages
    response = """🏨 **Accommodation Discount Bot**

I specialize in finding the **best hotel discounts**, **vacation rental deals**, and **luxury accommodation promotions**!

💡 **Try these commands:**
/start - Main menu with all options
/discounts - Types of accommodation discounts
/deals - Current limited-time offers

🔍 **Popular searches:**
• "New York hotel discounts"
• "Miami beach resort deals"
• "Las Vegas casino hotel promotions"
• "Orlando theme park packages"
• "Luxury hotel price drops"
• "Budget accommodation specials"

Join our channel for **exclusive promo codes** and **instant booking links**!"""
    
    bot.send_message(message.chat.id, response, parse_mode='Markdown')

if __name__ == "__main__":
    print("🏨 SEO Accommodation Bot is running...")
    bot.polling(none_stop=True)