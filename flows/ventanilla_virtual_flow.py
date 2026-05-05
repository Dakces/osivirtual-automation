from selenium.webdriver.support.ui import WebDriverWait

from pages.home_page import HomePage
from pages.ventanilla_virtual_page import VentanillaVirtualPage
from config.config import Config

class VentanillaVirtualFlow:
    """
    Flow de ingreso a la Ventanilla Virtual (VVO).
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)
        self.home_page = HomePage(driver, Config.DEFAULT_TIMEOUT)
        self.vvo_page = VentanillaVirtualPage(driver, Config.DEFAULT_TIMEOUT)

    def open_vvo(self):
        """
        Abre la Ventanilla Virtual, cambia a la nueva pestaña y acepta la modal inicial.
        """

        original_window = self.driver.current_window_handle

        # 1. Esperar que el menú esté listo
        self.home_page.wait_until_menu_ready()

        # 2. Esperar que el botón VVO esté realmente listo
        self.home_page.wait_for_vvo_ready()

        # 3. Click en Ventanilla Virtual
        self.home_page.open_ventanilla_virtual()

        # 4. Esperar nueva pestaña
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # 5. Cambiar a la nueva pestaña
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

        # 6. Aceptar modal inicial
        if self.vvo_page.modal_inicial_existe():
            self.vvo_page.aceptar_modal_inicial()
        