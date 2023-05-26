from dataclasses import dataclass


@dataclass
class TransactionMetric:
    buys: int
    sells: int


@dataclass
class TransactionStats:
    transactions_5m: TransactionMetric
    transactions_1h: TransactionMetric
    transactions_6h: TransactionMetric
    transactions_24h: TransactionMetric

    @classmethod
    def from_json(cls, data):
        assert data["pair"] is not None, "Pair data is None"
        assert data["pair"]["txns"] is not None, "Transaction data is None"
        assert (
            data["pair"]["txns"]["m5"] is not None
        ), "5 Minute Transaction data is None"
        assert data["pair"]["txns"]["h1"] is not None, "1 Hour Transaction data is None"
        assert data["pair"]["txns"]["h6"] is not None, "6 HourTransaction data is None"
        assert (
            data["pair"]["txns"]["h24"] is not None
        ), "24 Hour Transaction data is None"

        cls.transactions_5m = TransactionMetric(**data["pair"]["txns"]["m5"])
        cls.transactions_1h = TransactionMetric(**data["pair"]["txns"]["h1"])
        cls.transactions_6h = TransactionMetric(**data["pair"]["txns"]["h6"])
        cls.transactions_24h = TransactionMetric(**data["pair"]["txns"]["h24"])

        return cls


@dataclass
class VolumeStats:
    volume_5m_usd: float
    volume_1h_usd: float
    volume_6h_usd: float
    volume_24h_usd: float

    @classmethod
    def from_json(cls, data):
        assert data["pair"] is not None, "Pair data is None"
        assert data["pair"]["volume"] is not None, "Volume data is None"
        assert data["pair"]["volume"]["m5"] is not None, "5 Minute Volume data is None"
        assert data["pair"]["volume"]["h1"] is not None, "1 Hour Volume data is None"
        assert data["pair"]["volume"]["h6"] is not None, "6 Hour Volume data is None"
        assert data["pair"]["volume"]["h24"] is not None, "24 Hour Volume data is None"

        cls.volume_5m_usd = data["pair"]["volume"]["m5"]
        cls.volume_1h_usd = data["pair"]["volume"]["h1"]
        cls.volume_6h_usd = data["pair"]["volume"]["h6"]
        cls.volume_24h_usd = data["pair"]["volume"]["h24"]

        return cls


@dataclass
class PriceChangeStats:
    in_5m: float
    in_1h: float
    in_6h: float
    in_24h: float

    @classmethod
    def from_json(cls, data):
        assert data["pair"] is not None, "Pair data is None"
        assert data["pair"]["priceChange"] is not None, "Price Change data is None"
        assert (
            data["pair"]["priceChange"]["m5"] is not None
        ), "5 Minute Price Change data is None"
        assert (
            data["pair"]["priceChange"]["h1"] is not None
        ), "1 Hour Price Change data is None"
        assert (
            data["pair"]["priceChange"]["h6"] is not None
        ), "6 Hour Price Change data is None"
        assert (
            data["pair"]["priceChange"]["h24"] is not None
        ), "24 Hour Price Change data is None"

        cls.in_5m = data["pair"]["priceChange"]["m5"]
        cls.in_1h = data["pair"]["priceChange"]["h1"]
        cls.in_6h = data["pair"]["priceChange"]["h6"]
        cls.in_24h = data["pair"]["priceChange"]["h24"]

        return cls


@dataclass
class Token:
    symbol: str
    pool_id: int
    price_usd: str

    transactions_stats: TransactionStats
    volume_stats: VolumeStats
    price_stats: PriceChangeStats
    liquidity_usd: float
    fully_diluted_valuation_usd: float
