from dataclasses import dataclass
from datetime import date


@dataclass
class MarketData:
    symbol: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int

    def __post_init__(self):
        if not self.symbol:
            raise ValueError("Market data symbol cannot be empty.")

        if min(self.open, self.high, self.low, self.close) <= 0:
            raise ValueError("Prices must be greater than zero.")

        if self.high < self.low:
            raise ValueError("High cannot be lower than low.")

        if self.volume < 0:
            raise ValueError("Volume cannot be negative.")

        if self.high < max(self.open, self.close):
            raise ValueError("High cannot be lower than open or close.")

        if self.low > min(self.open, self.close):
            raise ValueError("Low cannot be higher than open or close.")