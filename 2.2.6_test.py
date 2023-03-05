import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
driver.get(link)

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input = driver.find_element(By.ID, "answer")
input.send_keys(y)
cbx = driver.find_element(By.ID, "robotCheckbox")
cbx.click()
button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
rdbtn = driver.find_element(By.ID, "robotsRule")
rdbtn.click()
button.click()

time.sleep(30)
driver.quit()