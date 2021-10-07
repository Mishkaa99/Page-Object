import unittest
from selenium import webdriver
import time


right_text = "Congratulations! You have successfully registered!"


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector("input[class*='first'][placeholder*='name']").send_keys('dakgh')
        browser.find_element_by_css_selector("input[class*='second'][placeholder*='last']").send_keys('fdcadc')
        browser.find_element_by_css_selector("input[class*='third'][placeholder*='email']").send_keys('dav@klgm.io')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt

        self.assertEqual(welcome_text_elt.text, right_text, "Should be absolute value of a number")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration.html")

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector("input[class*='first'][placeholder*='name']").send_keys('dakgh')
        browser.find_element_by_css_selector("input[class*='second'][placeholder*='last']").send_keys('fdcadc')
        browser.find_element_by_css_selector("input[class*='third'][placeholder*='email']").send_keys('dav@klgm.io')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt

        self.assertEqual(welcome_text_elt.text, right_text, "Should be absolute value of a number")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
