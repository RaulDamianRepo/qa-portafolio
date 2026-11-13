import utilidades

def test_porcentaje_con_aprobadas_y_fallidas():
    resultado = utilidades.porcentaje_aprobadas([True,  False, True, True])
    assert resultado == 75.0

def test_porcentaje_lista_vacia_devuelve_none():
    resultado = utilidades.porcentaje_aprobadas([])
    assert resultado is None 

def test_estado_texto_cuando_falla():
    resultado = utilidades.estado_texto(False)
    assert resultado == "FALLÓ"

def test_subtotal_backpack_y_bike_light():
    assert sum([29.99,9.99]) == 39.98


def test_total_con_impuestos_8_por_ciento():
    total = utilidades.calcular_total([29.99,9.99], 0.08)
    assert total == 43.18