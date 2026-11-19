"""Givet exempel på API-tester (lektion 4). Läs dem innan du skriver egna i test_api.py."""

from testdata import STANDARD_USER


def test_exempel_produktlistan_har_30_produkter_med_ratt_falt(api_client):
    # Act
    response = api_client.get_products()
    # Assert: statuskod först, sedan innehåll och struktur (schema)
    assert response.status_code == 200
    body = response.json()
    assert body["count"] == 30
    assert {"id", "name", "price_ore", "category", "stock"} <= set(body["items"][0])


def test_exempel_fel_losenord_ger_401(api_client):
    response = api_client.login(STANDARD_USER.email, "fel-losenord")
    assert response.status_code == 401
    assert response.json()["detail"] == "Fel e-post eller lösenord."
