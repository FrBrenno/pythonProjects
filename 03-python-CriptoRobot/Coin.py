from Webscrapper import Webscrapper
from datetime import datetime

class Coin:

    def __init__(self, name:str, quantite:float, prix_transaction:float, date_transaction):
        self.name = name
        self.price_now = Webscrapper().get_price(self.name)
        self.last_price_update = date_transaction
        self.quantity = quantite
        self.price_transaction = prix_transaction
        self.date_transaction = date_transaction


    def price_update(self):
        self.price_now = Webscrapper().get_price(self.name)
        self.last_price_update = datetime.today().strftime("\%Y-%m-%d-%H:%M:%S")

  

