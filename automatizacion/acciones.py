URL_LOGIN = "https://www.saucedemo.com/"

def iniciar_sesion(page, usuario, contrasena):
    page.goto(URL_LOGIN)
    page.locator("#user-name").fill(usuario)
    page.locator("#password").fill(contrasena)
    page.locator("#login-button").click()