from datetime import date
from typing import Protocol

from valdr_trading.data_engine.market_data import MarketData


class MarketDataProvider(Protocol):

    def get_daily_data(
        self,
        symbol: str,
        start_date: date,
        end_date: date
    ) -> list[MarketData]:
        ...