# Testscenarier från krav

> Del av inlämningen (lektion 5). Kedjan är: krav (TR-xx) → scenarier med hjälp av AI → granskade scenarier → automatiserade tester.
> Skriv på svenska i Gherkin: Egenskap, Scenario, Givet, När, Så, Och. Ange kravets ID ovanför varje scenario.
> Skriv minst 3 scenarier. Markera vad du ändrade efter granskningen.

**Prompt som användes:** `ai/prompts/01_scenarier_fran_krav.md` (se även posten i `ai/AI-logg.md`)

## Exempel (givet)

```gherkin
Egenskap: Fri frakt
  # TR-14
  Scenario: Frakt tas ut strax under gränsen
    Givet att kundvagnen innehåller varor för 499,99 kr efter rabatt
    När kunden går till kassan
    Så är frakten 49,00 kr
```

## Mina scenarier

```gherkin
Egenskap: Rabattkoder 
  # TR-13 
  Scenario: En ny giltig kod ersätter den tidigare 
    Givet att kunden har använt rabattkoden TECH10 
    När kunden använder rabattkoden VINTER15 
    Så gäller 15 % rabatt 
    Och rabattkoden TECH10 gäller inte längre 
  # TR-13 
  Scenario: En okänd kod avvisas 
    När kunden använder rabattkoden FINNSINTE 
    Så visas "Rabattkoden är ogiltig eller har gått ut." 
    Egenskap: Inloggning 
  # TR-03 
  Scenario: Okänd e-post ger samma besked som fel lösenord 
    När någon loggar in med en e-postadress som inte finns 
    Så visas "Fel e-post eller lösenord."

```

## Granskning

*Vad hallucinerade AI:n (funktioner som inte finns, fel gränsvärden)? Vad ändrade du, och varför? Vilka scenarier blev automatiserade tester, och var finns de?*

AI:n hittade på en rabattkod samt scenario när en kund får sitt konto spärrat. 
Det står inte i kravspecen, så jag tog bort de testen. 
AI:n missade att kontrollera vilken rabattkod som gällde efter att den nya rabattkoden applicerades. 
Jag lade till det från kravspec TR-13. 
Testet för en okänd kod väntade sig statuskoden 400. 
Kravet TR-13 anger ingen statuskod. 
API-dokumentationen och mitt test för SOMMAR20 säger 422, så jag ändrade facit.

| Scenario | Ändrat efter granskning? | Automatiserat i |
|---|---|---|
| En ny giltig kod ersätter den tidigare | Ja, testet kontrollerar kodens namn och procent | tests/api/test_ai_genererade.py::test_ny_giltig_rabattkod_ersatter_den_tidigare | 
| En okänd kod avvisas | Ja, 422 i stället för 400 | tests/api/test_ai_genererade.py::test_okand_rabattkod_avvisas | 
| Okänd e-post ger samma besked | Nej, rött när jag bröt det | tests/api/test_ai_genererade.py::test_okand_epost_ger_samma_besked_som_fel_losenord | 
