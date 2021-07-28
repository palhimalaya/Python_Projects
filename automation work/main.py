import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

CHROME_DRIVER_PATH = "c:\Developer\chromedriver.exe"
ZILLO_WEB = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
GOOGLE_DOCS = "https://docs.google.com/forms/d/e/1FAIpQLSccNfZP5IGMisWZxu7XjjOgwvDaoSVr0aAomn3yta-XjiAO9w/viewform?usp=sf_link"


class WorkAutomation:
    def __init__(self):
        self.address = []
        self.all_prices = []
        self.links = []

    def get_data(self):
        response = requests.get(
            ZILLO_WEB,
            headers=header)
        web_page = response.text
        soup = BeautifulSoup(web_page, 'html.parser')
        all_price_elements = soup.select(".list-card-heading")
        time.sleep(2)
        # all_price = soup.find_all(name="div", class_="list-card-price")
        for element in all_price_elements:
            # Get the prices. Single and multiple listings have different tag & class structures
            try:
                # Price with only one listing
                price = element.select(".list-card-price")[0].contents[0]
            except IndexError:
                print('Multiple listings for the card')
                # Price with multiple listings
                price = element.select(".list-card-details li")[0].contents[0]
            finally:
                self.all_prices.append(price)
        print(len(self.all_prices))
        all_address_elements = soup.select(".list-card-info address")
        self.address = [address.get_text().split(" | ")[-1] for address in all_address_elements]
        print(len(self.address))

        all_link_elements = soup.select(".list-card-top a")
        for link in all_link_elements:
            href = link["href"]
            if "http" not in href:
                self.links.append(f"https://www.zillow.com{href}")
            else:
                self.links.append(href)
        print(len(self.links))

    def add_data(self):
        driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        time.sleep(3)
        for n in range(len(self.links)):
            driver.get(
                GOOGLE_DOCS)
            time.sleep(4)
            address = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.click()
            address.send_keys(self.address[n])
            time.sleep(3)
            price = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.click()
            price.send_keys(self.all_prices[n])
            time.sleep(3)
            link = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.click()
            link.send_keys(self.links[n])
            time.sleep(3)
            submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
            submit_button.click()


wk = WorkAutomation()
wk.get_data()
wk.add_data()
