from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class VentanillaVirtualPage(BasePage):
    """
    Page Object del módulo Ventanilla Virtual (VVO).
    Maneja por ahora únicametne la modal inicial.
    """

    # SweetAlert2 - Botón Aceptar
    BTN_ACEPTAR_MODAL = (
        By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled"
    )

    def aceptar_modal_inicial(self):
        """
        Acepta la ventana emergente inicial de la VVO.
        """
        self.wait_for_clickable(self.BTN_ACEPTAR_MODAL)
        self.click(self.BTN_ACEPTAR_MODAL)

    def modal_inicial_existe(self):
        """
        Verifica si la modal inicial está visible.
        """
        try:
            self.wait_for_visibility(self.BTN_ACEPTAR_MODAL)
            return True
        except TimeoutException:
            return False
