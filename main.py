import os
import ccxt

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
})

def check_balance():
    try:
        balance = exchange.fetch_balance()
        print("✅ API bağlantısı başarılı! Cüzdan bakiyeleri:")
        for asset, amount in balance['total'].items():
            if amount > 0:
                print(f"→ {asset}: {amount}")
    except Exception as e:
        print("❌ HATA:", e)

if __name__ == "__main__":
    check_balance()
