import pytest

@pytest.mark.e2e
def test_ingreso_ventanilla_virtual(logged_driver):
    """
    Verifica que se pueda:
    - Abrir la Ventanilla Virtual
    - Cambiar a la nueva pestaña
    - Aceptar la modal inicial
    """

    from flows.ventanilla_virtual_flow import VentanillaVirtualFlow

    vvo_flow = VentanillaVirtualFlow(logged_driver)

    # Acción bajo prueba
    vvo_flow.open_vvo()

    # Validación mínima: seguimos en una pantalla distinta
    assert len(logged_driver.window_handles) > 1
    