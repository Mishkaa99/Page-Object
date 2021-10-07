from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:

    browser.get(link)
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)


    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(str(calc(x)))

    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_box.click()
    radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_button.click()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
