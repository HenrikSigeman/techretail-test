"""Dina GUI-tester för produktsidan (lektion 2).

TODO (lektion 2): Skriv minst 3 tester som använder ProductPage.

Regler:
  - Namnet ska börja med test_ men INTE med test_exempel_.
  - Använd expect(...) för att kontrollera. Ingen time.sleep() eller wait_for_timeout().
  - Ett test kontrollerar en sak.

Förslag:
  1. Produktsidan för produkt 1 visar namnet "Skruvdragare 18 V".
  2. När du lägger 1 vara i kundvagnen visar badgen 1.
  3. När du lägger 3 st i kundvagnen visar badgen 3.
  4. (Valfritt) En inloggad kund (fixturen logged_in_user) kan lägga en vara i kundvagnen.

Mall att utgå från:

    from playwright.sync_api import expect
    from pages.product_page import ProductPage

    def test_produktsidan_visar_namnet(page):
        # Arrange
        product_page = ProductPage(page)
        # Act
        product_page.open(1)
        # Assert
        expect(product_page.name).to_have_text("Skruvdragare 18 V")

Kör dina tester med:        uv run pytest tests/gui -v
Se webbläsaren medan de kör: uv run pytest tests/gui --headed --slowmo 500
Kontrollera milstolpen med:  make milstolpe L=2
"""
import re

from playwright.sync_api import Page, expect 
from pages.product_page import ProductPage 
def test_produktsidan_visar_namnet(page): 
  # Arrange 
  product_page = ProductPage(page) 
  # Act 
  product_page.open(1) 
  # Assert 
  expect(product_page.name).to_have_text("Skruvdragare 18 V")

def test_en_vara_ger_raknaren_1(page): 
  # Arrange 
  product_page = ProductPage(page).open(3) 
  # Act 
  product_page.add_to_cart() 
  # Assert 
  product_page.expect_cart_count(1)

def test_tre_varor_ger_raknaren_3(page): 
  # Arrange 
  product_page = ProductPage(page).open(4) 
  # Act 
  product_page.add_to_cart(3) 
  # Assert 
  product_page.expect_cart_count(3)


def test_example(page: Page) -> None: 
  page.goto("http://127.0.0.1:8000/produkter/1") 
  page.get_by_test_id("quantity-input").click() 
  page.get_by_test_id("quantity-input").fill("2") 
  page.get_by_test_id("add-to-cart").click() 
  expect(page.get_by_test_id("cart-badge")).to_contain_text("2") 