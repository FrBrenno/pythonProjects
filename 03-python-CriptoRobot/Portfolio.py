from Coin import Coin
from datetime import datetime

class Portfolio:

    def __init__(self, name:str):
        self.name = name
        self.coins = {}


    def add_coin(self, name:str, quantite:float, prix_transaction:float, date_transaction=datetime.today().strftime("\%Y-%m-%d-%H:%M:%S")):
        self.coins[name] = Coin(name, quantite, prix_transaction, date_transaction)



