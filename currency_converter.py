from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self):
        # Initialisation du convertisseur
        self.rates = {}  # Dictionnaire pour stocker les taux de change
        self.update_rates()  # Mise a jour initiale des taux

    def update_rates(self):
        # Simulation d'une mise a jour des taux de change
        # Dans un cas reel, ces donnees viendraient d'une API en ligne
        self.rates = {
            "USD": 1.0,     # Le dollar americain est la devise de base (toujours 1)
            "EUR": 0.85,    # 1 USD = 0.85 EUR
            "GBP": 0.73,    # 1 USD = 0.73 GBP (livre sterling)
            "JPY": 110.25,  # 1 USD = 110.25 JPY (yen japonais)
            "CAD": 1.25     # 1 USD = 1.25 CAD (dollar canadien)
        }
        self.last_update = datetime.now()  # Enregistre le moment de la derniere mise a jour

    def convert(self, amount, from_currency, to_currency):
        # Verifie si une mise a jour des taux est necessaire
        if self.is_update_needed():
            self.update_rates()

        # Verifie si les devises demandees sont supportees
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Devise non supportee")

        # Conversion en deux etapes :
        # 1. Convertir le montant de la devise de depart en USD
        usd_amount = amount / self.rates[from_currency]
        # 2. Convertir le montant USD dans la devise cible
        converted_amount = usd_amount * self.rates[to_currency]

        # Arrondir le resultat a deux decimales (centimes)
        return round(converted_amount, 3)

    def is_update_needed(self):
        # Verifie si la derniere mise a jour date de plus d'une minute
        return (datetime.now() - self.last_update) > timedelta(minutes=1)

    def get_supported_currencies(self):
        # Renvoie la liste des devises supportees
        return list(self.rates.keys())

if __name__ == "__main__":
    converter = CurrencyConverter()  # Cree une instance du convertisseur

    amount = 100  # Montant a convertir
    from_currency = "EUR"  # Devise de depart
    to_currency = "JPY"    # Devise d'arrivee

    # Effectue la conversion
    result = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")

    # Affiche les devises supportees
    print("Devises supportees:", converter.get_supported_currencies())