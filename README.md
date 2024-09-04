# Binance API vs TradingView Price Comparison

This project monitors the price difference between Binance's API spot price for BTCUSDT and the TradingView BTCUSD price for Binance. It flags significant deviations and allows you to visualize these differences on TradingView.

## Project Structure

- `fetch_binance_price.py`: Python script to fetch Binance API spot price.
- `tradingview_script.pine`: TradingView Pine Script to compare prices and flag deviations.
- `binance_spot_price.txt`: Output file where the Binance API spot price is stored.
- `README.md`: This documentation.

## Setup Instructions

### 1. Run the Python Script

1. Ensure you have Python installed.
2. Run `fetch_binance_price.py` to fetch the current Binance API spot price.
3. The price will be saved to `binance_spot_price.txt`.

### 2. Use the TradingView Pine Script

1. Open TradingView.
2. Create a new Pine Script and paste the contents of `tradingview_script.pine`.
3. Manually input the Binance API spot price or automate the input using a webhook.

### 3. Monitor and Analyze

- The Pine Script will plot the deviation between the Binance API spot price and the TradingView BTCUSD price.
- Any significant deviations will be flagged on the chart.

## Next Steps

- **Automation**: Integrate a webhook to automate the input of the Binance API spot price into TradingView.
- **Alerts**: Set up alerts based on deviations for trading strategies.
