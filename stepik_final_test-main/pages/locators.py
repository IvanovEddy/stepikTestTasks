from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_ROOT = (By.CSS_SELECTOR, "#login_form")
    REGIST_ROOT = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOTPASS = (By.CSS_SELECTOR, "p a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REG_EMAIL = (By.CSS_SELECTOR, "id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")