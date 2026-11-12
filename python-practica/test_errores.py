import errores

def test_convertir_tiempo_texto_valido_devuelve_float():
    resultado = errores.convertir_tiempo("4.8")
    assert resultado == 4.8

def test_convertir_tiempo_negativo_devuelve_none():
    resultado = errores.convertir_tiempo(-2)
    assert resultado is None