from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageLocators(object):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    INVENTORY = (By.CSS_SELECTOR, 'div.inventory_list')
    NEGATIVE_ASSERT = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    DROPDOWN_MENU = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    LOGOUT_ASSERT = (By.CSS_SELECTOR, 'div.bot_column')


class LoginPageMethods:

    def __init__(self, browser):
        self.browser = browser

    def fill_username(self, username):
        self.browser.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def fill_password(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def click_dropdown(self):
        self.browser.find_element(*LoginPageLocators.DROPDOWN_MENU).click()

    def click_logout(self):
        wait = WebDriverWait(self.browser, 5)
        expected_element = EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON)
        element = wait.until(expected_element)
        element.click()



    def login_icon_displayed(self):
        element = self.browser.find_element(*LoginPageLocators.LOGOUT_ASSERT)
        msg = element.is_displayed()
        return msg


    def go_to_website(self):
        self.browser.get("https://www.saucedemo.com/")

    def inventory_displayed(self):
        element = self.browser.find_element(*LoginPageLocators.INVENTORY)
        msg = element.is_displayed()
        return msg

    def error_displayed(self):
        element = self.browser.find_element(*LoginPageLocators.NEGATIVE_ASSERT)
        msg = element.is_displayed()
        return msg








