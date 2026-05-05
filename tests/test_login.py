import pytest
from flows.login_flow import LoginFlow

@pytest.mark.login
def test_login_successful(driver):
    """
    Verifica que un usuario pueda inciar sesión correctamente en el sistema OsiVirtual.
    """
    

    # ==========================
    # Ejecución del flujo
    # ==========================
    login_flow = LoginFlow(driver, environment="CERT")
    result = login_flow.execute(measure_time=True)

    # ==========================
    # Validaciones
    # ==========================
    assert result["success"] is True, "El login no fue exitoso"

    if result["elapsed_time"] is not None:
        assert result["elapsed_time"] < 15, (
            f"El login tardó demasiado tiempo: {result['elapsed_time']:.2f} segundos"
        )
