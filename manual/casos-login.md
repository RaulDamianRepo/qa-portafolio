# Casos de prueba: Login de SauceDemo

Aplicación: https://www.saucedemo.com/
Fecha de ejecución: 5 nov 2026
Ejecutado por: Raúl Damián

## TC-LOGIN-01: Login exitoso con usuario válido

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html`<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error |
| **Estado** | ✅ Pasó |

## TC-LOGIN-03: Login denegado a usuario bloqueado

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `locked_out_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. parece una leyenda sobre usuario restringido<br>3. los campos de username y password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Sorry, this user has been locked out`<br>3. el borde inferior de los campos en rojo y aparece una x en un circulo al final del campo.<br> |
| **Estado** | ✅ Pasó |


## TC-LOGIN-04: Login con campos vacíos

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | ninguno |
| **Pasos** | 1. Click en login<br>
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. Aparece una leyenda sobre usuario y contraseña no pueden estar vacios<br>3. los campos de username y password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Username is required`<br>3. el border inferior de los campos Username y Password en rojo y aparece una x en un circulo al final de esos campos..<br> |
| **Estado** | ❌ Falló, se espera que diga que tanto el username como el password son necesarios |

## TC-LOGIN-05: Login denegado con usuario pero con contraseña vacía

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | usuario: standard_user password:(vacía) |
| **Pasos** | 1. Escribir el usuario<br>2. Dejar la contraseña vacía<br>3. Clic en Login |
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. Aparece una leyenda sobre contraseña no puede estar vacio<br>3. el campo password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Password is required`<br>3. el border inferior de los campos Username y Password en rojo y aparece una x en un circulo al final de esos campos..<br> |
| **Estado** | ⚠️ Pasó con observación, la app también marca en rojo y pone una x en un circulo al final del campo en username. Consultar si ese es el comportamiento deseado |






