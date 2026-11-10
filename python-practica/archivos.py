# Archivos: guardar y leer resultados

resultados = [
    "TC-LOGIN-01: PASÓ",
    "TC-LOGIN-04: FALLÓ",
    "TC-LOGIN-08: FALLÓ",

]

# 1. Escribir (crea el archivo, o lo reemplaza si ya existe)
with open("reporte.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Reporte de pruebas\n")
    for linea in resultados:  # noqa: FURB122
        archivo.write(linea + "\n")

# 2. Leer todo de una vez
with open("reporte.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)

# 3. Agregar al final sin borrar lo anterior
with open("reporte.txt", "a", encoding="utf-8") as archivo:
    archivo.write("TC-LOGIN-11: PASÓ\n")

# 4. Leer línea por línea
with open("reporte.txt","r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# guarda el diccionario en el archivo con el formato especificado
def guardar_reporte(casos, nombre_archivo):
    aprobadas = 0
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for id_caso, aprobado in casos.items():
           archivo.write(f"{id_caso} | {aprobado}\n")
           if aprobado == "PASÓ":
               aprobadas += 1
        archivo.write(f"Aprobadas: {aprobadas} de {len(casos)}\n")

casos = {
    "TC-LOGIN-05": "FALLÓ",
    "TC-LOGIN-07": "FALLÓ",
    "TC-LOGIN-09": "PASÓ",
    "TC-LOGIN-10": "PASÓ",
    "TC-LOGIN-12": "FALLÓ",
    "TC-LOGIN-13": "PASÓ",
}

guardar_reporte(casos, "reporte2.txt")

# Lee el archivo y devuelve una lista con los tests que fallaron
def leer_fallidos(nombre_archivo):
    fallidos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if "FALLÓ" in linea:
                    fallidos.append(linea.strip())
    except FileNotFoundError:
        return fallidos
    return fallidos

# imprimirá la lista con las pruebas que fallaron     
print(leer_fallidos("reporte2.txt"))

#imprimirá una lista vacía
print(leer_fallidos("no_existe.txt"))