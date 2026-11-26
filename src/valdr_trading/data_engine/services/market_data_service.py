from datetime import date

from valdr_trading.data_engine.market_data import MarketData
from valdr_trading.data_engine.market_data_provider import MarketDataProvider


class MarketDataService:

    def __init__(self, provider: MarketDataProvider):
        self.provider = provider

    def get_daily_data(
        self,
        symbol: str,
        start_date: date,
        end_date: date
    ) -> list[MarketData]:

        return self.provider.get_daily_data(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date
        )