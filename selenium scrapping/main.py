from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_driver_path = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")
event_time = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")
event = {}
for n in range(len(event_time)):
    event[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text
    }

print(event)
driver.quit()


