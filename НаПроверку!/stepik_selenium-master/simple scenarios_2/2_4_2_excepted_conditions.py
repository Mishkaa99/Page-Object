import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
event = EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
WebDriverWait(browser, 12).until(event)
button = browser.find_element(By.CSS_SELECTOR, '#book')
button.click()
inputX = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = inputX.text

output = browser.find_element(By.CSS_SELECTOR, "#answer")
output.send_keys(str(calc(int(x))))

button = browser.find_element(By.XPATH, '//button[@type="submit"]')
button.click()
