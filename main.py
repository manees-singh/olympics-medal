import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://google.com")

time.sleep(10)

driver.quit()


# import selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time

# service= Service(executable_path="chromedriver-linux64/chromedriver")

# driver=webdriver.Chrome(service=service)

# driver.get("https://google.com")

# time.sleep(10)

# driver.quit()