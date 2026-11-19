from playwright.sync_api import Page, expect
from acciones import iniciar_sesion, llenar_informacion


def test_compra_completa_con_dos_productos(page: Page):
    iniciar_sesion(page, "standard_user", "secret_sauce")

    # 1. Agregar Sauce Labs Backpack y Sauce Labs Bike Light
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    expect(page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_text(
        "Remove")
    expect(page.locator('[data-test="remove-sauce-labs-bike-light"]')).to_have_text(
        "Remove")

    # 2. Abrir el carrito y confirmar que hay 2 productos
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator('[data-test="cart-list"]')).to_be_visible()
    productos = page.locator('[data-test="inventory-item-name"]')
    expect(productos).to_have_count(2)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")
    expect(page.locator('[data-test="shopping-cart-link"]')).to_have_attribute(
        'aria-label', 'Cart, 2 items')

    # 3. Click en Checkout
    page.locator('[data-test="checkout"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(page.locator('[data-test="checkout-info-container"]')).to_be_visible()

    # 4. Llenar First Name, Last Name y Zip con tus datos base y dar Continue
    llenar_informacion(page, "Rodrigo", "Barriga", "12345")
    expect(page.locator('[data-test="checkout-summary-container"]')).to_be_visible()

    # 5. En el resumen, verificar:
    #   - Item total: $39.98
    #   - Tax: $3.20
    #   - Total: $43.18
    expect(page.locator('[data-test="subtotal-label"]')).to_contain_text("$39.98")
    expect(page.locator('[data-test="tax-label"]')).to_contain_text("$3.20")
    expect(page.locator('[data-test="total-label"]')).to_contain_text("$43.18")

    # 6. Clic en Finish
    page.locator('[data-test="finish"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator('[data-test="checkout-complete-container"]')).to_be_visible()

    # 7. Verificar el mensaje "Thank you for your order!"
    expect(page.locator('[data-test="complete-header"]')).to_have_text(
        "Thank you for your order!")

    # 8. Verificar que el carrito quedó vacío
    expect(page.locator('[data-test="shopping-cart-badge"]')).not_to_be_visible()
    expect(page.locator('[data-test="shopping-cart-link"]')).to_have_attribute(
        'aria-label', 'Cart, empty')
