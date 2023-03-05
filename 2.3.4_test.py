import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
# link = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome()
driver.get(link)
btn = driver.find_element(By.CLASS_NAME,'btn')
btn.click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
# confirm = driver.switch_to.alert
# confirm.accept()

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input = driver.find_element(By.ID, "answer")
input.send_keys(y)
btn_2 = driver.find_element(By.CLASS_NAME, "btn")
btn_2.click()

time.sleep(30)
driver.quit()