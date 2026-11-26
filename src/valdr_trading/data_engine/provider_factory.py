
from typing import Callable

from valdr_trading.config import Settings
from valdr_trading.data_engine.market_data_provider import MarketDataProvider
from valdr_trading.data_engine.providers.massive_provider import MassiveProvider


ProviderCreator = Callable[[], MarketDataProvider]


_PROVIDER_REGISTRY: dict[str, ProviderCreator] = {
    "massive": MassiveProvider,
}


def register_provider(name: str, creator: ProviderCreator) -> None:
    provider_name = name.strip().lower()

    if not provider_name:
        raise ValueError("Provider name cannot be empty.")

    if provider_name in _PROVIDER_REGISTRY:
        raise ValueError(
            f"Provider '{provider_name}' is already registered."
        )

    _PROVIDER_REGISTRY[provider_name] = creator


def create_market_data_provider() -> MarketDataProvider:
    provider_name = (Settings.DATA_PROVIDER or "").strip().lower()

    if not provider_name:
        raise ValueError("DATA_PROVIDER is not configured.")

    creator = _PROVIDER_REGISTRY.get(provider_name)

    if creator is None:
        raise ValueError(
            f"Unsupported data provider: '{provider_name}'."
        )

    return creator()
