
from valdr_trading.stock import Stock


def filter_by_adr(stocks: list[Stock], minimum_adr: float) -> list[Stock]:
    return [
        stock
        for stock in stocks
        if stock.adr >= minimum_adr
    ]
def filter_by_dollar_volume(
    stocks: list[Stock],
    minimum_dollar_volume: float
) -> list[Stock]:
    return [
        stock
        for stock in stocks
        if stock.average_daily_dollar_volume is not None
        and stock.average_daily_dollar_volume >= minimum_dollar_volume
    ]
def screen_stocks(
    stocks: list[Stock],
    minimum_adr: float,
    minimum_dollar_volume: float
) -> list[Stock]:

    adr_candidates = filter_by_adr(stocks, minimum_adr)

    return filter_by_dollar_volume(
        adr_candidates,
        minimum_dollar_volume
    )