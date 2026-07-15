# 🤖 Telegram Trading Bot dengan AI

## 📋 Deskripsi

Bot Telegram otomatis untuk tracking harga crypto dan analisis AI. Bot ini membantu kamu monitor market 24/7.

### ✨ Fitur Utama:
- ✅ **Cek Harga Real-time** - Harga Bitcoin, Ethereum, dan ribuan crypto lainnya
- ✅ **Tracking Otomatis** - Monitor multiple coins sekaligus
- ✅ **AI Analysis** - Sinyal trading otomatis (Bullish/Bearish)
- ✅ **Simple & User-friendly** - Mudah digunakan untuk pemula

---

## 🚀 Quick Start (Untuk Pemula)

### Step 1: Setup Environment

1. **Install Python 3.8+** dari [python.org](https://www.python.org/)

2. **Clone/Download Repository**
   ```bash
   cd telegram_tranding_bot
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Dapatkan Telegram Bot Token

1. Buka Telegram dan cari **@BotFather**
2. Kirim: `/newbot`
3. Ikuti instruksi:
   - Masukkan nama bot: `Trading Bot` (atau nama lain)
   - Masukkan username: `trading_bot_123` (harus unik)
4. **Salin token** yang diberikan

### Step 3: Setup Token

1. Buka file `.env` dengan text editor
2. Ganti `your_token_here` dengan token dari Step 2
   ```
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHijKlmnoPQRstUVwxyz...
   ```
3. **Simpan file**

### Step 4: Jalankan Bot

```bash
python main.py
```

Kalo berhasil, akan muncul: `🤖 Bot is running...`

---

## 📖 Cara Menggunakan

Di Telegram, gunakan command berikut:

### 1️⃣ Cek Harga
```
/price bitcoin
/price ethereum
/price solana
```

**Output:**
```
💰 HARGA BITCOIN

💵 USD: $45,000
💴 IDR: Rp 720,000,000

📊 Market Cap: $900 Billion
📈 24h Change: +2.50%

⏰ Update: 2024-01-15 10:30:45
```

### 2️⃣ Track Coin (Monitoring Otomatis)
```
/track bitcoin
/track ethereum
/mytracks          ← Lihat list tracking
/untrack bitcoin   ← Berhenti track
```

### 3️⃣ AI Analysis
```
/analyze bitcoin
```

**Output:**
```
🤖 AI ANALYSIS - BITCOIN

📊 Signal: 🟢 BULLISH
💹 24h Change: +2.50%

💡 Rekomendasi:
Pertimbangkan untuk BUY (dengan risk management)

⚠️ DISCLAIMER:
Analisis ini untuk edukasi saja, bukan financial advice.
```

### 4️⃣ Help
```
/help   ← Lihat semua command
```

---

## 🔧 Troubleshooting

### ❌ Error: "Token tidak valid"
- Pastikan token di `.env` benar
- Pastikan tidak ada spasi atau karakter ekstra

### ❌ Error: "Coin tidak ditemukan"
- Gunakan nama coin yang benar (lowercase)
- Contoh: `bitcoin`, bukan `Bitcoin` atau `BTC`
- Untuk daftar coin: https://api.coingecko.com/api/v3/coins/list

### ❌ Bot tidak merespons
- Cek apakah program masih running
- Cek koneksi internet
- Restart bot dengan Ctrl+C lalu `python main.py`

---

## 📝 File Structure

```
telegram_tranding_bot/
├── main.py              # File utama bot
├── requirements.txt     # Python dependencies
├── .env                 # Token & konfigurasi (RAHASIA!)
├── .gitignore          # File yang tidak di-upload
└── README.md           # Dokumentasi ini
```

---

## ⚙️ Configuration

### Edit `.env` untuk customize:

```env
# Token dari BotFather (WAJIB)
TELEGRAM_BOT_TOKEN=your_token_here
```

---

## 🔐 Security Tips

✅ **JANGAN:**
- ❌ Share file `.env` ke orang lain
- ❌ Push `.env` ke GitHub
- ❌ Share token di social media

✅ **LAKUKAN:**
- ✅ Simpan token di `.env` (sudah di `.gitignore`)
- ✅ Reset token jika terlalu lama tidak dipakai
- ✅ Gunakan `.env` untuk semua secret

---

## 📚 API Reference

### CoinGecko API (Free)
- Base URL: `https://api.coingecko.com/api/v3`
- Rate Limit: 50 calls/minute (unlimited untuk free tier)
- Dokumentasi: https://docs.coingecko.com

### Telegram Bot API
- Dokumentasi: https://core.telegram.org/bots/api
- Python Library: https://python-telegram-bot.readthedocs.io

---

## 🚀 Next Steps (Advanced)

1. **Add Database** - Simpan history tracking
2. **Price Alerts** - Notifikasi otomatis saat harga naik/turun
3. **Webhook** - Deploy ke server (Heroku, AWS, dll)
4. **Advanced AI** - Integrasikan ChatGPT untuk analysis
5. **Trading Signals** - Automated buy/sell signals

---

## 📞 Support

- 🐛 **Bug Report**: Buat issue di GitHub
- 💬 **Questions**: Hubungi developer
- 📖 **Documentation**: Baca README ini

---

## 📄 License

MIT License - Bebas digunakan untuk keperluan apapun

---

## 💡 Tips untuk Sukses

1. **Start Small** - Monitor 2-3 coin dulu
2. **Learn First** - Jangan langsung trade dengan uang besar
3. **Research** - Bot adalah tool, bukan trading guru
4. **Risk Management** - Selalu pakai stop loss
5. **Backup** - Backup file token kamu

---

**Happy Trading! 🚀📈**
