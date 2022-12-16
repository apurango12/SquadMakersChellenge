from time import sleep

from behave import *

from features.pages.home_page import HomePageMethods


@when('Select the two products in the menu')
def step_impl(context):
    context.home_page = HomePageMethods(context.browser)
    context.home_page.add_product1()
    context.home_page.add_product2()


@when('Complete the checkout')
def step_impl(context):
    context.home_page.click_cart_button()
    context.home_page.checkout_button()
    context.home_page.fill_name("Andres")
    context.home_page.fill_last_name("Test")
    context.home_page.fill_zip_code("05001")
    context.home_page.continue_button()
    context.home_page.finish_button()


@then('The products are bought successfully')
def step_impl(context):
    message = context.home_page.finish_order_displayed()
    assert message is True


