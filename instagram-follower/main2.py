from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "c:\Developer\chromedriver.exe"
SIMILAR_ACCOUNT = "codes.learning"
USERNAME = "4testingcode"
PASSWORD = "testingcode4@()"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.click()
        email.send_keys(USERNAME)
        time.sleep(2)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.click()
        password.send_keys(PASSWORD)
        time.sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login.click()
        time.sleep(3)
        self.driver.get("https://www.instagram.com/accounts/onetap/?next=%2F")
        info_not = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        info_not.click()
        time.sleep(3)
        notification = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        notification.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(3)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
