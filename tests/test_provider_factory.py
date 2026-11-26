
from unittest.mock import Mock

import pytest

from valdr_trading.config import Settings
from valdr_trading.data_engine import provider_factory
from valdr_trading.data_engine.provider_factory import (
    create_market_data_provider,
    register_provider,
)

def test_create_massive_provider(monkeypatch):
    fake_provider = Mock()

    monkeypatch.setattr(
        Settings,
        "DATA_PROVIDER",
        "massive"
    )

    monkeypatch.setitem(
        provider_factory._PROVIDER_REGISTRY,
        "massive",
        lambda: fake_provider
    )

    result = create_market_data_provider()

    assert result is fake_provider

def test_register_and_create_new_provider(monkeypatch):
    fake_provider = Mock()

    monkeypatch.setattr(
    provider_factory,
    "_PROVIDER_REGISTRY",
    dict(provider_factory._PROVIDER_REGISTRY),
)

    monkeypatch.setattr(
        Settings,
        "DATA_PROVIDER",
        "alpaca"
    )

    register_provider(
        "alpaca",
        lambda: fake_provider
    )

    result = create_market_data_provider()

    assert result is fake_provider

def test_unsupported_provider_raises_error(monkeypatch):
    monkeypatch.setattr(
        Settings,
        "DATA_PROVIDER",
        "unknown"
    )

    with pytest.raises(
        ValueError,
        match="Unsupported data provider"
    ):
        create_market_data_provider()