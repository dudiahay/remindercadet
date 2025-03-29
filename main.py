import requests
import schedule
import time

TOKEN = "7891757524:AAEfhDFqlwbuB4Uj414x9bWTjsnsTqfyBWA"  # Ganti dengan token bot Anda
CHAT_ID = "-1002641914103"  # Ganti dengan chat ID supergroup Anda

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "MarkdownV2"
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Pesan berhasil dikirim!")
    else:
        print("Gagal mengirim pesan:", response.text)

def send_absen_pagi():
    message = """🔔 *PESAN PENGINGAT* 🔔

Jangan lupa untuk *absen pagi* rekan\\-rekan taruna  
Waktu : *06\\.00 \\- 10\\.00 WIB*  
Link absensi : [Klik di sini](https://157.66.34.25:5173/absen)

Terima kasih rekan\\-rekan taruna 🫡  
Enjoy your holiday ✨
"""
    send_message(message)

def send_absen_malam():
    message = """🔔 *PESAN PENGINGAT* 🔔

Jangan lupa untuk *absen malam* rekan\\-rekan taruna  
Waktu : *18\\.00 \\- 22\\.00 WIB*  
Link absensi : [Klik di sini](https://157.66.34.25:5173/absen)

Terima kasih rekan\\-rekan taruna 🫡  
Enjoy your holiday ✨
"""
    send_message(message)

# Jadwal pengiriman pesan (Waktu GMT+7 Jakarta)
schedule.every().day.at("06:00").do(send_absen_pagi)  # Absen pagi
schedule.every().day.at("18:00").do(send_absen_malam)  # Absen malam

print("Bot Telegram berjalan...")

# Loop agar script berjalan terus
while True:
    schedule.run_pending()
    time.sleep(60)  # Cek setiap 60 detik
