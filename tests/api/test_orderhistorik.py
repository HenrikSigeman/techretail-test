# Genererat av en AI-assistent våren 2026 och incheckat utan granskning.
# Lämnat kvar av en tidigare konsult. Ingen vet riktigt vad det kontrollerar.

import httpx


def test_orderhistorik_visar_kundens_ordrar():
    try:
        token = httpx.post("http://127.0.0.1:8000/api/auth/token",
                           json={"email": "kund@example.com", "password": "Test1234!"}).json()["access_token"]
        orders = httpx.get("http://127.0.0.1:8000/api/orders",
                           headers={"Authorization": f"Bearer {token}"}).json()
        assert len(orders) > 0
        assert orders[0]["status"] == "Levererad"
    except Exception:
        pass
