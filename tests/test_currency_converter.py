import pytest
from datetime import datetime, timedelta
import time
from currency_converter import CurrencyConverter

class TestCurrencyConverter:

    @pytest.fixture
    def converter(self):
        # Cette fixture cree une nouvelle instance de CurrencyConverter pour chaque test
        return CurrencyConverter()

    def test_initialization(self, converter):
        # Verifie que le convertisseur est correctement initialise
        assert converter.rates is not None  # Les taux de change ne doivent pas être vides
        assert isinstance(converter.last_update, datetime)  # La derniere mise a jour doit être un objet datetime

    def test_update_rates(self, converter):
        # Verifie que la methode update_rates() fonctionne correctement
        old_update = converter.last_update
        time.sleep(0.001)  # Attend un court instant pour s'assurer que le temps a change
        converter.update_rates()
        assert converter.last_update >= old_update  # La nouvelle mise a jour doit être plus recente
        assert converter.last_update != old_update  # La nouvelle mise a jour doit être differente de l'ancienne

    def test_convert_usd_to_eur(self, converter):
        # Teste la conversion de 100 USD en EUR
        result = converter.convert(100, "USD", "EUR")
        assert pytest.approx(result, 0.01) == 85  # Le resultat doit être proche de 85 EUR (avec une marge d'erreur de 0.01)

    def test_convert_eur_to_usd(self, converter):
        # Teste la conversion de 100 EUR en USD
        result = converter.convert(100, "EUR", "USD")
        assert pytest.approx(result, 0.01) == 117.65  # Le resultat doit être proche de 117.65 USD

    def test_convert_unsupported_currency(self, converter):
        # Verifie que la conversion avec une devise non supportee leve une exception
        with pytest.raises(ValueError):
            converter.convert(100, "USD", "XYZ")  # XYZ est une devise fictive non supportee

    def test_is_update_needed(self, converter):
        # Teste la logique de mise a jour des taux
        assert not converter.is_update_needed()  # Juste apres l'initialisation, pas de mise a jour necessaire
        converter.last_update = datetime.now() - timedelta(seconds=59)
        assert not converter.is_update_needed()  # Apres 59 secondes, toujours pas de mise a jour necessaire
        converter.last_update = datetime.now() - timedelta(seconds=61)
        assert converter.is_update_needed()  # Apres 61 secondes, une mise a jour est necessaire

    def test_get_supported_currencies(self, converter):
        # Verifie que la methode get_supported_currencies() renvoie les bonnes devises
        currencies = converter.get_supported_currencies()
        assert isinstance(currencies, list)  # Le resultat doit être une liste
        # Verifie que toutes les devises attendues sont presentes
        assert "USD" in currencies
        assert "EUR" in currencies
        assert "GBP" in currencies
        assert "JPY" in currencies
        assert "CAD" in currencies