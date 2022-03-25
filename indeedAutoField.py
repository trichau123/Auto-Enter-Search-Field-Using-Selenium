from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#user_name = "apply"
#password = "New.jer.sey.123"
PATH = "/Users/trichau/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.indeed.com/")


what = driver.find_element_by_id("text-input-what")

#element = driver.find_element_by_id("search-site")
#searchw.send_keys("Software Engineering Entry Level OPT")
what.send_keys("Software Engineer Entry Level")
#element = driver.find_element_by_id("pass")
#element.send_keys(password)

what.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()



