from loguru import logger
from selenium import webdriver


logger.debug("config Selenium")
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=r"./chromedriver")

logger.debug("initial request")
driver.get("http://www.example.com")
driver.get_screenshot_as_file("ss.png")
