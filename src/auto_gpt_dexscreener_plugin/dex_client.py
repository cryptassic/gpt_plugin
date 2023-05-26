import json
from dataclasses import dataclass
from datetime import datetime

import requests

from .models import PriceChangeStats, Token, TransactionStats, VolumeStats

URL = "https://api.dexscreener.com/latest/dex/pairs/osmosis/"


@dataclass
class QueryResult:
    symbol: str
    pool_id: int


def to_file(filepath: str, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def get(index: int):
    response = requests.get(URL + str(index))

    if response.status_code == 200:
        print(f"{datetime.now()} - GET {URL + str(index)} {response.status_code}")
        data = response.json()
        return data

    return None


def get_id(pool_id: int) -> QueryResult:
    data = get(pool_id)

    if data["pair"] is not None:
        symbol = data["pair"]["baseToken"]["symbol"]
        pool_id = int(data["pair"]["pairAddress"])

        return QueryResult(symbol, pool_id)

    return None


def get_token(pool_id: int) -> Token:
    data = get(pool_id)

    if data["pair"] is not None:
        symbol = data["pair"]["baseToken"]["symbol"]
        pool_id = int(data["pair"]["pairAddress"])
        price_usd = data["pair"]["priceUsd"]

        transaction_stats = TransactionStats.from_json(data)
        volume_stats = VolumeStats.from_json(data)
        price_stats = PriceChangeStats.from_json(data)
        liquidity_usd = data["pair"]["liquidity"]["usd"]
        fdv = data["pair"]["fdv"]

        return Token(
            symbol,
            pool_id,
            price_usd,
            transaction_stats,
            volume_stats,
            price_stats,
            liquidity_usd,
            fdv,
        )


if __name__ == "__main__":
    token = get_token(960)
    print()
