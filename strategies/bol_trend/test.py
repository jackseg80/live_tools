#SEG, V2.1
import sys
sys.path.append("./live_tools")
import ccxt
import ta
import pandas as pd
from utilities.perp_bitget import PerpBitget
from utilities.custom_indicators import get_n_columns
from datetime import datetime
import time
import json

f = open(
    "./live_tools/secret.json",
)
secret = json.load(f)
f.close()

account_to_select = "bitget_exemple"
production = False

pair = "ETH/USDT:USDT"
timeframe = "1h"
leverage = 1.3

bitget = PerpBitget(
    apiKey=secret[account_to_select]["apiKey"],
    secret=secret[account_to_select]["secret"],
    password=secret[account_to_select]["password"],
)

# Get data
df = bitget.get_more_last_historical_async(pair, timeframe, 1000)

print(df)

usd_balance = float(bitget.get_usdt_equity())
usd_balance = round(usd_balance,2)
print("USD balance :", usd_balance, "$")

positions_data = bitget.get_open_position()
position = [
    {"side": d["side"], "size": d["contractSize"], "market_price":d["info"]["marketPrice"], "usd_size": float(d["contractSize"]) * float(d["info"]["marketPrice"]), "open_price": d["entryPrice"]}
    for d in positions_data if d["symbol"] == pair]


