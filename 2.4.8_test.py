import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

driver = webdriver.Chrome()
driver.get(link)

button = driver.find_element(By.ID, "book")
price = WebDriverWait(driver, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))

button.click()

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input = driver.find_element(By.ID, "answer")
input.send_keys(y)
btn = driver.find_element(By.ID, "solve")
btn.click()

time.sleep(20)
driver.quit()