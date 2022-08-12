from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def click_on_element(self, element):
        self.browser.find_element(*self.page_elements[element]).click()

    def input_text(self, element, content):
        self.browser.find_element(*self.page_elements[element]).send_keys(content)

    def wait_until_clickable(self, element):
        try:
            wait = WebDriverWait(self.browser, 15)
            expected_element = expected_conditions.element_to_be_clickable(element)
            wait.until(expected_element)
        except TimeoutError:
            raise

    def get_element_text(self, element):
        return self.browser.find_element(*self.page_elements[element]).text

    def get_element_attribute(self, element, attribute):
        return self.browser.find_element(*self.page_elements[element]).get_attribute(attribute)
