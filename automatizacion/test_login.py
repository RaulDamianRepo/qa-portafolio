# Pruebas automatizadas del login de SauceDemo

from playwright.sync_api import Page, expect

URL_LOGIN = "https://www.saucedemo.com/"


def iniciar_sesion(page, usuario, contrasena):
    page.goto(URL_LOGIN)
    page.locator("#user-name").fill(usuario)
    page.locator("#password").fill(contrasena)
    page.locator("#login-button").click()


def test_login_exitoso_con_usuario_valido(page: Page):
    iniciar_sesion(page, "standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_fallido_por_contrasena_incorrecta(page: Page):
    iniciar_sesion(page, "standard_user", "secret_sauce1")

    expect(page).to_have_url(URL_LOGIN)
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Username and password "
        "do not match any user in this service"
    )


def test_login_denegado_a_usuario_bloqueado(page: Page):
    iniciar_sesion(page, "locked_out_user", "secret_sauce")

    expect(page).to_have_url(URL_LOGIN)
    expect(page.locator('[data-test="error"]')).to_have_text(
        "Epic sadface: Sorry, " 
        "this user has been locked out."
    )
