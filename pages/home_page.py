from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import ActionChains

class HomePage(BasePage):
    """
    Page Object de la pantalla principal de OsiVirtual.
    """

    BTN_VVO = (
        By.XPATH,
        "//mat-list-item[.//span[normalize-space()='Ventanilla virtual (VVO)']]"
    )

    SIDENAV = (By.ID, "sidenav")

    def wait_until_menu_ready(self):
        self.wait_for_visibility(self.SIDENAV)

    def wait_for_vvo_ready(self):
        self.wait.until(
            lambda d: d.find_element(*self.BTN_VVO).is_displayed()
            and d.find_element(*self.BTN_VVO).is_enabled()
        )

    def open_ventanilla_virtual(self):
        element = self.wait_for_clickable(self.BTN_VVO)
        
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.pause(0.5)
        actions.click()
        actions.perform()
