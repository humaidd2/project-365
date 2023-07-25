from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_path_driver = "C:/Users/Humaid Dikko/Documents/Dev/chromedriver"
driver = webdriver.Chrome()
driver.get(url="https://www.python.org/")

e = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]')
events = e.find_elements(By.CSS_SELECTOR, value="li a")
date = e.find_elements(By.CSS_SELECTOR, value="time")

output = {}

for i in range(len(events) - 1):
    output[i] = [date[i].text, events[i].text]

print(output)

driver.quit()
