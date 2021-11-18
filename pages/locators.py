from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_USERNAME = (By.ID, "id_login-username")
    LOGIN_FORM_PASSWORD = (By.ID, "id_login-password")
    REGISTER_FORM_USERNAME = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASSWORD_RE = (By.ID, "id_registration-password2")