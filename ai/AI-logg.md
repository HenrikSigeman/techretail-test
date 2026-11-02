# AI-logg

Här skriver du ner varje gång du använder en AI-assistent i kursen. Loggen är en del av inlämningen och visar att du granskar det AI:n ger dig.

Granska varje gång med GRANSKA-kortet:

| Steg | Fråga |
|---|---|
| **Bad** | Vad bad du om? Klistra in prompten. |
| **Fick** | Vad gav AI:n dig? Kort sammanfattning eller länk till commit. |
| **Kör** | Gick koden att köra? Vad blev resultatet? |
| **Bryt** | Ändrade du koden eller appen så att testet borde bli rött? Blev det rött av rätt anledning? |
| **Data** | Skickade du någon persondata eller hemlighet? (Svaret ska vara nej.) |
| **Kostnad** | Ungefär hur många tokens, hur lång tid, vilken kostnad? |
| **Beslut** | Accepterade, ändrade eller kastade du resultatet – och varför? |

Tumregel: lägg mer tid på att granska än på att generera.

---

## Mall – kopiera för varje ny post

### ÅÅÅÅ-MM-DD · Lektion X · Verktyg: (till exempel Copilot Free)

- **Bad:**
- **Fick:**
- **Kör:**
- **Bryt:**
- **Data:**
- **Kostnad:**
- **Beslut:**

---

## Mina poster

### 2026-11-02 · Lektion 1 · Verktyg: Copilot

- **Bad:** Föreslå ett pytest-test för apply_discount i src/techretail/pricing.py som prövar ett gränsvärde jag inte redan har. Följ AAA. Ändra inga filer.
- **Fick:** ett test för att säkerställa att en beställning på 0 kr med 15% rabatt fortfarande blir 0 kr efter att rabatten har lagts på.

```
def test_nollpris_ger_noll_efter_rabatt():
    # Arrange
    pris = 0

    # Act
    resultat = apply_discount(pris, 15)

    # Assert
    assert resultat == 0.0
```

- **Kör:** Jag körde uv run pytest tests/unit -v: 9 tester. Gröna resultat.
- **Bryt:** Ändrade värdet på resultat till 1.0. Rött resultat med assert 0.0 == 1.0. Rött av rätt anledning
- **Data:** Nej ingen persondata eller hemlighet skickades.
- **Kostnad:** 15 sekunder och 0.3 tokens. $ 0.003
- **Beslut:** Jag har behållit resultatet som del av testsviten. Även om det är högst osannolikt att en kund kommer att handla något för 0.0kr och försöka att få rabatt på det så kan ett plötsligt misslyckat test betyda att det har uppstått ett allvarligt fel med koden.

---

## Summering (fylls i före inlämningen)

| | Antal / värde |
|---|---|
| Antal AI-poster | |
| Accepterade utan ändring | |
| Ändrade | |
| Kastade | |
| Ungefärlig total kostnad (tokens eller kronor) | |
| Vad lärde du dig om att granska AI-genererade tester? | |
