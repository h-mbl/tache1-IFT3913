from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self):
        # Initialisation du convertisseur
        self.rates = {}  # Dictionnaire pour stocker les taux de change
        self.update_rates()  # Mise à jour initiale des taux

    def update_rates(self):
        # Simulation d'une mise à jour des taux de change
        # Dans un cas réel, ces données viendraient d'une API en ligne
        self.rates = {
            "USD": 1.0,     # Le dollar américain est la devise de base (toujours 1)
            "EUR": 0.85,    # 1 USD = 0.85 EUR
            "GBP": 0.73,    # 1 USD = 0.73 GBP (livre sterling)
            "JPY": 110.25,  # 1 USD = 110.25 JPY (yen japonais)
            "CAD": 1.25     # 1 USD = 1.25 CAD (dollar canadien)
        }
        self.last_update = datetime.now()  # Enregistre le moment de la dernière mise à jour

    def convert(self, amount, from_currency, to_currency):
        # Vérifie si une mise à jour des taux est nécessaire
        if self.is_update_needed():
            self.update_rates()

        # Vérifie si les devises demandées sont supportées
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Devise non supportee")

        # Conversion en deux étapes :
        # 1. Convertir le montant de la devise de départ en USD
        usd_amount = amount / self.rates[from_currency]
        # 2. Convertir le montant USD dans la devise cible
        converted_amount = usd_amount * self.rates[to_currency]

        # Arrondir le résultat à deux décimales (centimes)
        return round(converted_amount, 2)

    def is_update_needed(self):
        # Vérifie si la dernière mise à jour date de plus d'une minute
        return (datetime.now() - self.last_update) >= timedelta(minutes=1)

    def get_supported_currencies(self):
        # Renvoie la liste des devises supportées
        return list(self.rates.keys())

if __name__ == "__main__":
    converter = CurrencyConverter()  # Crée une instance du convertisseur

    amount = 100  # Montant à convertir
    from_currency = "USD"  # Devise de départ
    to_currency = "EUR"    # Devise d'arrivée

    # Effectue la conversion
    result = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")

    # Affiche les devises supportées
    print("Devises supportees:", converter.get_supported_currencies())