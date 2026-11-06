# Casos de prueba: Login de SauceDemo

Aplicación: https://www.saucedemo.com/
Fecha de ejecución: 6 nov 2026
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

## TC-LOGIN-02: Login fallido por contraseña incorrecta

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce1` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. Aparece una leyenda sobre usuario y contraseña no coinciden<br>3. los campos de username y password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Username and password do not match any user in this service`<br>3. el borde inferior de los campos Username y Password en rojo y aparece una x en un circulo al final de esos campos.<br> |
| **Estado** | ⚠️ Pasó con observación, La leyenda aparece desfasado con su recuadro.  |

## TC-LOGIN-03: Login denegado a usuario bloqueado

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `locked_out_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. Aparece una leyenda sobre usuario restringido<br>3. los campos de username y password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Sorry, this user has been locked out`<br>3. el borde inferior de los campos en rojo y aparece una x en un circulo al final del campo.<br> |
| **Estado** | ✅ Pasó |


## TC-LOGIN-04: Login con campos vacíos

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | ninguno |
| **Pasos** | 1. Click en login<br>
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. Aparece una leyenda sobre usuario y contraseña no pueden estar vacíos<br>3. los campos de username y password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Username is required`<br>3. el borde inferior de los campos Username y Password en rojo y aparece una x en un circulo al final de esos campos.<br> |
| **Estado** | ❌ Falló, se espera que diga que tanto el username como el password son necesarios |

## TC-LOGIN-05: Login denegado con usuario pero con contraseña vacía

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user` · Contraseña:(vacía) |
| **Pasos** | 1. Escribir el usuario<br>2. Dejar la contraseña vacía<br>3. Clic en Login |
| **Resultado esperado** | 1. Se queda en la misma pantalla <br>2. Aparece una leyenda sobre contraseña no puede estar vacía<br>3. el campo password en rojo<br>
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Password is required`<br>3. el borde inferior de los campos Username y Password en rojo y aparece una x en un circulo al final de esos campos.<br> |
| **Estado** | ⚠️ Pasó con observación, la app también marca en rojo y pone una x en un circulo al final del campo en username. Consultar si ese es el comportamiento deseado |

## TC-LOGIN-06: Login con usuario con mayúsculas

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `Standard_User` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error |
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Username and password do not match any user in this service`<br>3. No aparece el ícono del carrito<br>4. El borde inferior de los campos Username y Password en rojo y aparece una x en un círculo al final de esos campos. |
| **Estado** | ⚠️ Pasó con observación: "El login distingue mayúsculas en el usuario. No hay requisito que lo defina; consultar si es el comportamiento deseado |

## TC-LOGIN-07: Login con un espacio al final del usuario

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user ` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error |
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece la leyenda: `Epic sadface: Username and password do not match any user in this service`<br>3. No aparece el ícono del carrito<br>4. El borde inferior de los campos Username y Password en rojo y aparece una x en un círculo al final de esos campos. |
| **Estado** | ⚠️ Pasó con observación,pero con un argumento más fuerte: los usuarios copian y pegan su nombre de usuario y arrastran espacios.Quitar los espacios al inicio y al final es una practica común. |

## TC-LOGIN-08: Productos muestran su imagen correcta con problem_user.

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `problem_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. Cada producto muestra su propia imagen<br>5. No aparece ningún mensaje de error |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html`<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. Muestra la misma imagen de un perro en todos los productos<br>5. No aparece ningún mensaje de error |
| **Estado** | ❌ Falló, las imágenes que se muestran no son las de los productos |

## TC-LOGIN-09: Login con velocidad de carga adecuada

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `performance_glitch_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html` en 2 segundos <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. Cada producto muestra su propia imagen<br5. No aparece ningún mensaje de error |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html` en 4.8s|5.1s|4.9s<br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. Cada producto muestra su propia imagen<br>5. No aparece ningún mensaje de error |
| **Estado** | ❌ Falló, le toma más del doble del tiempo cargar la página |

## TC-LOGIN-10: Login regresando con el botón de atrás

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login<br>4. Clic en el botón atrás en el navegador  |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html` <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error<br>5. Al dar click 'atrás', nos regresa a la página de login<br>6. Al escribir la URL  `https://www.saucedemo.com/inventory.html`, la sesión sigue activa y se ven los productos |
| **Resultado obtenido**| 1. La URL cambia a `/inventory.html` <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error<br>5. Al dar click 'atrás', nos regresa a la página de login<br>6. Al cambiar la URL a `https://www.saucedemo.com/inventory.html`, la sesión sigue activa y se ven los productos |
| **Estado** | ✅ Pasó |

## TC-LOGIN-11: Login, Logout y luego intentar volver a /inventory.html

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login<br>4. Clic en el menú ☰<br>5. En el menú desplegable click en Logout<br>6. Escribir en la barra de direcciones https://www.saucedemo.com/inventory.html  | 
| **Resultado esperado** | 1. La URL cambia a `/inventory.html` <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error<br>5. Al dar click a Logout, nos regresa a la página de login<br>6. Al escribir la URL  `https://www.saucedemo.com/inventory.html`,  nos aparece una leyenda que diga que no se puede acceder sin haber iniciado sesión |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html` <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error<br>5. Al dar click a Logout, nos regresa a la página de login<br>6. Al escribir la URL  `https://www.saucedemo.com/inventory.html`,  Aparece la leyenda: `Epic sadface: You can only access '/inventory.html' when you are logged in.` y el borde inferior de los campos Username y Password en rojo y aparece una x en un círculo al final de esos campos. La leyenda aparece desfasada hacía arriba del recuadro.|
| **Estado** | ⚠️ Pasó con observación, la leyenda aparece desfasada hacía arriba del recuadro. |

## TC-LOGIN-12: Login, Logout y luego botón de atrás del navegador

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login<br>4. Clic en el menú ☰<br>5. En el menú desplegable click en Logout<br>6. Clic en el botón atrás en el navegador  | 
| **Resultado esperado** | 1. La URL cambia a `/inventory.html` <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error<br>5. Al dar clic a Logout, nos regresa a la página de login<br>6. Al dar clic en el botón atrás en el navegador  nos aparece una leyenda que diga que no se puede acceder sin haber iniciado sesión |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html` <br>2. Aparece el título "Products"<br>3. Se ve el ícono del carrito<br>4. No aparece ningún mensaje de error<br>5. Al dar clic a Logout, nos regresa a la página de login<br>6. Al dar clic en el botón atrás en el navegador, Aparece la leyenda: `Epic sadface: You can only access '/inventory.html' when you are logged in.` y el borde inferior de los campos Username y Password en rojo y aparece una x en un círculo al final de esos campos. La leyenda aparece desfasada hacía arriba del recuadro. |
| **Estado** | ⚠️ Pasó con observación, la leyenda aparece desfasada hacía arriba del recuadro. |