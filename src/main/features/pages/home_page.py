from selenium.webdriver.common.by import By
from src.main.features.pages.base_page import BasePage


class HomePage(BasePage):

    page_elements = {
        "elements": (By.XPATH, "//h5[.='Elements']"),
        "forms": (By.XPATH, "//h5[.='Forms']"),
    }
