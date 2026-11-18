# Pruebas automatizadas del login de SauceDemo

import pytest
from playwright.sync_api import Page, expect
from acciones import URL_LOGIN, iniciar_sesion

URL_LOGIN = "https://www.saucedemo.com/"

@pytest.mark.parametrize(
        "usuario, contrasena, mensaje",
        [
            ("", "", "Epic sadface: Username is required"),

            # TC-LOGIN-05: usuario lleno, contraseña vacía
            ("standard_user", "", "Epic sadface: Password is required"),

            # TC-LOGIN-02: contraseña incorrecta
            ("standard_user", "secret_sauce1", 
             "Epic sadface: Username and password "
            "do not match any user in this service"),
           
            # TC-LOGIN-03: usuario bloqueado
            ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ],
        ids=["campos_vacios", "contrasena_vacia", "contrasena_incorrecta", "usuario_bloqueado"],
)
def test_login_con_datos_invalidos(page: Page, usuario, contrasena, mensaje):
    iniciar_sesion(page, usuario, contrasena)

    expect(page).to_have_url(URL_LOGIN)
    expect(page.locator('[data-test="error"]')).to_have_text(mensaje)
    
def test_login_exitoso_con_usuario_valido(page: Page):
    iniciar_sesion(page, "standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


