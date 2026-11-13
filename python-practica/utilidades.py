# Funciones reutilizables para reportes de prueba

def porcentaje_aprobadas(resultados):
    if len(resultados) == 0:
        return None
    return resultados.count(True) / len(resultados) * 100


def estado_texto(aprobado):
    if aprobado:
        return "PASÓ"
    return "FALLÓ"


# guarda el diccionario en el archivo con el formato especificado
def guardar_reporte(casos, nombre_archivo):
    aprobadas = 0
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("Reporte generado el 2026-11-11\n")
        for caso in casos:
           partes = caso.split(":")
           resultado = False
           if partes[1].strip() == "True":
               resultado = True
           aprobado = estado_texto(resultado)
           archivo.write(f"{partes[0]} | {aprobado}\n")
           if aprobado == "PASÓ":
               aprobadas += 1
        archivo.write(f"Aprobadas: {aprobadas} de {len(casos)}\n")

def calcular_total(precios,tasa_impuestos):
    subtotal = sum(precios)
    impuesto = round(subtotal * tasa_impuestos, 2)
    return round(subtotal + impuesto, 2)

if __name__ == "__main__":
    print("Se cargó utilidades.py")

