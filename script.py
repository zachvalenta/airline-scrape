import time

from loguru import logger
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


logger.debug("config Selenium")
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1800x800')
driver = webdriver.Chrome(chrome_options=options, executable_path=r"./chromedriver")
driver.implicitly_wait(10)

logger.debug("waiting for page to load")
driver.get("https://www.westjet.com")

logger.debug("locating inputs")
origin = driver.find_element_by_css_selector('#origin-search')
destination = driver.find_element_by_css_selector('#destination-search')

logger.debug("input origin")
driver.find_element_by_css_selector("#book-flight-form > div.col-xs-12.col-smv-6.col-lgv-12.wrapper.airport.origin > button > i").click()
origin.send_keys('JFK')
time.sleep(3)
driver.get_screenshot_as_file("1.png")

logger.debug("click origin")
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".tt-dataset-airports"))
    ).click()
driver.get_screenshot_as_file("2.png")

logger.debug("input destination")
driver.find_element_by_css_selector("#book-flight-form > div.col-xs-12.col-smv-6.col-lgv-12.wrapper.airport.destination > button > i").click()
destination.send_keys('YYZ')
time.sleep(3)
driver.get_screenshot_as_file("3.png")

logger.debug("click destination")
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#destination-picker .tt-dataset-airports"))
    ).click()
driver.get_screenshot_as_file("4.png")

logger.debug("input date")
driver.find_element_by_css_selector('#depart').click()
time.sleep(3)
driver.get_screenshot_as_file("5.png")

logger.debug("click date")
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.dw-cal-slide-a [data-full='2019-7-14'"))
    ).click()
driver.get_screenshot_as_file("6.png")

logger.debug("get flights")
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#desktop-submit input[value='Get flights']"))
    ).click()
time.sleep(5)
driver.get_screenshot_as_file("7.png")

logger.debug("done")
