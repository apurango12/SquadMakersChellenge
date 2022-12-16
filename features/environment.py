from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.browser = browser


def after_scenario(context, scenario):
    context.browser.quit()

