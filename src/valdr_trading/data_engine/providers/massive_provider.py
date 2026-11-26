
from datetime import date, datetime, timezone

from massive import RESTClient

from valdr_trading.config import Settings
from valdr_trading.data_engine.market_data import MarketData


class MassiveProvider:

    def __init__(self):
        if not Settings.MASSIVE_API_KEY:
            raise ValueError(
                "Massive API key is missing. Check your .env file."
            )

        self.client = RESTClient(
            api_key=Settings.MASSIVE_API_KEY,
            pagination=False
        )

    def get_daily_data(
        self,
        symbol: str,
        start_date: date,
        end_date: date
    ) -> list[MarketData]:

        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        aggregates = self.client.list_aggs(
            ticker=symbol,
            multiplier=1,
            timespan="day",
            from_=start_date.isoformat(),
            to=end_date.isoformat(),
            adjusted="true",
            sort="asc",
            limit=50000
        )

        market_data = []

        for aggregate in aggregates:
            trading_date = datetime.fromtimestamp(
                aggregate.timestamp / 1000,
                tz=timezone.utc
            ).date()

            market_data.append(
                MarketData(
                    symbol=symbol,
                    date=trading_date,
                    open=aggregate.open,
                    high=aggregate.high,
                    low=aggregate.low,
                    close=aggregate.close,
                    volume=aggregate.volume
                )
            )

        return market_data
