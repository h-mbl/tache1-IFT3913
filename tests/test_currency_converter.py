import pytest
from datetime import datetime, timedelta
import time
from currency_converter import CurrencyConverter

class TestCurrencyConverter:

    @pytest.fixture
    def converter(self):
        return CurrencyConverter()

    def test_initialization(self, converter):
        assert converter.rates is not None
        assert isinstance(converter.last_update, datetime)

    def test_update_rates(self, converter):
        old_update = converter.last_update
        time.sleep(0.001)
        converter.update_rates()
        assert converter.last_update >= old_update
        assert converter.last_update != old_update

    def test_convert_usd_to_eur(self, converter):
        result = converter.convert(100, "USD", "EUR")
        assert pytest.approx(result, 0.01) == 85

    def test_convert_eur_to_usd(self, converter):
        result = converter.convert(100, "EUR", "USD")
        assert pytest.approx(result, 0.01) == 117.65

    def test_convert_unsupported_currency(self, converter):
        with pytest.raises(ValueError):
            converter.convert(100, "USD", "XYZ")

    def test_is_update_needed(self, converter):
        assert not converter.is_update_needed()
        converter.last_update = datetime.now() - timedelta(seconds=59)
        assert not converter.is_update_needed()
        converter.last_update = datetime.now() - timedelta(seconds=61)
        assert converter.is_update_needed()

    def test_get_supported_currencies(self, converter):
        currencies = converter.get_supported_currencies()
        assert isinstance(currencies, list)
        assert "USD" in currencies
        assert "EUR" in currencies
        assert "GBP" in currencies
        assert "JPY" in currencies
        assert "CAD" in currencies