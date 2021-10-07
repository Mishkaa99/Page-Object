from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
try:

    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()


    inputX = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = inputX.text

    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(str(calc(int(x))))

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
