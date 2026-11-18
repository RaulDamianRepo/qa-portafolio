from playwright.sync_api import Page, expect
from acciones import iniciar_sesion

def test_agregar_un_producto_al_carrito(page: Page):
    iniciar_sesion(page, "standard_user", "secret_sauce")

    # 1. Clic en "Add to cart" del Backpack
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # 2. Verificar que el ícono del carrito muestre "1"
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    expect(page.locator('[data-test="shopping-cart-link"]')).to_have_attribute('aria-label', 'Cart, 1 items')

    # 3. Verificar que el botón del Backpack ahora diga "Remove"
    expect(page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_text(
        "Remove")

    # 4. Abrir el carrito
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    
    # 5. Verificar nombre "Sauce Labs Backpack" y precio "$29.99"
    productos = page.locator('[data-test="inventory-item-name"]')
    expect(productos).to_have_count(1)
    expect(productos).to_have_text("Sauce Labs Backpack")
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(
        "$29.99")


def test_quitar_unico_producto_del_carrito_desde_pagina_carrito(page: Page):
    iniciar_sesion(page, "standard_user", "secret_sauce")

    # 1. Agregar Sauce Labs Bike Light
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    expect(page.locator('[data-test="remove-sauce-labs-bike-light"]')).to_have_text(
        "Remove")

    # 2. Abrir el carrito y confirmar que llegaste con carrito con 1 producto
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    productos = page.locator('[data-test="inventory-item-name"]')
    expect(productos).to_have_count(1)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    expect(page.locator('[data-test="shopping-cart-link"]')).to_have_attribute('aria-label', 'Cart, 1 items')

    # 3. Clic en Remove
    page.locator('[data-test="remove-sauce-labs-bike-light"]').click()

    # 4. Verificar que el carrito quedó vacío: 0 productos
    expect(productos).not_to_be_visible()
    expect(page.locator('[data-test="shopping-cart-link"]')).to_have_attribute('aria-label', 'Cart, empty')

    # 5. Verificar que el círculo rojo con el número ya no aparece
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)
