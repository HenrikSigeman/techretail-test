"""ProductPage – produktsidan /produkter/<id> (lösning lektion 2)."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.name = page.get_by_role("heading", level=1)
        self.price = page.get_by_test_id("product-price")
        self.stock_status = page.get_by_test_id("stock-status")
        self.quantity_input = page.get_by_label("Antal")
        self.add_to_cart_button = page.get_by_role("button", name="Lägg i kundvagn")

    def open(self, product_id: int) -> "ProductPage":
        """Gå till produktsidan för product_id och returnera self."""
        self.page.goto(f"/produkter/{product_id}")
        return self

    def add_to_cart(self, quantity: int = 1) -> None:
        """Fyll i antal och klicka på "Lägg i kundvagn"."""
        self.quantity_input.fill(str(quantity))
        self.add_to_cart_button.click()
