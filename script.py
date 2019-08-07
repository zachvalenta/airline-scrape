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
origin.send_keys('JFK')
time.sleep(3)
driver.get_screenshot_as_file("jfk-find.png")

logger.debug("click origin")
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".tt-dataset-airports"))
    ).click()
driver.get_screenshot_as_file("jfk-choose.png")

logger.debug("input destination")
destination.send_keys('YXU')
time.sleep(3)
driver.get_screenshot_as_file("yxu-find.png")

logger.debug("click destination")
WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#destination-picker .tt-dataset-airports"))
    ).click()
driver.get_screenshot_as_file("yxu-choose.png")

logger.debug("done")
