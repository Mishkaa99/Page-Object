from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:

    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("test")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("test")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test")
    input4 = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
