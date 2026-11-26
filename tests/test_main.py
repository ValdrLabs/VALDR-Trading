
from unittest.mock import Mock

import valdr_trading.main as main_module
from valdr_trading.data_engine.services.market_data_service import (
    MarketDataService,
)


def test_create_market_data_service_uses_provider_factory(monkeypatch):
    fake_provider = Mock()

    monkeypatch.setattr(
        main_module,
        "create_market_data_provider",
        lambda: fake_provider,
    )

    service = main_module.create_market_data_service()

    assert isinstance(service, MarketDataService)
    assert service.provider is fake_provider
