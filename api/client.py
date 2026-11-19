"""TechRetailClient – en liten API-klient ovanpå httpx (given kod, lektion 4).

Metoderna returnerar httpx.Response. Då kan testet själv kontrollera
statuskod, svarstid och innehåll:

    response = client.get_product(1)
    assert response.status_code == 200
    assert response.json()["name"] == "Skruvdragare 18 V"

Belopp i API:t anges i öre: 19990 betyder 199,90 kr.
API-dokumentationen finns på http://127.0.0.1:8000/docs
"""

from __future__ import annotations

import httpx


class TechRetailClient:
    def __init__(self, base_url: str, timeout: float = 10.0):
        self.http = httpx.Client(base_url=base_url, timeout=timeout)

    # -------------------------------------------------------------- inloggning

    def login(self, email: str, password: str) -> httpx.Response:
        """Logga in. Vid lyckad inloggning skickas token automatiskt i följande anrop."""
        response = self.http.post("/api/auth/token", json={"email": email, "password": password})
        if response.status_code == 200:
            self.http.headers["Authorization"] = f"Bearer {response.json()['access_token']}"
        return response

    def logout(self) -> None:
        self.http.headers.pop("Authorization", None)

    def me(self) -> httpx.Response:
        return self.http.get("/api/me")

    # -------------------------------------------------------------- produkter

    def get_products(self, **params) -> httpx.Response:
        """Sök produkter. Exempel: get_products(q="lampa", category="el-belysning", max_price=100)."""
        return self.http.get("/api/products", params=params)

    def get_product(self, product_id: int) -> httpx.Response:
        return self.http.get(f"/api/products/{product_id}")

    def get_categories(self) -> httpx.Response:
        return self.http.get("/api/categories")

    # -------------------------------------------------------------- kundvagn

    def get_cart(self) -> httpx.Response:
        return self.http.get("/api/cart")

    def add_to_cart(self, product_id: int, quantity: int = 1) -> httpx.Response:
        return self.http.post("/api/cart/items", json={"product_id": product_id, "quantity": quantity})

    def set_quantity(self, product_id: int, quantity: int) -> httpx.Response:
        return self.http.patch(f"/api/cart/items/{product_id}", json={"quantity": quantity})

    def clear_cart(self) -> httpx.Response:
        return self.http.delete("/api/cart")

    def apply_discount(self, code: str) -> httpx.Response:
        return self.http.post("/api/cart/discount", json={"code": code})

    # -------------------------------------------------------------- ordrar

    def create_order(self, name: str = "Kim Kund", address: str = "Testgatan 1", zip: str = "111 22",
                     city: str = "Exempelstad", payment: str = "kort", personnummer: str | None = None) -> httpx.Response:
        body = {"name": name, "address": address, "zip": zip, "city": city, "payment": payment}
        if personnummer:
            body["personnummer"] = personnummer
        return self.http.post("/api/orders", json=body)

    def get_orders(self) -> httpx.Response:
        return self.http.get("/api/orders")

    def get_order(self, order_id: int) -> httpx.Response:
        return self.http.get(f"/api/orders/{order_id}")

    def close(self) -> None:
        self.http.close()
