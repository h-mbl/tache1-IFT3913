# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
class CurrencyConverter:
    def __init__(self):
        self.rates = {}
        self.update_rates()

    def update_rates(self):
        # Simulation de l'API
        self.rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.73,
            "JPY": 110.25,
            "CAD": 1.25
        }
        self.last_update = datetime.now()

    def convert(self, amount, from_currency, to_currency):
        if self.is_update_needed():
            self.update_rates()

        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Devise non supportee")

        # Convertir d'abord en USD, puis dans la devise cible
        usd_amount = amount / self.rates[from_currency]
        converted_amount = usd_amount * self.rates[to_currency]

        return round(converted_amount, 2)

    def is_update_needed(self):
        return (datetime.now() - self.last_update) >= timedelta(minutes=1)

    def get_supported_currencies(self):
        return list(self.rates.keys())


# Exemple d'utilisation
if __name__ == "__main__":
    converter = CurrencyConverter()

    amount = 100
    from_currency = "USD"
    to_currency = "EUR"

    result = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")

    print("Devises supportees:", converter.get_supported_currencies())