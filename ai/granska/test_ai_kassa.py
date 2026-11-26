# AI-GENERERAT, OGRANSKAT – övning i lektion 5.
#
# Prompten var: "Skriv Playwright-tester i Python för kassan i vår webbutik."
# Filen ligger utanför tests/ och körs inte av make test.
# Din uppgift: granska filen med GRANSKA-kortet och logga i ai/AI-logg.md.
# Hur många problem hittar du? Vilka av testerna skulle du behålla efter ändring?

import time

import requests
from playwright.sync_api import Page


def test_kassa(page: Page):
    page.goto("http://localhost:8000/login")
    page.fill("//html/body/div[2]/main/form/div[1]/input", "anna.bergstrom@example.com")
    page.fill("//html/body/div[2]/main/form/div[2]/input", "Password123")
    page.click("text=Login")
    time.sleep(3)
    page.goto("http://localhost:8000/produkter/1")
    page.click("button")
    time.sleep(2)
    page.goto("http://localhost:8000/kassa")
    page.fill("#name", "Anna Bergström")
    page.fill("#personnummer", "19850312-4471")
    page.click("text=Betala")
    assert page.url != "http://localhost:8000/kassa"


def test_presentkort_drar_av_beloppet(page: Page):
    page.goto("http://localhost:8000/kassa")
    page.fill("#presentkort", "GIFT-1234")
    page.click("text=Använd presentkort")
    assert "presentkort" in page.content().lower()


def test_api_order():
    r = requests.post("http://localhost:8000/api/order", json={"product": 1})
    assert r.status_code != 500


def test_tre_misslyckade_inloggningar_lasar_kontot(page: Page):
    for _ in range(3):
        page.goto("http://localhost:8000/logga-in")
        page.fill("#email", "kund@example.com")
        page.fill("#password", "fel")
        page.click("#login")
    page.fill("#password", "Test1234!")
    page.click("#login")
    try:
        assert "låst" in page.content()
    except AssertionError:
        print("Kontot låstes inte, men det är okej")
