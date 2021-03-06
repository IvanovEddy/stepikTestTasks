import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "URL is false"
        # проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_ROOT) is not None, "Login form is not presented"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGIST_ROOT) is not None, "Registration form is not presented"
        # есть форма регистрации на странице

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_pass = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_pass.send_keys(password)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2)
        reg_pass2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_btn.click()
