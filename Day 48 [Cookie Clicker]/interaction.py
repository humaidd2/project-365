from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_path_driver = "C:/Users/Humaid Dikko/Documents/Dev/chromedriver"
driver = webdriver.Chrome()
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

search = driver.find_element(By.ID, value="searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
