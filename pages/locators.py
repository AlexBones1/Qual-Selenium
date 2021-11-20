from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_USERNAME = (By.ID, "id_login-username")
    LOGIN_FORM_PASSWORD = (By.ID, "id_login-password")
    REGISTER_FORM_USERNAME = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASSWORD_RE = (By.ID, "id_registration-password2")


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_NAME = (By.CSS_SELECTOR, ".alertinner strong")