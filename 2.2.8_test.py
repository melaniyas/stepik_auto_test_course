import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
driver.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

input1 = driver.find_element(By.NAME, "firstname")
input2 = driver.find_element(By.NAME, "lastname")
input3 = driver.find_element(By.NAME, "email")
input4 = driver. find_element(By.ID, "file")
input1.send_keys('Ivan')
input2.send_keys('Ivanov')
input3.send_keys('ivan2000@mail.ru')
input4.send_keys(file_path)
btn = driver.find_element(By.CLASS_NAME, "btn").click()

time.sleep(30)
driver.quit()