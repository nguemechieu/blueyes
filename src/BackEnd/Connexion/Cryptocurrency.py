from src.BackEnd.Connexion.Currency import Currency


class CryptoCurrency(Currency):

    def __init__(self, difficulty, name, _id, full_name, central_bank, country, fraction_digits):
        super().__init__(name, _id, full_name, central_bank, country, fraction_digits)
        self.difficulty = int(difficulty)
