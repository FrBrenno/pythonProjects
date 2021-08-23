from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep 


class Webscrapper:
    """Class responsible to get data from the internet.
    """
    
    def __init__(self):
        self.brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        self.config_path = "C:\\Users\\brenn\\Documents\\GitHub\\pythonProjects\\03-python-CriptoRobot\\webscrapper_config.txt"
        self.option = webdriver.ChromeOptions()
        self.option.binary_location = self.brave_path
        self.option.headless = True
        self.driver = webdriver.Chrome(options=self.option)
        
    
    def enter_coinmarket(self):
        """Enter in the site which the url is in the webscrapper_config.txt file
        """
        url = ""
        with open(self.config_path) as config:
                url = config.read()      
        self.driver.get(url)

    def get_price(self, name_coin):
        """Search in coinmarket the price of the selected coin.

        Args:
            name_coin (string): Name of the coin which we want to know the price
        """
        self.enter_coinmarket()
        try:
            sleep(2)
            search = self.driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[1]/div[2]/div/nav/div/div[2]").click()
        except NoSuchElementException:
            sleep(5)
            self.search_coin_price(name_coin)
        finally:
            try:
                sleep(2)
                search_bar = self.driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/input")
                search_bar.send_keys(name_coin)
                search_bar.send_keys(Keys.RETURN)
            except NoSuchElementException:
                sleep(5)
                self.search_coin_price(name_coin)
            finally:
                try:
                    sleep(2)
                    price = self.driver.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div").text
                except NoSuchElementException:
                    sleep(5)
                    self.search_coin_price(name_coin)
                finally:
                    return price
        
        
    





    