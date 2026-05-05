from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    Clase base para todas las páginas.
    Contiene acciones genéricas de Selenium.
    """

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # =========================
    # Métodos de espera
    # =========================
    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
    
    # =========================
    # Acciones comunes
    # =========================
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def type(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait_for_visibility(locator)
            return True
        except TimeoutException:
            return False