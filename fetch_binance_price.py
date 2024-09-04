import requests

def get_binance_api_spot_price():
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

def save_price_to_file(price, filepath='binance_spot_price.txt'):
    with open(filepath, 'w') as file:
        file.write(str(price))

if __name__ == "__main__":
    binance_spot_price = get_binance_api_spot_price()
    save_price_to_file(binance_spot_price)
    print(f"Binance API Spot Price: {binance_spot_price} saved to binance_spot_price.txt")
