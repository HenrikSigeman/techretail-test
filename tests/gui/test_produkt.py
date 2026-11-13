"""GUI-tester för produktsidan (lösning lektion 2)."""

from playwright.sync_api import expect

from pages.product_page import ProductPage


def test_produktsidan_visar_namn_och_pris(page):
    # Arrange
    product_page = ProductPage(page)
    # Act
    product_page.open(1)
    # Assert
    expect(product_page.name).to_have_text("Skruvdragare 18 V")
    expect(product_page.price).to_have_text("1 499,00 kr")


def test_en_vara_i_kundvagnen_visar_1_i_badgen(page):
    product_page = ProductPage(page).open(3)
    product_page.add_to_cart()
    product_page.expect_cart_count(1)


def test_tre_varor_i_kundvagnen_visar_3_i_badgen(page):
    product_page = ProductPage(page).open(4)
    product_page.add_to_cart(3)
    product_page.expect_cart_count(3)


def test_slut_i_lager_har_inaktiv_kopknapp(page):
    product_page = ProductPage(page).open(9)
    expect(product_page.stock_status).to_have_text("Slut i lager")
    expect(product_page.add_to_cart_button).to_be_disabled()


def test_inloggad_kund_kan_lagga_vara_i_kundvagnen(page, logged_in_user):
    product_page = ProductPage(page).open(11)
    product_page.add_to_cart(2)
    product_page.expect_cart_count(2)
