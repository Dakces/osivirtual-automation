import time
from pages.login_page import LoginPage
from config.config import Config

class LoginFlow:
    """
    Flow encargado del proceso de autenticación en el sistema OsiVirtual.
    """

    def __init__(self, driver, environment="CERT"):
        self.driver = driver
        self.environment = environment.upper()
        self.login_page = LoginPage(
            driver,
            timeout=Config.DEFAULT_TIMEOUT
        )

    # ========================
    # Utilidades internas
    # ========================
    def _get_login_url(self):
        """
        Construye la URL de login según el entorno.
        """
        if self.environment == "DESA":
            base_url = Config.BASE_URL_DESA
        elif self.environment == "PROD":
            base_url = Config.BASE_URL_PROD
        else: #CERT por defecto
            base_url = Config.BASE_URL_CERT

        return f"{base_url}{Config.LOGIN_PATH}"
    
    # ========================
    # Ejecución del flow
    # ========================
    def execute(self, measure_time=False):
        """
        Ejecuta el flujo de login.
        :param measure_time: bool
            Indica si se debe medir el tiempo de carga post-login
        :return:
            dict con el resultado del login
        """
        login_url = self._get_login_url()
        self.login_page.open(login_url)

        self.login_page.enter_username(Config.USERNAME)
        self.login_page.enter_password(Config.PASSWORD)

        start_time = None
        if measure_time:
            start_time = time.time()

        self.login_page.click_login()

        login_success = self.login_page.is_logged_in()

        elapsed_time = None
        if measure_time and start_time:
            elapsed_time = time.time() - start_time

        return {
            "success": login_success,
            "elapsed_time": elapsed_time
        }
    