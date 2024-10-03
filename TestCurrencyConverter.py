# -*- coding: utf-8 -*-

import unittest
from datetime import datetime, timedelta
import time
from currency_converter import CurrencyConverter
#from IFT3913 import currency_converter
class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter()

    def test_initialization(self):
        self.assertIsNotNone(self.converter.rates)
        self.assertIsInstance(self.converter.last_update, datetime)

    def test_update_rates(self):
        old_update = self.converter.last_update
        time.sleep(0.001)
        self.converter.update_rates()
        self.assertGreaterEqual(self.converter.last_update, old_update)
        self.assertNotEqual(self.converter.last_update, old_update)

    def test_convert_usd_to_eur(self):
        result = self.converter.convert(100, "USD", "EUR")
        self.assertAlmostEqual(result, 85, delta=0.01)

    def test_convert_eur_to_usd(self):
        result = self.converter.convert(100, "EUR", "USD")
        self.assertAlmostEqual(result, 117.65, delta=0.01)

    def test_convert_unsupported_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert(100, "USD", "XYZ")

    def test_is_update_needed(self):
        self.assertFalse(self.converter.is_update_needed())
        self.converter.last_update = datetime.now() - timedelta(seconds=59)
        self.assertFalse(self.converter.is_update_needed())
        self.converter.last_update = datetime.now() - timedelta(seconds=61)
        self.assertTrue(self.converter.is_update_needed())

    def test_get_supported_currencies(self):
        currencies = self.converter.get_supported_currencies()
        self.assertIsInstance(currencies, list)
        self.assertIn("USD", currencies)
        self.assertIn("EUR", currencies)
        self.assertIn("GBP", currencies)
        self.assertIn("JPY", currencies)
        self.assertIn("CAD", currencies)

if __name__ == '__main__':
    unittest.main()