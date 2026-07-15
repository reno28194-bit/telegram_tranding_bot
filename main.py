import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import aiohttp
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
COINGECKO_API = "https://api.coingecko.com/api/v3"

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# States untuk conversation
TRACKING_COIN = range(1)

# Dictionary untuk track user tracking list
user_tracking = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    user_name = update.effective_user.first_name
    welcome_text = f"""
🤖 Selamat datang {user_name}!

Saya adalah Trading Bot dengan AI. Saya bisa membantu kamu:

📊 Fitur:
• /price <coin> - Cek harga crypto
• /track <coin> - Track harga crypto otomatis
• /untrack <coin> - Berhenti tracking
• /mytracks - Lihat list tracking kamu
• /analyze <coin> - Analisis AI untuk coin
• /help - Bantuan lengkap

Contoh: /price bitcoin
    """
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = """
📖 PANDUAN LENGKAP

🔍 PERINTAH HARGA:
/price bitcoin - Cek harga Bitcoin sekarang
/price ethereum - Cek harga Ethereum

📈 TRACKING OTOMATIS:
/track bitcoin - Mulai tracking Bitcoin
/mytracks - Lihat semua tracking kamu
/untrack bitcoin - Henti tracking

🤖 AI ANALYSIS:
/analyze bitcoin - Dapatkan analisis AI

💡 TIPS:
• Gunakan nama coin lowercase (bitcoin, ethereum, etc)
• Tracking bisa untuk multiple coins
• Bot akan beri notifikasi jika ada perubahan harga

❓ Butuh bantuan? Ketik /start
    """
    await update.message.reply_text(help_text)

async def get_crypto_price(coin_name: str) -> dict:
    """Fetch crypto price from CoinGecko API"""
    try:
        url = f"{COINGECKO_API}/simple/price"
        params = {
            "ids": coin_name.lower(),
            "vs_currencies": "usd,idr",
            "include_market_cap": "true",
            "include_24hr_vol": "true",
            "include_24hr_change": "true"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if coin_name.lower() in data:
                        return data[coin_name.lower()]
                    return None
    except Exception as e:
        logger.error(f"Error fetching price: {e}")
        return None

async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get crypto price"""
    if not context.args:
        await update.message.reply_text(
            "❌ Format salah!\n\nGunakan: /price <nama_coin>\n\nContoh: /price bitcoin"
        )
        return
    
    coin_name = " ".join(context.args)
    await update.message.reply_text(f"⏳ Mengecek harga {coin_name}...")
    
    price_data = await get_crypto_price(coin_name)
    
    if price_data:
        usd_price = price_data.get('usd', 'N/A')
        idr_price = price_data.get('idr', 'N/A')
        market_cap = price_data.get('usd_market_cap', 'N/A')
        change_24h = price_data.get('usd_24h_change', 'N/A')
        
        change_symbol = "📈" if change_24h > 0 else "📉" if change_24h < 0 else "➡️"
        
        message = f"""
💰 HARGA {coin_name.upper()}

💵 USD: ${usd_price:,}
💴 IDR: Rp {idr_price:,.0f}

📊 Market Cap: ${market_cap:,.0f}
{change_symbol} 24h Change: {change_24h:.2f}%

⏰ Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        await update.message.reply_text(message)
    else:
        await update.message.reply_text(
            f"❌ Coin '{coin_name}' tidak ditemukan!\n\nCoba dengan nama yang berbeda."
        )

async def track_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start tracking a coin"""
    user_id = update.effective_user.id
    
    if not context.args:
        await update.message.reply_text(
            "❌ Format salah!\n\nGunakan: /track <nama_coin>\n\nContoh: /track bitcoin"
        )
        return
    
    coin_name = " ".join(context.args).lower()
    
    if user_id not in user_tracking:
        user_tracking[user_id] = []
    
    if coin_name in user_tracking[user_id]:
        await update.message.reply_text(
            f"⚠️ {coin_name.capitalize()} sudah ada di list tracking kamu!"
        )
        return
    
    user_tracking[user_id].append(coin_name)
    await update.message.reply_text(
        f"✅ Mulai tracking {coin_name.upper()}!\n\n📊 Kamu akan mendapat update harga setiap jam."
    )

async def mytracks_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user's tracking list"""
    user_id = update.effective_user.id
    
    if user_id not in user_tracking or len(user_tracking[user_id]) == 0:
        await update.message.reply_text(
            "📭 Kamu belum tracking coin apapun!\n\nGunakan /track <coin> untuk mulai tracking."
        )
        return
    
    tracking_list = user_tracking[user_id]
    message = "📊 DAFTAR TRACKING MU:\n\n"
    for i, coin in enumerate(tracking_list, 1):
        message += f"{i}. {coin.upper()}\n"
    
    message += "\n💡 Gunakan /untrack <coin> untuk berhenti tracking"
    await update.message.reply_text(message)

async def untrack_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop tracking a coin"""
    user_id = update.effective_user.id
    
    if not context.args:
        await update.message.reply_text(
            "❌ Format salah!\n\nGunakan: /untrack <nama_coin>\n\nContoh: /untrack bitcoin"
        )
        return
    
    coin_name = " ".join(context.args).lower()
    
    if user_id not in user_tracking or coin_name not in user_tracking[user_id]:
        await update.message.reply_text(
            f"❌ {coin_name.capitalize()} tidak ada di list tracking kamu!"
        )
        return
    
    user_tracking[user_id].remove(coin_name)
    await update.message.reply_text(
        f"✅ Berhenti tracking {coin_name.upper()}!"
    )

async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """AI analysis of a coin"""
    if not context.args:
        await update.message.reply_text(
            "❌ Format salah!\n\nGunakan: /analyze <nama_coin>\n\nContoh: /analyze bitcoin"
        )
        return
    
    coin_name = " ".join(context.args)
    price_data = await get_crypto_price(coin_name)
    
    if not price_data:
        await update.message.reply_text(
            f"❌ Coin '{coin_name}' tidak ditemukan!"
        )
        return
    
    change_24h = price_data.get('usd_24h_change', 0)
    
    # Simple AI Analysis
    if change_24h > 5:
        signal = "🟢 BULLISH"
        recommendation = "Pertimbangkan untuk BUY (dengan risk management)"
    elif change_24h > 0:
        signal = "🟡 NEUTRAL BULLISH"
        recommendation = "Monitor lebih lanjut sebelum keputusan"
    elif change_24h > -5:
        signal = "🟡 NEUTRAL BEARISH"
        recommendation = "Tunggu konfirmasi trend sebelum action"
    else:
        signal = "🔴 BEARISH"
        recommendation = "Hati-hati, pertimbangkan HOLD atau SELL"
    
    analysis = f"""
🤖 AI ANALYSIS - {coin_name.upper()}

📊 Signal: {signal}
💹 24h Change: {change_24h:.2f}%

💡 Rekomendasi:
{recommendation}

⚠️ DISCLAIMER:
Analisis ini untuk edukasi saja, bukan financial advice.
Selalu lakukan research sendiri sebelum trading!
    """
    
    await update.message.reply_text(analysis)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle general messages"""
    await update.message.reply_text(
        "❓ Perintah tidak dikenal!\n\nGunakan /help untuk melihat daftar perintah."
    )

def main():
    """Start the bot"""
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price_command))
    app.add_handler(CommandHandler("track", track_command))
    app.add_handler(CommandHandler("mytracks", mytracks_command))
    app.add_handler(CommandHandler("untrack", untrack_command))
    app.add_handler(CommandHandler("analyze", analyze_command))
    
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    # Start bot
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
