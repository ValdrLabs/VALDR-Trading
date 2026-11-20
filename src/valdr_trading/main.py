

from valdr_trading.stock import Stock
from valdr_trading.scanner import filter_by_adr
from valdr_trading.scanner import filter_by_dollar_volume


def main():
    stocks = [
    Stock("NVDA", 200.0, 5.8, "NVIDIA", "Technology", 50_000_000),
    Stock("AAPL", 250.0, 3.2, "Apple", "Technology", 80_000_000),
    Stock("TSLA", 300.0, 7.5, "Tesla", "Automotive", 35_000_000)
]

    print("VALDR Trading")
    print("--------------------")

    candidates = filter_by_adr(stocks, minimum_adr=5.0)
    candidates = filter_by_dollar_volume(
    candidates,
    minimum_dollar_volume=20_000_000
)

    print("\nStocks meeting ADR criteria:")
    for stock in candidates:
        print(stock.symbol, stock.adr)


if __name__ == "__main__":
    main()

