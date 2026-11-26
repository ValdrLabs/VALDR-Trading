
from valdr_trading.stock import Stock
from valdr_trading.scanner import (
    filter_by_adr,
    filter_by_dollar_volume,
    screen_stocks
)


def test_filter_by_adr():
    stocks = [
        Stock("NVDA", 200.0, 5.8),
        Stock("AAPL", 250.0, 3.2),
        Stock("TSLA", 300.0, 7.5)
    ]

    result = filter_by_adr(stocks, minimum_adr=5.0)

    assert len(result) == 2
    assert result[0].symbol == "NVDA"
    assert result[1].symbol == "TSLA"


def test_no_stocks_meet_adr():
    stocks = [
        Stock("AAPL", 250.0, 3.2),
        Stock("MSFT", 400.0, 4.1)
    ]

    result = filter_by_adr(stocks, minimum_adr=5.0)

    assert len(result) == 0


def test_all_stocks_meet_adr():
    stocks = [
        Stock("NVDA", 200.0, 5.8),
        Stock("TSLA", 300.0, 7.5)
    ]

    result = filter_by_adr(stocks, minimum_adr=5.0)

    assert len(result) == 2


def test_stock_exactly_at_adr_threshold():
    stocks = [
        Stock("AAPL", 250.0, 5.0)
    ]

    result = filter_by_adr(stocks, minimum_adr=5.0)

    assert len(result) == 1
    assert result[0].symbol == "AAPL"


def test_empty_stock_list():
    stocks = []

    result = filter_by_adr(stocks, minimum_adr=5.0)

    assert result == []

def test_filter_by_dollar_volume():
    stocks = [
        Stock("NVDA", 200.0, 5.8, average_daily_dollar_volume=50_000_000),
        Stock("AAPL", 250.0, 3.2, average_daily_dollar_volume=80_000_000),
        Stock("TSLA", 300.0, 7.5, average_daily_dollar_volume=10_000_000)
    ]

    result = filter_by_dollar_volume(stocks, minimum_dollar_volume=20_000_000)

    assert len(result) == 2
    assert result[0].symbol == "NVDA"
    assert result[1].symbol == "AAPL"


def test_filter_by_dollar_volume_excludes_missing_data():
    stocks = [
        Stock("NVDA", 200.0, 5.8, average_daily_dollar_volume=50_000_000),
        Stock("AAPL", 250.0, 3.2)
    ]

    result = filter_by_dollar_volume(stocks, minimum_dollar_volume=20_000_000)

    assert len(result) == 1
    assert result[0].symbol == "NVDA"


def test_filter_by_dollar_volume_empty_list():
    result = filter_by_dollar_volume([], minimum_dollar_volume=20_000_000)

    assert result == []

def test_combined_screening():
    stocks = [
        Stock("NVDA", 200.0, 5.8, average_daily_dollar_volume=50_000_000),
        Stock("AAPL", 250.0, 3.2, average_daily_dollar_volume=80_000_000),
        Stock("TSLA", 300.0, 7.5, average_daily_dollar_volume=10_000_000),
        Stock("MSFT", 400.0, 5.0, average_daily_dollar_volume=30_000_000)
    ]

    result = screen_stocks(
        stocks,
        minimum_adr=5.0,
        minimum_dollar_volume=20_000_000
    )

    assert len(result) == 2
    assert result[0].symbol == "NVDA"
    assert result[1].symbol == "MSFT"