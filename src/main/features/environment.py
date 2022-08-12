from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# import pages
from src.main.features.pages.home_page import HomePage
from src.main.features.pages.element_page import ElementPage


def before_scenario(context, scenario):
    option = webdriver.ChromeOptions()
    # option.add_argument("--start-maximized")
    # option.add_argument("--headless")  # run browser headless
    # option.add_experimental_option("detach", True)  # keep browser open after finished test
    context.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option) # chrome option
    context.browser.implicitly_wait(10)  # implicitly_wait (seconds)

    # set page for context
    context.home_page = HomePage(context.browser)
    context.element_page = ElementPage(context.browser)


def after_scenario(context, step):
    # take screenshot when step failed
    if step.status == "failed":
        context.browser.save_screenshot("src/main/features/screenshots/" + context.scenrio + step.name + ".png")
