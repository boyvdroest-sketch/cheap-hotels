from flask import Flask, render_template_string
import threading
import time
import os

app = Flask(__name__)

# SEO-optimized HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Discounts Finder | Cheap Accommodation Deals USA | Luxury Hotel Promotions</title>
    <meta name="description" content="Find best hotel discounts, cheap accommodation deals, luxury hotel promotions, vacation rental specials. Up to 75% OFF hotels in NYC, Miami, Las Vegas, Orlando.">
    <meta name="keywords" content="hotel discounts, cheap accommodation, luxury hotel deals, vacation rental discounts, hotel promo codes, budget hotels, last minute hotel deals, extended stay discounts">
    <meta name="robots" content="index, follow">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { background: rgba(255,255,255,0.95); padding: 40px; border-radius: 20px; margin-bottom: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .keyword-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; }
        .keyword-card { background: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease; }
        .keyword-card:hover { transform: translateY(-5px); }
        .discount-badge { background: #ff6b6b; color: white; padding: 5px 15px; border-radius: 20px; display: inline-block; margin: 10px 0; font-weight: bold; }
        .seo-list { columns: 2; gap: 20px; margin: 20px 0; }
        .seo-item { background: #f8f9fa; padding: 15px; margin-bottom: 15px; border-radius: 10px; break-inside: avoid; }
        @media (max-width: 768px) { .seo-list { columns: 1; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏨 Accommodation Discounts Finder Bot</h1>
            <p class="subtitle">Find <strong>hotel discounts</strong>, <strong>cheap accommodation deals</strong>, and <strong>luxury hotel promotions</strong> across USA</p>
        </div>

        <div style="background: white; padding: 30px; border-radius: 15px; margin-bottom: 30px;">
            <h2>💰 Top Accommodation Discount Categories</h2>
            <div class="keyword-grid">
                <div class="keyword-card">
                    <h3>🏙️ New York City Hotels</h3>
                    <div class="discount-badge">UP TO 70% OFF</div>
                    <p>Times Square, Manhattan luxury discounts, budget NYC accommodation</p>
                </div>
                <div class="keyword-card">
                    <h3>🌴 Miami Beach Resorts</h3>
                    <div class="discount-badge">UP TO 65% OFF</div>
                    <p>Oceanfront property specials, South Beach luxury hotel deals</p>
                </div>
                <div class="keyword-card">
                    <h3>🎰 Las Vegas Casino Hotels</h3>
                    <div class="discount-badge">UP TO 75% OFF</div>
                    <p>Strip resort price cuts, weekend package deals, VIP suite upgrades</p>
                </div>
                <div class="keyword-card">
                    <h3>🏰 Orlando Theme Park Hotels</h3>
                    <div class="discount-badge">UP TO 60% OFF</div>
                    <p>Disney area budget stays, family resort packages, vacation home rentals</p>
                </div>
            </div>
        </div>

        <div style="background: white; padding: 30px; border-radius: 15px; margin-bottom: 30px;">
            <h2>🔍 SEO Accommodation Keywords We Target</h2>
            <div class="seo-list">
                <div class="seo-item">
                    <h4>🏨 Hotel Discount Keywords</h4>
                    <p>• hotel discounts • cheap hotels • luxury hotel deals • budget accommodation • last minute hotel deals</p>
                </div>
                <div class="seo-item">
                    <h4>🏠 Vacation Rental Keywords</h4>
                    <p>• vacation rental discounts • apartment rentals • beachfront condos • mountain cabins • city apartments</p>
                </div>
                <div class="seo-item">
                    <h4>💰 Price & Deal Keywords</h4>
                    <p>• hotel price drops • accommodation specials • promo codes • flash sales • extended stay discounts</p>
                </div>
                <div class="seo-item">
                    <h4>⭐ Luxury Keywords</h4>
                    <p>• 5-star hotel discounts • luxury resort deals • boutique hotels • spa retreats • premium accommodation</p>
                </div>
                <div class="seo-item">
                    <h4>🕒 Timing Keywords</h4>
                    <p>• last minute bookings • early bird specials • weekend getaways • seasonal promotions • holiday deals</p>
                </div>
                <div class="seo-item">
                    <h4>📍 Location Keywords</h4>
                    <p>• NYC hotel deals • Miami resort discounts • Las Vegas casino hotels • Orlando theme park packages</p>
                </div>
            </div>
        </div>

        <div style="background: white; padding: 30px; border-radius: 15px; margin-bottom: 30px;">
            <h2>🔥 Current Limited Time Offers</h2>
            <div style="background: #fff5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
                <h3>🏨 Hotel Chain Discounts</h3>
                <p><strong>Marriott Hotels:</strong> 50% OFF + Free Breakfast</p>
                <p><strong>Hilton Properties:</strong> 55% Discount + Late Checkout</p>
                <p><strong>Hyatt Hotels:</strong> 60% OFF + Room Upgrade</p>
                <p><strong>IHG Hotels:</strong> 45% OFF All Locations</p>
            </div>
            <div style="background: #f0f9ff; padding: 20px; border-radius: 10px; margin: 20px 0;">
                <h3>🏠 Vacation Rental Deals</h3>
                <p><strong>Airbnb:</strong> 40% OFF First Booking</p>
                <p><strong>VRBO:</strong> 35% Discount + No Service Fees</p>
                <p><strong>Booking.com:</strong> Genius Level 2 Discounts</p>
            </div>
        </div>

        <div style="background: #e8f4f8; padding: 25px; border-radius: 15px; text-align: center;">
            <h3>🚀 Ready to Find Accommodation Discounts?</h3>
            <p>Start our Telegram bot to access exclusive <strong>hotel discounts</strong>, <strong>promo codes</strong>, and <strong>limited-time accommodation deals</strong>!</p>
            <p style="margin-top: 15px;"><strong>Bot Status:</strong> <span style="color: green;">✅ Online & Finding Discounts</span></p>
            <p style="font-style: italic; margin-top: 10px;">Specializing in: hotel price drops, luxury accommodation promotions, vacation rental discounts, budget hotel deals</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return "🏨 Accommodation Bot Healthy"

@app.route('/sitemap')
def sitemap():
    return {
        "pages": [
            {"url": "/", "title": "Accommodation Discounts Finder", "keywords": ["hotel discounts", "cheap accommodation"]},
            {"url": "/health", "title": "Health Check"},
        ],
        "keywords": [
            "hotel discounts", "cheap accommodation", "luxury hotel deals", 
            "vacation rental discounts", "budget hotels", "last minute hotel deals",
            "extended stay discounts", "hotel promo codes", "accommodation specials"
        ]
    }

def run_bot():
    try:
        from bot import bot
        print("🏨 Starting SEO Accommodation Bot...")
        bot.remove_webhook()
        time.sleep(2)
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"❌ Bot error: {e}")
        print("🔄 Restarting in 30 seconds...")
        time.sleep(30)
        run_bot()

if __name__ == '__main__':
    # Start bot in separate thread
    if os.environ.get('RENDER'):
        bot_thread = threading.Thread(target=run_bot)
        bot_thread.daemon = True
        bot_thread.start()
    
    app.run(host='0.0.0.0', port=5000, debug=False)