import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_cart_button(browser):
	browser.get(link)
	time.sleep(5)
	button = browser.find_element_by_css_selector("[type='submit']").is_displayed()
	assert button, "There is not button!"
