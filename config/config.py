import os
from dotenv import load_dotenv

# Carga variables del .env
load_dotenv()

class Config:
    # URLs
    BASE_URL_DESA = os.getenv("BASE_URL_DESA")
    BASE_URL_CERT = os.getenv("BASE_URL_CERT")
    BASE_URL_PROD = os.getenv("BASE_URL_PROD")
    LOGIN_PATH = os.getenv("LOGIN_PATH")

    # Credenciales
    USERNAME = os.getenv("OSIV_USER")
    PASSWORD = os.getenv("OSIV_PASSWORD")

    # Selenium
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 15))
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # Cierre Browser
    CLOSE_BROWSER = os.getenv("CLOSE_BROWSER", "true").lower() == "true"
