import argparse
from binance.client import Client

API_KEY = "API key use here"
API_SECRET = "Secret key use here"

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    if args.type == "MARKET":
        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type="MARKET",
            quantity=args.qty
        )

    elif args.type == "LIMIT":
        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type="LIMIT",
            quantity=args.qty,
            price=args.price,
            timeInForce="GTC"
        )

    print("Order placed successfully")
    print(order)

except Exception as e:
    print("Order failed")
    print(str(e))