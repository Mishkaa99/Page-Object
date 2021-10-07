from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
try:

    browser.get(link)
    input1 = browser.find_element_by_tag_name("[placeholder=\"Input your first name\"]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name("[placeholder=\"Input your last name\"]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_tag_name("[placeholder=\"Input your email\"]")
    input3.send_keys("test@test.su")
    input4 = browser.find_element_by_tag_name("[placeholder=\"Input your phone:\"]")
    input4.send_keys("+7928")
    input5 = browser.find_element_by_tag_name("[placeholder=\"Input your address:\"]")
    input5.send_keys("aaaaaa")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
