import requests
import os
import time

# Mengambil token & chat ID dari Railway Environment Variables
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# URL API Telegram
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Fungsi untuk mengirim pesan
def send_message():
    MESSAGE = "🚀 Bot Telegram Railway Aktif!"
    data = {"chat_id": CHAT_ID, "text": MESSAGE}
    response = requests.post(URL, data=data)

    if response.status_code == 200:
        print("✅ Pesan berhasil dikirim!")
    else:
        print("❌ Gagal mengirim pesan:", response.text)

# Mengirim pesan setiap 1 menit (jika ingin terus berjalan)
while True:
    send_message()
    time.sleep(60)  # Tunggu 60 detik sebelum mengirim ulang
