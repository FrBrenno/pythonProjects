from Portfolio import Portfolio
from datetime import datetime

class User:

    def __init__(self, name:str):
        self.name = name
        self.portfolio =[]

    def add_portfolio(self, name:str):
        self.portfolio.append(Portfolio(name))

    



