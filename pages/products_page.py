"""ProductsPage – produktlistsidan /produkter (med sökning).

Sidan visar alla produkter med möjlighet att filtrera efter produkter.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    path = "/produkter"

    def __init__(self, page: Page):
        super().__init__(page)
        # Lokaliserare för sökningen (följ ordningen: role > test_id > CSS > XPath)
        self.search_input = page.get_by_role("searchbox")
        self.search_button = page.get_by_role("button", name="Filtrera")
        self.result_count = page.get_by_test_id("result-count")
        self.product_cards = page.locator('[data-test="product-card"]')

    def filter_by(self, query: str) -> "ProductsPage":
        """Sök efter en produkt med given sökterm."""
        self.search_input.fill(query)
        self.search_button.click()
        return self


    def get_product_names(self) -> list[str]:
        """Returnera namn på alla produkter som visas."""
        names = []
        for i in range(self.product_cards.count()):
            card = self.product_cards.nth(i)
            # Följ lokaliseringsordningen: data-test > CSS
            name_locator = card.locator('[data-test="product-name"]')
            if name_locator.count() > 0:
                text = name_locator.text_content()
                if text:
                    names.append(text.strip())
        return names

    def has_product(self, product_name: str) -> bool:
        """Kontrollera om en produkt med givet namn visas."""
        return product_name in self.get_product_names()

    def search_result_contains(self, text: str) -> bool:
        """Kontrollera om söksidan innehåller given text."""
        return text.lower() in self.page.content().lower()
