#Mi primer programa: variables y tipos

nombre_caso = "TC-LOGIN-02" #str: texto, siempre entre comillas
numero_pasos = 3            #int: número entero
tiempo_segundos = 1.5       #float: número con decimales
aprobado = True             #bool: True o False (verdadero o falso)

print(nombre_caso)
print(type(nombre_caso))
print(type(numero_pasos))
print(type(tiempo_segundos))
print(type(aprobado))

print(f"El caso {nombre_caso} tiene {numero_pasos} pasos y tardó {tiempo_segundos} segundos")

id_caso = "TC-LOGIN-01" #str: texto, siempre entre comillas
numero_pasos1 = 3            #int: número entero
aprobado1 = True             #bool: True o False (verdadero o falso)
usuario = "standard_user"    

print(f"{id_caso} | Usuario: {usuario} | Pasos: {numero_pasos1} | Aprobado: {aprobado1}")