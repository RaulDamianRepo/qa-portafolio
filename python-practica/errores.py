# Manejo de errores

# 1. Atrapar un error conocido
def porcentaje(aprobadas, total):
    try:
        return aprobadas/total * 100
    except ZeroDivisionError:
        return None

print(porcentaje(3,4))
print(porcentaje(0,0))

# 2. Convertir texto a número
tiempo_texto = "cinco"
try:
    tiempo = int(tiempo_texto)
    print(tiempo)
except ValueError:
    print(f"'{tiempo_texto}' no es un número")

# 3. Ver el mensaje del error y ejecutar algo siempre
casos = ["TC-LOGIN-01","TC-LOGIN-02"]
try:
    print(casos[10])
except IndexError as error:
    print(f"Error capturado: {error}")
finally:
    print("Esto se ejecuta siempre")

def convertir_tiempo(texto):
    try:
        numero = float(texto)
        if numero < 0:
            return None
        else:
            return numero
    except ValueError:
        return None
    
# imprimirá 4.8
print(convertir_tiempo("4.8"))

# imprimirá None
print(convertir_tiempo("cinco"))

# imprimirá None
print(convertir_tiempo(""))

# imprimirá None
print(convertir_tiempo("-2"))

# imprimirá 0.0
print(convertir_tiempo("0"))


print(type(convertir_tiempo("cinco")))
print(type(convertir_tiempo("-2")))
