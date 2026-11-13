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

## TC-COMPRA-10: Hacer checkout con los campos vacíos en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) |
| **Pasos** | 1. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. Se queda en la misma pantalla<br>2. Aparece una leyenda que nos dice que no pueden estar vacíos los campos<br>3. Los campos se ponen en color rojo |
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece una leyenda que nos dice: "Error: First Name is required"<br>3. Los campos se ponen en color rojo con una "x" sobre un círculo rojo al final de cada campo |
| **Estado** | ⚠️ Pasó con observación, la leyenda solo menciona que el campo de "First Name" es requerido, se recomienda ver si es conveniente que se mencionen que todos los campos son requeridos |

## TC-COMPRA-11: Hacer checkout con solo el campo de First Name lleno en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · First Name: Rodrigo |
| **Pasos** | 1. Llenar el campo de "First Name" con "Rodrigo"<br>2. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. Se queda en la misma pantalla<br>2. Aparece una leyenda que nos dice que no pueden estar vacíos los campos de "Last Name" y "Zip/Postal Code"<br>3. Los campos se ponen en color rojo |
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece una leyenda que nos dice: "Error: Last Name is required"<br>3. Los campos de "Last Name" y "Zip/Postal Code" se ponen en color rojo con una "x" sobre un círculo rojo al final de cada campo |
| **Estado** | ⚠️ Pasó con observación, la leyenda solo menciona que el campo de "Last Name" es requerido, se recomienda ver si es conveniente que se mencione que también el campo de "Zip/Postal Code" es requerido. Además, el campo de "First Name" también pone el borde rojo y la "x" sobre un círculo rojo, ver si es necesario que no lo marque como error |

## TC-COMPRA-12: Hacer checkout con los campos de First Name y Last Name llenos en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · First Name: Rodrigo · Last Name: Barriga |
| **Pasos** | 1. Llenar el campo de "First Name" con "Rodrigo"<br>2. Llenar el campo de "Last Name" con "Barriga"<br>3. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. Se queda en la misma pantalla<br>2. Aparece una leyenda que nos dice que no puede estar vacío el campo de "Zip/Postal Code"<br>3. El campo se pone en color rojo |
| **Resultado obtenido** | 1. Se queda en la misma pantalla<br>2. Aparece una leyenda que nos dice: "Error: Postal Code is required"<br>3. Los 3 campos se ponen en color rojo con una "x" sobre un círculo rojo al final de cada campo |
| **Estado** | ⚠️ Pasó con observación, los campos de "First Name" y "Last Name" también ponen el borde rojo y la "x" sobre un círculo rojo, ver si es necesario que no lo marque como error |

## TC-COMPRA-13: Hacer checkout con solo 1 carácter en los campos de First Name, Last Name y Zip/Postal Code en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · First Name: "x" · Last Name: "x" · Zip/Postal Code: "x" |
| **Pasos** | 1. Llenar los tres campos con una "x"<br>2. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Estado** | ⚠️ Pasó con observación. Existen nombres y apellidos de una sola letra. Sin embargo, un zip code de un carácter sí es dudoso. |

## TC-COMPRA-14: Hacer checkout con espacios en los campos de First Name, Last Name y Zip/Postal Code en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · First Name: " " · Last Name: " " · Zip/Postal Code: " " |
| **Pasos** | 1. Llenar los tres campos con un espacio<br>2. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. Se queda en la misma pantalla<br>2. Aparece "Error: First Name is required"<br>3. Los 3 campos se ponen en color rojo |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Estado** | ❌ Falló. La app ya exige estos campos. Un campo con solo espacios está vacío en la práctica, así que se salta validación que la propia app tiene |

## TC-COMPRA-15: Hacer checkout con los campos de First Name y Last Name llenos y Zip/Postal Code con letras en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · First Name: "Rodrigo" · Last Name: "Barriga" · Zip/Postal Code: "ABCDE" |
| **Pasos** | 1. Llenar los tres campos<br>2. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Estado** | ⚠️ Pasó con observación, en México son 5 dígitos, pero en Reino Unido o Canadá los códigos postales llevan letras, y SauceDemo es una tienda en inglés. Aceptar letras puede ser correcto. |

## TC-COMPRA-16: Hacer checkout con el campo de First Name con 100 caracteres y Last Name y Zip/Postal Code llenos en información

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/checkout-step-one.html (iniciar sesión → carrito → Checkout), con sesión iniciada con `standard_user` y "Sauce Labs Backpack" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · First Name: "A" cien veces · Last Name: "Barriga" · Zip/Postal Code: "12345" |
| **Pasos** | 1. Llenar los tres campos<br>2. Dar clic en el botón de "Continue" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparecen los datos del artículo a comprar, de la tarjeta de crédito, la información de envío, el desglose del costo<br>3. Aparece el botón de "Finish" |
| **Estado** | ⚠️ Pasó con observación, hay que consultar si debe haber un máximo de caracteres en los campos |

## TC-COMPRA-17: Confirmación de los datos del pedido en la página de resumen

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` y "Sauce Labs Backpack" y "Sauce Labs Bike Light" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · Sauce Labs Bike Light ($9.99) · First Name: "Rodrigo" · Last Name: "Barriga" · Zip/Postal Code: "12345" |
| **Pasos** | 1. Clic en el ícono de carrito<br>2. Clic en "Checkout"<br>3. Llenar First Name, Last Name y Zip/Postal Code con los datos base<br>4. Clic en "Continue" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparece "Sauce Labs Backpack", cantidad 1, $29.99<br>3. Aparece "Sauce Labs Bike Light", cantidad 1, $9.99<br>4. Muestra los datos de la tarjeta con la que se hará el cobro<br>5. Muestra la información del método de envío<br>6. Muestra el desglose del costo total incluyendo la suma de los dos productos y su respectivo impuesto |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparece "Sauce Labs Backpack", cantidad 1, $29.99<br>3. Aparece "Sauce Labs Bike Light", cantidad 1, $9.99<br>4. Muestra los datos de la tarjeta: "Payment Information: SauceCard #31337"<br>5. Muestra la información del método de envío: "Shipping Information: Free Pony Express Delivery!"<br>6. Muestra el desglose del costo: "Price Total Item total: $39.98 Tax: $3.20 Total: $43.18" |
| **Estado** | ⚠️ Pasó con observación, hay que consultar si debe también mostrar el nombre del tarjetahabiente y su dirección de facturación, así como la dirección de envío en la información del envío |

## TC-COMPRA-18: Cálculo correcto de subtotal, impuesto y total

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` y "Sauce Labs Backpack" y "Sauce Labs Bike Light" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · Sauce Labs Bike Light ($9.99) · First Name: "Rodrigo" · Last Name: "Barriga" · Zip/Postal Code: "12345" |
| **Pasos** | 1. Clic en el ícono de carrito<br>2. Clic en "Checkout"<br>3. Llenar First Name, Last Name y Zip/Postal Code con los datos base<br>4. Clic en "Continue" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparece "Sauce Labs Backpack", cantidad 1, $29.99<br>3. Aparece "Sauce Labs Bike Light", cantidad 1, $9.99<br>4. Muestra el desglose del costo total incluyendo la suma de los dos productos $39.98 ($29.99 + 9.99) y su respectivo impuesto.5. Total = Item total + Tax, exacto al centavo. |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-step-two.html`<br>2. Aparece "Sauce Labs Backpack", cantidad 1, $29.99<br>3. Aparece "Sauce Labs Bike Light", cantidad 1, $9.99<br>4. Muestra el desglose del costo total: $43.18 incluyendo la suma de los dos productos: $29.99 + $9.99 = $39.98 y su respectivo impuesto del 8.0%: (calculado: 3.20 / 39.98 = 8.0%) $3.20, con un total de  39.98 + 3.20 = 43.18 |
| **Estado** | ⚠️ Pasó con observación. La página no muestra la tasa de impuesto; se deduce un 8.0%. Consultar si es la tasa correcta |

## TC-COMPRA-19: El botón de Cancel regresa a la página de inventory conservando los productos en el carrito

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` y "Sauce Labs Backpack" y "Sauce Labs Bike Light" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · Sauce Labs Bike Light ($9.99) · First Name: "Rodrigo" · Last Name: "Barriga" · Zip/Postal Code: "12345" |
| **Pasos** | 1. Clic en el ícono de carrito<br>2. Clic en "Checkout"<br>3. Llenar First Name, Last Name y Zip/Postal Code con los datos base<br>4. Clic en "Continue"<br>5. Clic en "Cancel" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/inventory.html`<br>2. el ícono de carrito sigue mostrando el "2" sobre un círculo rojo<br>3. En ambos productos siguen los botones de "Remove" en rojo<br>4. Al dar clic en el ícono del carrito seguimos viendo los 2 productos |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/inventory.html`<br>2. el ícono de carrito sigue mostrando el "2" sobre un círculo rojo<br>3. En ambos productos siguen los botones de "Remove" en rojo<br>4. Al dar clic en el ícono del carrito seguimos viendo los 2 productos |
| **Estado** | ✅ Pasó. Esperaba que Cancel regresara a la tienda sin vaciar el carrito, porque cancelar el pago no significa abandonar la compra: así funcionan la mayoría de las tiendas en línea |

## TC-COMPRA-20: El botón de Finish nos da mensaje de confirmación, vacía el carrito y nos permite volver a inventory

| Campo | Contenido |
|---|---|
| **Precondición** | Estar en https://www.saucedemo.com/inventory.html, con sesión iniciada con `standard_user` y "Sauce Labs Backpack" y "Sauce Labs Bike Light" en el carrito |
| **Datos** | Usuario: `standard_user` · Contraseña: `secret_sauce` · Sauce Labs Backpack ($29.99) · Sauce Labs Bike Light ($9.99) · First Name: "Rodrigo" · Last Name: "Barriga" · Zip/Postal Code: "12345" |
| **Pasos** | 1. Clic en el ícono de carrito<br>2. Clic en "Checkout"<br>3. Llenar First Name, Last Name y Zip/Postal Code con los datos base<br>4. Clic en "Continue"<br>5. Clic en "Finish"<br>6. Clic en "Back Home" |
| **Resultado esperado** | 1. La URL cambia a `https://www.saucedemo.com/checkout-complete.html`<br>2. Aparece un mensaje de confirmación de nuestro pedido y la fecha estimada de llegada<br>3. El ícono del carrito ya no muestra número<br>4. La URL vuelve a `https://www.saucedemo.com/inventory.html` |
| **Resultado obtenido** | 1. La URL cambia a `https://www.saucedemo.com/checkout-complete.html`<br>2. Aparece el siguiente mensaje: "Thank you for your order! Your order has been dispatched, and will arrive just as fast as the pony can get there!"<br>3. El ícono del carrito ya no muestra número<br>4. Aparece el botón de "Generate PDF order"<br>5. La URL vuelve a `https://www.saucedemo.com/inventory.html` |
| **Estado** | ⚠️ Pasó con observación. La confirmación no indica fecha estimada de entrega |


