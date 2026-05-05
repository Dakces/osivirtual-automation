import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import Config
from flows.login_flow import LoginFlow

@pytest.fixture(scope="function")
def driver():
    """
    Fixture que incializa y finaliza el WebDriver.
    Se ejecuta una vez por test.
    """

    options = webdriver.ChromeOptions()

    # Headless desde .env
    if Config.HEADLESS:
        options.add_argument("--headless=new")

    # Mantener navegador abierto
    if not Config.CLOSE_BROWSER:
        options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver

    # Cierre controlado del navegador
    if Config.CLOSE_BROWSER:
        driver.quit()

@pytest.fixture(scope="function")
def logged_driver(driver):
    """
    Fixture que devuelve un WebDriver con sesión iniciada.
    El login se ejecuta una sola vez por test.
    """

    login_flow = LoginFlow(driver, environment="CERT")
    result = login_flow.execute()

    if not result["success"]:
        pytest.fail("No se pudo iniciar sesión. Precondición fallida.")

    return driver
    