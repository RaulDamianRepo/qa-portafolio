# Listas: varios datos en una sola variable

casos = ["TC-LOGIN-01", "TC-LOGIN-02", "TC-LOGIN-03"]

print(casos)
print(casos[0])        # primer elemento
print(casos[2])        # tercer elemento
print(casos[-1])       # último elemento
print(len(casos))      # cuántos elementos hay

casos.append("TC-LOGIN-04")    # agregar al final
print(casos)

casos.remove("TC-LOGIN-02")    # quitar uno por su valor
print(casos)

print("TC-LOGIN-01" in casos)  # ¿está en la lista?
print("TC-LOGIN-02" in casos)


resultados = []
print(len(resultados))
print(resultados.count(True))
Pass = resultados.count(True)
porcentaje = Pass / len(resultados) * 100
print(f"Pasaron {Pass} de {len(resultados)} pruebas ({porcentaje}%)")