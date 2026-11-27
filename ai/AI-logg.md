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
- **Beslut:** Behövde kompletteras. Copilot skrev fyra tester istället för ett och de tre så extra resurser gick åt till att skriva tester som jag inte bett om. Jag har tagit bort de tre tester som jag inte bad om och behöll "test_sokning_efter_lampa_visar_resultat", har behövt skriva om testet. Från början så klickade den inte på sök-knappen innan den kollar upp antalet resultat, vilket negerar själva testet. Vad gäller products_page som Copilot genererade så fanns det bra och dåliga metoder. Filen behövde ses över och kompletteras med mer användbara metoder. Exempelvis så finns det en metod som heter "search" som tar emot en string och förväntas fylla i sökfältet med den, och returnerar sedan resultatet. Den gör detta utan att klicka på "filtrera"-knappen. Namnet behöver också bytas ut till "filter_by" för att förtydliga att listan inte aktivt hämtar poster vid filtrering. Jag tar bort de onödiga testerna, byter namn på "search" till "filter_by", samt kompletterar metoden med att den faktiskt klickar på "filtrera"-knappen.


### 2026-11-26 · Lektion 5 · Verktyg: AI-genererad fil i repot 
 - **Bad:** "Skriv Playwright-tester i Python för kassan i vår webbutik." 
  Inget krav, inga fixtures, inga regler. 
  - **Fick:** Fyra tester i ai/granska/test_ai_kassa.py. 
  - **Kör:** Nej. ModuleNotFoundError: No module named 'requests'. 
  - **Bryt:** Inget test kan bli rött av rätt anledning, till exempel i test_api_order så blir r.status_code aldrig 500. 
  - **Data:** Ja, namn och personnummer i test_kassa. Det bryter mot regel 7. 
  Jag byter de värden mot värdena i testkonton, och tar även bort referens till personnummer. 
  - **Kostnad:** Cirka 7 minuter granskning. 
  - **Beslut:** test_api_order och test_kassa skrivs om. Test_kassa testar bara en del av köp-processen (gå till kassamed en vara i varukorgen). test_presentkort_drar_av_beloppet och test_tre_misslyckade_inloggningar_lasar_kontot testar ingenting i varken kravspec eller manualen.

### 2026-11-26 · Lektion 5 · Verktyg: Copilot agent 
 - **Bad:** Prompten i labbens steg 9, test 2 (TR-13). 
 - **Fick:** test_okand_rabattkod_avvisas i tests/api/test_ai_genererade.py. Det väntade statuskoden 400 och texten ur kravet. 
 - **Kör:** Rött: E assert 422 = 400 
 - **Bryt:** Testet var redan rött. Felet låg i testets facit, inte i butiken. 
 - **Data:** Nej, endast testkonton och rabattkoder. 
 - **Kostnad:** Cirka 10 minuter. 
 - **Beslut:** Ändrat. Ändrade förväntad statuskod till 422. Kravspec nämner ingen förväntad statuskod i detta fall, men i /docs och i andra liknande tester förväntas svarskoden vara 422. 

### 2026-11-26 · Lektion 5 · Verktyg: Copilot agent 
- **Bad:** Prompten i labbens steg 9, test 1 (TR-13). 
- **Fick:** test_ny_giltig_rabattkod_ersatter_den_tidigare i tests/api/test_ai_genererade.py. 
Det kontrollerade enbart statuskoden 200. 
- **Kör:** Grönt. 
- **Bryt:** Bytte VINTER15 mot TECH10
- **Data:** Nej, endast testkonton och rabattkoder. 
- **Kostnad:** Cirka 10 minuter. 
- **Beslut:** Ändrat. Testet kontrollerade inte om den senare rabattkoden bytte ut den första, utan väntade endast på en 200-kod som svar. Den testade inte kravet i TR-13 där en andra rabattkod alltid byter ut den första. Testet ändrades så att den kontrollerade namnet på den aktiva rabattkoden, samt den nuvarande rabatten i procent.

### 2026-11-27 · Lektion 5 · Verktyg: Copilot agent 
 - **Bad:** Prompten i labbens steg 9, test 3 (TR-03). 
 - **Fick:** test_okand_epost_ger_samma_besked_som_fel_losenord i tests/api/test_ai_genererade.py. 
  Det väntade statuskoden 401 och texten ur kravet. 
 - **Kör:** Grönt. 
 - **Bryt:** Bytte "Fel e-post eller lösenord." mot "Fel lösenord". 
 - **Data:** Nej, endast en påhittad e-postadress och kursens testlösenord. 
 - **Kostnad:** Cirka 5 minuter. 
 - **Beslut:** Behållet utan ändring. Testet blir rött av rätt anledning.

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
