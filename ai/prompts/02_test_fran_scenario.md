# Prompt: automatiserat test från ett scenario

Byt ut texten inom [hakparenteser]. Granska svaret med GRANSKA-kortet och logga i `ai/AI-logg.md`.

---

Skriv ett pytest-test i Python för scenariot nedan. Projektet använder:
- fixturen `logged_in_api_client` (httpx-klient, klassen finns i api/client.py) för API-tester, eller
- Playwright med Page Objects i pages/ och fixturen `page` för GUI-tester.
- `expect(...)` för väntan. Aldrig time.sleep eller wait_for_timeout.
- Lokaliserare i ordningen get_by_role/get_by_label, get_by_test_id (attributet data-test), CSS.
- Testnamn på svenska utan å, ä, ö. Ett test kontrollerar en sak (AAA).
- Markera testet med @pytest.mark.ai_genererad.

Scenario:
[Klistra in scenariot]

Relevanta delar av api/client.py eller pages/:
[Klistra in de metoder testet behöver]
