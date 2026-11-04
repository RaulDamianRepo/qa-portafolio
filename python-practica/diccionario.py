#Diccionarios: datos con nombre

caso = {
    "id": "TC-LOGIN-02",
    "titulo": "Login fallido por contraseña incorrecta",
    "usuario": "standard_user",
    "pasos": 3,
    "aprobado": True,
}

print(caso)
print(caso["titulo"])   # leer un valor por su clave
print(caso["pasos"])

caso["aprobado"] = False   # modificar un valor
caso["prioridad"] = "alta" # agregar una clave nueva
print(caso)

print("usuario" in caso)   # ¿existe esa clave?
print(caso.get("autor"))   # leer una clave que NO existe, sin error
print(caso.get("autor", "sin autor")) # lo mismo, con valor por defecto
print(caso.keys())       # todas las claves


casos = [
    {"id": "TC-LOGIN-01", "usuario": "standard_user", "aprobado": True},
    {"id": "TC-LOGIN-02", "usuario": "standard_user", "aprobado": True},
    {"id": "TC-LOGIN-03", "usuario": "locked_out_user", "aprobado": False},
]

print(casos[2]["usuario"])      # posición 2 de la lista → clave "usuario"
casos[1]["aprobado"] = False
print(casos)                     # verificar el cambio
print(len(casos))
