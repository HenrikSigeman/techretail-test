"""Dina API-tester (lektion 4).

TODO 1: Skriv minst 6 API-tester. Blanda tre slag:
  - status:  rätt statuskod för ett lyckat anrop
  - schema:  svaret har rätt fält och typer
  - negativt fall: fel indata ger rätt felkod (401, 404, 409 eller 422)

Förslag:
  1. GET /api/products/1 ger 200 och namnet "Skruvdragare 18 V".
  2. Filtret category=verktyg ger bara produkter i kategorin verktyg.
  3. En okänd produkt (id 999) ger 404.
  4. Rabattkoden TECH10 ger 10 % rabatt på kundvagnen (logged_in_api_client).
  5. Den utgångna koden SOMMAR20 ger 422.
  6. Att lägga fler varor än lagret räcker till ger 409.

TODO 2: Skriv ett test som bevisar IDOR: standardkunden ska INTE kunna läsa
Robin Rings order 1002. Kursens krav: svaret ska vara 404 eller 403.
Butiken har felet, så testet blir rött. Markera det som ett känt fel:

    import pytest

    @pytest.mark.xfail(strict=True, reason="IDOR: andra kunders ordrar kan läsas")
    def test_kund_kan_inte_lasa_annan_kunds_order(logged_in_api_client):
        response = logged_in_api_client.get_order(1002)
        assert response.status_code in (403, 404)

strict=True betyder: om felet en dag rättas blir testet rött, och du tar bort markeringen.

Fixtures (finns i conftest.py):
  api_client            utan inloggning
  logged_in_api_client  inloggad som standardkunden (Kim Kund), tom kundvagn

Kör:  make test-api
Utmaning: skriv en fixture som loggar in via API:t och lägger sessionen i webbläsaren,
så att GUI-testerna slipper logga in via formuläret.
"""
