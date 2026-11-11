# Casos de prueba: Compras de SauceDemo

Aplicación: https://www.saucedemo.com/
Fecha de ejecución: 11 nov 2026
Ejecutado por: Raúl Damián

## TC-COMPRA-01: Agregar 1 producto con carrito vacío

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` y con el carrito vacío |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) |
| **Pasos** | 1. Clic en "Add to cart" en el producto "Sauce Labs Backpack"<br>2. Abrir el carrito y comparar que se haya agregado el producto y su precio |
| **Resultado esperado** | 1. En el ícono del carrito aparece un "1" sobre un círculo rojo<br>2. El botón del producto "Sauce Labs Backpack" cambia a "Remove" con un borde y letra en rojo<br>3. Aparece el producto "Sauce Labs Backpack" con su precio ($29.99) en la página del carrito |
| **Resultado obtenido** | 1. En el ícono del carrito aparece un "1" sobre un círculo rojo<br>2. El botón del producto "Sauce Labs Backpack" cambia a "Remove" con un borde y letra en rojo<br>3. Aparece el producto "Sauce Labs Backpack" con su precio ($29.99) en la página del carrito |
| **Estado** | ✅ Pasó |

## TC-COMPRA-02: Agregar los 6 productos

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` y con el carrito vacío |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| **Pasos** | 1. Clic en "Add to cart" en cada uno de los productos |
| **Resultado esperado** | 1. En el ícono del carrito aparece un "6" sobre un círculo rojo<br>2. El botón de todos los productos cambia a "Remove" con un borde y letra en rojo |
| **Resultado obtenido** | 1. En el ícono del carrito aparece un "6" sobre un círculo rojo<br>2. El botón de todos los productos cambia a "Remove" con un borde y letra en rojo |
| **Estado** | ✅ Pasó |

## TC-COMPRA-03: Quitar un producto desde la página de productos

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` con el carrito con 2 productos |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Bolt T-Shirt ($15.99) · Sauce Labs Fleece Jacket ($49.99) |
| **Pasos** | 1. Clic en el botón de "Remove" en el producto "Sauce Labs Fleece Jacket"<br>2. Clic en el ícono del carrito |
| **Resultado esperado** | 1. En el ícono del carrito se decrementa de 2 a 1 sobre un círculo rojo<br>2. El botón del producto "Sauce Labs Fleece Jacket" cambia a "Add to cart" con un borde y letra en negro<br>3. La página del carrito se actualiza quitando el producto "Sauce Labs Fleece Jacket" y dejando solo el producto Sauce Labs Bolt T-Shirt |
| **Resultado obtenido** | 1. En el ícono del carrito se decrementa de 2 a 1 sobre un círculo rojo<br>2. El botón del producto "Sauce Labs Fleece Jacket" cambia a "Add to cart" con un borde y letra en negro<br>3. La página del carrito se actualiza quitando el producto "Sauce Labs Fleece Jacket" y dejando solo el producto Sauce Labs Bolt T-Shirt |
| **Estado** | ✅ Pasó |

## TC-COMPRA-04: Quitar un producto desde la página de carrito

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` con el carrito y 3 productos: "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt" y "Sauce Labs Fleece Jacket" |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · Sauce Labs Bolt T-Shirt ($15.99) · Sauce Labs Fleece Jacket ($49.99) |
| **Pasos** | 1. Clic en el ícono del carrito<br>2. En el producto "Sauce Labs Fleece Jacket", dar clic en el botón de "Remove" |
| **Resultado esperado** | 1. La página se actualiza mostrando solo los productos "Sauce Labs Backpack" y "Sauce Labs Bolt T-Shirt"<br>2. El ícono del carrito va de 3 a 2 |
| **Resultado obtenido** | 1. La página se actualiza mostrando solo los productos "Sauce Labs Backpack" y "Sauce Labs Bolt T-Shirt"<br>2. El ícono del carrito va de 3 a 2 |
| **Estado** | ✅ Pasó |

## TC-COMPRA-05: Quitar todos los productos desde la página de carrito

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` con el producto "Sauce Labs Bike Light" agregado al carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Bike Light ($9.99) |
| **Pasos** | 1. Clic en el ícono del carrito<br>2. En la descripción del producto dar clic en el botón de "Remove" |
| **Resultado esperado** | 1. La página se actualiza sin productos<br>2. En el ícono del carrito se borra el "1" junto con el círculo rojo |
| **Resultado obtenido** | 1. La página se actualiza sin productos<br>2. En el ícono del carrito se borra el "1" junto con el círculo rojo |
| **Estado** | ⚠️ Pasó con observación, sería adecuado que apareciera una leyenda de "Your cart is empty" cuando no hay ningún producto |

## TC-COMPRA-06: Cerrar sesión con el carrito con productos y volver a iniciar sesión

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Bike Light ($9.99) · Sauce Labs Backpack ($29.99) |
| **Pasos** | 1. Clic en "Add to cart" en los productos "Sauce Labs Bike Light" y "Sauce Labs Backpack"<br>2. Clic en el menú ☰<br>3. En el menú desplegable clic en Logout<br>4. Escribir el usuario<br>5. Escribir la contraseña<br>6. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. En el ícono del carrito sigue mostrando un 2 y los botones de "Remove" siguen en los productos "Sauce Labs Bike Light" y "Sauce Labs Backpack" |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html`<br>2. En el ícono del carrito sigue mostrando un 2 y los botones de "Remove" siguen en los productos "Sauce Labs Bike Light" y "Sauce Labs Backpack" |
| **Estado** | ✅ Pasó |

## TC-COMPRA-07: Regresar a la página de productos desde el carrito

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/cart.html, con sesión iniciada con `standard_user` y 5 productos en el carrito: "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Bike Light" y "Sauce Labs Onesie" |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · Sauce Labs Bike Light ($9.99) · Sauce Labs Bolt T-Shirt ($15.99) · Sauce Labs Fleece Jacket ($49.99) · Sauce Labs Onesie ($7.99) |
| **Pasos** | 1. Clic en "Continue Shopping" |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. En el ícono del carrito sigue mostrando el número "5" y los 5 productos: "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt" y "Sauce Labs Fleece Jacket", "Sauce Labs Bike Light" y "Sauce Labs Onesie" siguen con sus botones de "Remove" |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html`<br>2. En el ícono del carrito sigue mostrando el número "5" y los 5 productos: "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt" y "Sauce Labs Fleece Jacket", "Sauce Labs Bike Light" y "Sauce Labs Onesie" siguen con sus botones de "Remove" |
| **Estado** | ✅ Pasó |

## TC-COMPRA-08: Carrito de un usuario visible al iniciar sesión con otro usuario

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Usuario: `visual_user` · Sauce Labs Bike Light ($9.99) · Sauce Labs Backpack ($29.99) |
| **Pasos** | 1. Clic en "Add to cart" en los productos "Sauce Labs Bike Light" y "Sauce Labs Backpack"<br>2. Clic en el menú ☰<br>3. En el menú desplegable clic en Logout<br>4. Escribir el usuario `visual_user` <br>5. Escribir la contraseña<br>6. Clic en Login |
| **Resultado esperado** | 1. La URL cambia a `/inventory.html`<br>2. En el ícono del carrito no muestra número y todos los productos muestran "Add to cart" |
| **Resultado obtenido** | 1. La URL cambia a `/inventory.html`<br>2. En el ícono del carrito sigue mostrando un 2 y los botones de "Remove" siguen en los productos "Sauce Labs Bike Light" y "Sauce Labs Backpack" |
| **Estado** | ❌ Falló, fallo de seguridad al mostrar el carrito de otro usuario |

## TC-COMPRA-09: Página de productos muestra precios, imágenes e íconos correctos con visual_user

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/, sin sesión iniciada |
| **Datos** | Usuario: `visual_user` · Contraseña: `secret_sauce` · Precios de referencia (vistos con `standard_user`): Sauce Labs Backpack $29.99 · Sauce Labs Bike Light $9.99 · Sauce Labs Bolt T-Shirt $15.99 · Sauce Labs Fleece Jacket $49.99 · Sauce Labs Onesie $7.99 · Test.allTheThings() T-Shirt (Red) $15.99 |
| **Pasos** | 1. Escribir el usuario<br>2. Escribir la contraseña<br>3. Clic en Login<br>4. Revisar precio, imagen y nombre de cada producto<br>5. Revisar la posición del ícono del carrito y del filtro |
| **Resultado esperado** | 1. Cada producto muestra el precio de referencia<br>2. Cada producto muestra su propia imagen<br>3. El ícono del carrito está en la esquina superior derecha y no se encima con el filtro |
| **Resultado obtenido** | 1. "Sauce Labs Backpack" con precio $3.16, "Sauce Labs Bike Light" con precio de $75.01, "Sauce Labs Bolt T-Shirt" con precio de $10.74, "Sauce Labs Fleece Jacket" con precio de $96.12, "Sauce Labs Onesie" con precio de $18.93 y "Test.allTheThings() T-Shirt (Red)" con precio de $88.01, cada vez que se recarga la página los precios de todos los productos cambian<br>2."Sauce Labs Backpack" muestra una imagen de un perro<br>3. El ícono del carrito aparece arriba del ícono del filtro |
| **Estado** | ❌ Falló. Precios distintos a los de referencia, imagen incorrecta en Sauce Labs Backpack e ícono del carrito desacomodado. |