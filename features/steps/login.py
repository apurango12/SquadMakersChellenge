from behave import *

from features.pages.login_page import LoginPageMethods


@given('Go to the website')
def step_impl(context):
    context.login_page = LoginPageMethods(context.browser)
    context.login_page.go_to_website()


@when('User logs in with valid credential')
def step_impl(context):
    context.login_page.fill_username('standard_user')
    context.login_page.fill_password('secret_sauce')
    context.login_page.click_login()


@then('I should be logged in successfully')
def step_impl(context):
    inventory = context.login_page.inventory_displayed()
    assert inventory is True


@when('Fill invalid username and password')
def step_impl(context):
    context.login_page.fill_username('standard_user1')
    context.login_page.fill_password('secret_sauce1')
    context.login_page.click_login()


@then('I should get an error message')
def step_impl(context):
    error = context.login_page.error_displayed()
    assert error is True


@given('Im in the main page')
def step_impl(context):
    context.execute_steps(u"""
            Given Go to the website
            When User logs in with valid credential
            Then I should be logged in successfully
        """)


@when('Go to the dropdown menu')
def step_impl(context):
    context.login_page.click_dropdown()


@when('hit the logout button')
def step_impl(context):
    context.login_page.click_logout()


@then('The application logged out successfully')
def step_impl(context):
    icon = context.login_page.login_icon_displayed()
    assert icon is True

