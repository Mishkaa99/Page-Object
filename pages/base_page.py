from selenium.common.exceptions import NoSuchElementException # (имя исключения)

# Можно сделать это по-разному (с настройкой явных или неявных ожиданий). 
# Сейчас неявным ожиданием:
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # (is_element_present) в него будем передавать два аргумента: как искать (css, id, xpath и тд)
    #  и собственно что искать (строку-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self): 
        self.browser.get(self.url)






# class BasePage():
#     def __init__(self, browser, url):
#         self.browser = browser
#         self.url = url

#     def open(self): 
#         self.browser.get(self.url)