from selenium.webdriver.common.by import By
from src.main.features.pages.base_page import BasePage


class ElementPage(BasePage):

    page_elements = {
        # text box
        "text box": (By.XPATH, "//span[.='Text Box']"),
        "full name": (By.ID, "userName"),
        "email": (By.ID, "userEmail"),
        "current address": (By.ID, "currentAddress"),
        "permanent address": (By.ID, "permanentAddress"),
        "submit button": (By.ID, "submit"),
        "result area": (By.CSS_SELECTOR, ".border"),

        # checkbox
        "check box": (By.XPATH, "//span[.='Check Box']"),
        "home": (By.CSS_SELECTOR, "[for='tree-node-home'] > .rct-checkbox > .rct-icon"),


    }
