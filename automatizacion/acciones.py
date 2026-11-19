URL_LOGIN = "https://www.saucedemo.com/"

def iniciar_sesion(page, usuario, contrasena):
    page.goto(URL_LOGIN)
    page.locator("#user-name").fill(usuario)
    page.locator("#password").fill(contrasena)
    page.locator("#login-button").click()

def llenar_informacion(page, nombre, apellido, cp):
    page.locator("#first-name").fill(nombre)
    page.locator("#last-name").fill(apellido)
    page.locator("#postal-code").fill(cp)
    page.locator("#continue").click()