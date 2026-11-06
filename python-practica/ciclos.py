#Ciclos y condiciones

casos = [
    {"id": "TC-LOGIN-01", "aprobado": True},
    {"id": "TC-LOGIN-02", "aprobado": True},
    {"id": "TC-LOGIN-04", "aprobado": False},
    {"id": "TC-LOGIN-05", "aprobado": True},
]

# 1. Recorrer una lista
for caso in casos:
    print(caso["id"])

# 2. Recorrer y decidir
for caso in casos:
    if caso["aprobado"]:
        print(f"{caso['id']}: PASÓ")
    else:
        print(f"{caso['id']}: FALLÓ")

# 3. Varias condiciones
tiempo_carga = 4.2
if tiempo_carga <= 2:
    print("Rápido")
elif tiempo_carga <= 5:
    print("Aceptable")
else:
    print("Lento: reportar")

# 4. Repetir mientras se cumpla algo
intentos = 0
while intentos < 3:
    print(f"Intento {intentos + 1}")
    intentos += 1


def porcentaje_aprobadas(resultados):
    if len(resultados) == 0:
        return 0
    else:
        aprobadas= contar_aprobadas(resultados)
        return round((aprobadas/len(resultados)*100),2)
    

def contar_aprobadas(resultados):
    aprobadas = 0
    for caso in resultados:
        if caso["aprobado"]:
            aprobadas += 1
                
    return aprobadas

for caso in casos:
    if caso["aprobado"] == False:
        print(f"Revisar: {caso["id"]}")
print(f"{porcentaje_aprobadas(casos)}%")

lista_vacia = [ ]
lista_todas_true = [
    {"id": "TC-LOGIN-01", "aprobado": True},
    {"id": "TC-LOGIN-02", "aprobado": True},
    {"id": "TC-LOGIN-03", "aprobado": True},
    {"id": "TC-LOGIN-04", "aprobado": True},
]
lista_mixta = [
    {"id": "TC-LOGIN-05", "aprobado": True},
    {"id": "TC-LOGIN-06", "aprobado": False},
    {"id": "TC-LOGIN-07", "aprobado": False},
    {"id": "TC-LOGIN-08", "aprobado": True},
    {"id": "TC-LOGIN-09", "aprobado": True},
    {"id": "TC-LOGIN-10", "aprobado": True},
    {"id": "TC-LOGIN-11", "aprobado": False},
]
#Se espera que imprima 0
print(f"{porcentaje_aprobadas(lista_vacia)}")

#Se espera que imprima 100.0%
print(f"{porcentaje_aprobadas(lista_todas_true)}%")

#Se espera que imprima 57.14%
print (f"{porcentaje_aprobadas(lista_mixta)}%")
