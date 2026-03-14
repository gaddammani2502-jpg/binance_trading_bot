# Binance Futures Trading Bot (Python)

This project is a simple CLI-based trading bot built in Python that interacts with the Binance Futures Testnet API.

## Features
- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Command-line interface input
- Error handling and order response display

## Requirements
- Python 3.x
- python-binance library

Install dependencies:
pip install python-binance

## Example Usage

Market Order:
python bot.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

Limit Order:
python bot.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 60000

## Output
The bot prints:
- Order ID
- Order status
- Executed quantity
- API response

## Note
This bot works with Binance Futures **Testnet**, not the real trading environment.
