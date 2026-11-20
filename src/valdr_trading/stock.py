
from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    price: float
    adr: float
    company_name: str | None = None
    sector: str | None = None
    average_daily_dollar_volume: float | None = None

    def __post_init__(self):
        if not self.symbol:
            raise ValueError("Stock symbol cannot be empty.")

        if self.price <= 0:
            raise ValueError("Stock price must be greater than zero.")

        if self.adr <= 0:
            raise ValueError("ADR must be greater than zero.")

        if (
        self.average_daily_dollar_volume is not None
        and self.average_daily_dollar_volume <= 0
        ):
         raise ValueError("Average daily dollar volume must be greater than zero.")
