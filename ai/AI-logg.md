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

### 2026-11-09 . Lektion 2 . Verktyg: Copilot

- **Bad:** Använd Playwright MCP. Öppna http://127.0.0.1:8000/produkter och sök 
efter lampa. Beskriv kort vad sidan visar. Skriv sedan ett pytest-test i 
tests/gui/test_sok.py som kontrollerar sökresultatet. Följ lokaliseringsordningen 
i pages/base_page.py. Inga fasta väntetider. Kör testet med: uv run pytest 
tests/gui/test_sok.py -v
- **Fick:** En nyskapad pages-fil: "products_page.py", samt en ny testfil: "tests/gui/tests_sok.py":
```
def test_sokning_efter_lampa_visar_resultat(page):
    """Testa att sökning efter 'lampa' visar produkter."""
    # Arrange
    products_page = ProductsPage(page)
    
    # Act
    products_page.open()
    initial_count = products_page.product_cards.count()
    products_page.search("lampa")
    
    # Assert - Söksidan bör visa produkter
    product_names = products_page.get_product_names()
    assert len(product_names) > 0, "Sökningen efter 'lampa' bör visa minst en produkt"


def test_sokruta_accepterar_text(page):
    """Testa att sökreutan tar emot text korrekt."""
    # Arrange
    products_page = ProductsPage(page)
    
    # Act
    products_page.open()
    products_page.search_input.fill("lampa")
    
    # Assert
    search_value = products_page.search_input.input_value()
    assert search_value == "lampa", f"Sökreutan bör innehålla 'lampa', men innehåller '{search_value}'"


def test_produktsidan_laddas(page):
    """Testa att produktlistsidan laddas utan fel."""
    # Arrange
    products_page = ProductsPage(page)
    
    # Act
    products_page.open()
    
    # Assert - Sidan ska innehålla produkter
    expect(products_page.product_cards.first).to_be_visible()
    product_names = products_page.get_product_names()
    assert len(product_names) > 0, "Produktlistan bör inte vara tom"


def test_produkt_namn_visas_korrekt(page):
    """Testa att produktnamn extraheras korrekt."""
    # Arrange
    products_page = ProductsPage(page)
    
    # Act
    products_page.open()
    
    # Assert
    product_names = products_page.get_product_names()
    # Kontrollera att vi får ett rimligt antal produkter
    assert len(product_names) > 5, "Bör visa minst 6 produkter på standardsidan"
    # Kontrollera att namnen inte är tomma
    assert all(len(name) > 0 for name in product_names), "Alla produktnamn bör ha längd > 0"
```
- **Kör:** testet körs utan problem och ger fyra stycken gröna "passed" resultat.
- **Bryt:** test_sokning_efter_lampa_visar_resultat faller inte som förväntat när söktermen "lampa" byts till "klampa". Oförändrat grönt resultat. Resten av testerna faller som förväntat när jag medvetet bryter funktionen.
- **Data:** Nej
- **Kostnad:** 4 minuter, 20 credits (~$0.2)
- **Beslut:** Inte så bra resultat. Dels så skrev copilot 4 tester istället för bara 1 som jag bad om, och dessutom så är det inte jättebra tester, speciellt inte eftersom att det handlar om dyra GUI-tester. Jag hade tagit bort alla tester förutom den första, "test_sokning_efter_lampa_visar_resultat", men hade såklart skrivit om den så att den faktiskt utför testet korrekt. Just nu så klickar den inte på sök-knappen innan den kollar på antalet resultat, vilket motarbetar själva testet. Vad gäller products_page så har den ett par stycken användbara funktioner, men i de flesta fall är de överflödiga. Filen behöver ses över och kompletteras med mer användbara metoder. Exempelvis så finns det en metod som heter "search" som tar emot en string och förväntas fylla i sökfältet med den, och returnerar sedan resultatet. Den gör detta utan att klicka på "sök"-knappen. Namnet behöver också bytas ut till "filter_by", eftersom att den tekniskt sett inte söker på något, utan bara filtrerar bort.

## Summering (fylls i före inlämningen)

| | Antal / värde |
|---|---|
| Antal AI-poster | |
| Accepterade utan ändring | |
| Ändrade | |
| Kastade | |
| Ungefärlig total kostnad (tokens eller kronor) | |
| Vad lärde du dig om att granska AI-genererade tester? | |
