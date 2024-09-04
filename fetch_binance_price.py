import requests
import time

def get_binance_api_spot_price():
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

def log_price(price, filepath='binance_spot_price_log.txt'):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(filepath, 'a') as file:
        file.write(f"{timestamp}: {price}\n")

if __name__ == "__main__":
    while True:
        try:
            binance_spot_price = get_binance_api_spot_price()
            log_price(binance_spot_price)
            print(f"Logged Binance API Spot Price: {binance_spot_price}")
        except Exception as e:
            print(f"Error fetching or logging price: {e}")
        
        # Sleep for 10 seconds before fetching the price again
        time.sleep(10)
