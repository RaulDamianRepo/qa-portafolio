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

