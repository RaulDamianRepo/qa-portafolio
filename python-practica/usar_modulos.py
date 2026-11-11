# Usar funciones de otro archivo y de Python

import utilidades
from datetime import date

resultados = [
    "TC-LOGIN-05: True",
    "TC-LOGIN-06: False",
    "TC-LOGIN-08: True",
]

print(utilidades.porcentaje_aprobadas([True, False, True, True]))
print(utilidades.estado_texto(False))
print(f"Reporte generado el {date.today()}")

# Reporte generado el 2026-11-11
# TC-LOGIN-05 | PASÓ
# TC-LOGIN-06 | FALLÓ
# TC-LOGIN-08 | PASÓ
# Aprobadas: 2 de 3
utilidades.guardar_reporte(resultados, "reporte_nuevo.txt")

