# Funciones: código reutilizable con nombre

def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Raúl"))
print(saludar("QA"))

def describir_caso(caso):
    return f"{caso['id']} | {caso["titulo"]} | Aprobado: {caso['aprobado']}"

caso_1 = {"id": "TC-LOGIN-01", "titulo": "Login exitoso con usuario válido", "aprobado": True}
caso_4 = {"id": "TC-LOGIN-04", "titulo": "Login con campos vacíos", "aprobado": False}

print(describir_caso(caso_1))
print(describir_caso(caso_4))

def porcentaje_aprobadas(resultados):
    aprobadas = resultados.count(True)
    return aprobadas / len(resultados) * 100

print(porcentaje_aprobadas([True,False,True,True]))


def contar_fallidas(resultados):
    fallidas = resultados.count(False)
    return fallidas

def reporte(resultados):
    Total = len(resultados)
    Fallidas = contar_fallidas(resultados)
    Aprobadas = porcentaje_aprobadas(resultados)
    return f"Total: {Total} | Fallidas: {Fallidas} | Aprobadas: {round(Aprobadas, 2)}%"

corrida_1 = [True,False,False,True,False,True,True]
corrida_2 = [False,True,False,True,False]
# Esperado: Total: 5 | Fallidas: 3 | Aprobadas: 40.0%

print(reporte(corrida_1))
print(reporte(corrida_2))

