import pytest
from datetime import date

from valdr_trading.data_engine.market_data import MarketData


def test_create_market_data():
    market_data = MarketData(
        symbol="NVDA",
        date=date(2026, 11, 26),
        open=180.0,
        high=190.0,
        low=175.0,
        close=185.0,
        volume=50_000_000
    )

    assert market_data.symbol == "NVDA"
    assert market_data.close == 185.0


def test_market_data_rejects_invalid_prices():
    with pytest.raises(ValueError):
        MarketData(
            symbol="NVDA",
            date=date(2026, 11, 26),
            open=180.0,
            high=170.0,
            low=175.0,
            close=185.0,
            volume=50_000_000
        )

from valdr_trading.data_engine.services.market_data_service import MarketDataService


class MockMarketDataProvider:

    def get_daily_data(self, symbol, start_date, end_date):
        return [
            MarketData(
                symbol=symbol,
                date=date(2026, 11, 26),
                open=180.0,
                high=190.0,
                low=175.0,
                close=185.0,
                volume=50_000_000
            )
        ]


def test_market_data_service():
    provider = MockMarketDataProvider()
    service = MarketDataService(provider)

    result = service.get_daily_data(
        symbol="NVDA",
        start_date=date(2026, 11, 1),
        end_date=date(2026, 11, 26)
    )

    assert len(result) == 1
    assert result[0].symbol == "NVDA"
    assert result[0].close == 185.0