"""GUI-tester för söksidan /produkter.

Dessa tester kontrollerar att sökningen fungerar korrekt på produktsidan.
"""

from playwright.sync_api import expect
from pages.products_page import ProductsPage


def test_sokning_efter_lampa_visar_resultat(page):
    # Arrange
    products_page = ProductsPage(page)
    
    # Act
    products_page.open()
    products_page.filter_by("lampa")
    
    # Assert - Söksidan bör visa produkter
    expect(products_page.result_count).to_have_text("2 produkter")