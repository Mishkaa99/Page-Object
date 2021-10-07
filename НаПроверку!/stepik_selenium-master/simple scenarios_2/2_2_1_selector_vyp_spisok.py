from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
try:

    browser.get(link)
    num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    summ = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
