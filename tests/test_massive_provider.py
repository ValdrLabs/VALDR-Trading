
from datetime import date, datetime, timezone
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from valdr_trading.config import Settings
from valdr_trading.data_engine.providers import massive_provider
from valdr_trading.data_engine.providers.massive_provider import MassiveProvider


def test_get_daily_data_converts_massive_aggregates(monkeypatch):
    # Simulate an API key without using a real one.
    monkeypatch.setattr(Settings, "MASSIVE_API_KEY", "test-api-key")

    # Create a simulated response from Massive.
    timestamp = int(
        datetime(2026, 11, 26, tzinfo=timezone.utc).timestamp() * 1000
    )

    fake_aggregate = SimpleNamespace(
        timestamp=timestamp,
        open=100.0,
        high=105.0,
        low=99.0,
        close=104.0,
        volume=1_000_000,
    )

    # Replace the real API client with a mock.
    fake_client = Mock()
    fake_client.list_aggs.return_value = [fake_aggregate]

    fake_rest_client = Mock(return_value=fake_client)
    monkeypatch.setattr(
        massive_provider,
        "RESTClient",
        fake_rest_client
    )

    provider = MassiveProvider()

    result = provider.get_daily_data(
        symbol="NVDA",
        start_date=date(2026, 11, 1),
        end_date=date(2026, 11, 30),
    )

    # Verify that the API response was converted correctly.
    assert len(result) == 1
    assert result[0].symbol == "NVDA"
    assert result[0].date == date(2026, 11, 26)
    assert result[0].open == 100.0
    assert result[0].high == 105.0
    assert result[0].low == 99.0
    assert result[0].close == 104.0
    assert result[0].volume == 1_000_000

    # Verify the client configuration.
    fake_rest_client.assert_called_once_with(
        api_key="test-api-key",
        pagination=False,
    )

    # Verify the exact request parameters.
    fake_client.list_aggs.assert_called_once_with(
        ticker="NVDA",
        multiplier=1,
        timespan="day",
        from_="2026-11-01",
        to="2026-11-30",
        adjusted="true",
        sort="asc",
        limit=50000,
    )

def test_missing_api_key_raises_value_error(monkeypatch):
    monkeypatch.setattr(Settings, "MASSIVE_API_KEY", None)

    with pytest.raises(
        ValueError,
        match="Massive API key is missing"
    ):
        MassiveProvider()