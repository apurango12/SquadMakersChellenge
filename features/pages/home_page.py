from selenium.webdriver.common.by import By


class HomePageLocators(object):
    ADD_PRODUCT1 = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_PRODUCT2 = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    CART_BUTTON = (By.ID, 'shopping_cart_container')
    CHECKOUT = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    FINISH_ORDER = (By.CSS_SELECTOR, '#checkout_complete_container > h2')


class HomePageMethods:

    def __init__(self, browser):
        self.browser = browser

    def add_product1(self):
        self.browser.find_element(*HomePageLocators.ADD_PRODUCT1).click()

    def add_product2(self):
        self.browser.find_element(*HomePageLocators.ADD_PRODUCT2).click()

    def click_cart_button(self):
        self.browser.find_element(*HomePageLocators.CART_BUTTON).click()

    def checkout_button(self):
        self.browser.find_element(*HomePageLocators.CHECKOUT).click()

    def continue_button(self):
        self.browser.find_element(*HomePageLocators.CONTINUE_BUTTON).click()

    def finish_button(self):
        self.browser.find_element(*HomePageLocators.FINISH_BUTTON).click()

    def fill_name(self, name):
        self.browser.find_element(*HomePageLocators.FIRST_NAME).send_keys(name)

    def fill_last_name(self, last_name):
        self.browser.find_element(*HomePageLocators.LAST_NAME).send_keys(last_name)

    def fill_zip_code(self, zip_code):
        self.browser.find_element(*HomePageLocators.ZIP_CODE).send_keys(zip_code)

    def finish_order_displayed(self):
        element = self.browser.find_element(*HomePageLocators.FINISH_ORDER)
        msg = element.is_displayed()
        return msg













