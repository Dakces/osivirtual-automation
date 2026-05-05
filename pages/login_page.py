from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)

    USERNAME_INPUT = (By.ID, "documentoIdentidad")
    PASSWORD_INPUT = (By.ID, "contrasena")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Ingresar']")

    LOGOUT_TEXT = (By.XPATH, "//*[contains(text(), 'Cerrar Sesión')]")
    LOGOUT_ICON = (By.XPATH, "//*[@icon-name='icon-cerrar-sesion']")

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.is_visible(self.LOGOUT_TEXT)
    