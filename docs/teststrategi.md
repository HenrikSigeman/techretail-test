# Teststrategi för TechRetail AB

> Den här filen är en del av inlämningen. Du fyller på den under kursen – börja i lektion 1 och skriv klart i lektion 9.
> Skriv kort och konkret. Motivera dina val med TechRetails situation, inte med allmänna påståenden.

**Författare:** Henrik Sigeman
**Senast uppdaterad:** 2026-11-02

## 1. Nuläge och mognad

*Hur testar TechRetail AB i dag? Var ligger företaget i kursens mognadsmodell (Strategi och styrning, Verktyg och arkitektur, Kompetens och organisation, Process och CI/CD, Mätning och resultat), och vilken nivå siktar ni på?*
| Dimension | Nivå | Bevis och motivering | 
|---|---|---| 
| Strategi och styrning | 1 |Ingen gemensam teststrategi, personberoende.| 
| Verktyg och arkitektur | 1 | Saknas gemensam teststrategi och verktyg.| 
| Kompetens och organisation | 2 | finns viss kompetens, speciellt hos Karin | 
| Process och CI/CD | 1 | Inga tester körs när koden ändras. Regressionen görs för hand | 
| Mätning och resultat | 1 | Ingen följer upp resultat, finns krav från ledningen som vi inte vet om de följs upp, vet bara att Karins svit hittar fel| 

 

Målnivå: 3. Störst kulturell risk: Tid och förväntningar. Konkret förslag: Avsätt lite tid (med utvecklarna) i varje spring för att utveckla automation.
## 2. Vad automatiseras och vad inte

*Bedöm automationskandidater med kriterierna frekvens, stabilitet, risk, determinism, kostnad att underhålla och värde av snabb återkoppling. Klassa varje fall i Karins manuella regressionssvit (MT-01 – MT-25) som ersätts, kompletteras eller behålls manuellt, och motivera.*

| Testfall | Klass (ersätts / kompletteras / behålls manuellt) | Nivå | Motivering |
|---|---|---|---|
| MT-01 | Ersätts | GUI, API | Den viktigaste sekundära funktionen för webbsidan/webbshoppen. Kunder måste kunna logga in genom hemsidan, så därför är testet uppdelat dels med front-end, och dels med kommunikationen till servern (API) |
| MT-03 | Ersätts | API | Ett spärrat konto ska inte kunna logga in och försöket bör hanteras och testas genom vårat API. Det behövs också ingen mänsklig mellanhand utan funktionen kan testas automatiskt med ett testkonto. |
| MT-06 | Ersätts | API | Filtrering är en viktig funktion för en sida som säljer produkter. Kan ersättas helt och hållet med automatiska tester då, även om våra produkter ändras, så kommer det alltid att förväntas samma resultat: att alla produkter som hämtas har kategorin "El och belysning", och att produkterna ska kosta mellan 100 kr och 300 kr. För att säkerställa korrekt information bör också den hämtade listan jämföras med den kompletta listan av produkter så att inte någon produkt med rätt kategori och pris inte kommit med. |
| MT-08 | GUI | Ersätts | Ännu en viktig komponent vid online-shopping. Då all information relevant till en persons kundvagn sker lokalt så behövs det ingen test av APIet eller vår back-end. Resultatet är också enkelt och tydligt och kan därför automatiseras helt och hållet. |
| MT-11 | Ersätts | GUI, API | Ett anrop sker från kundvagnen för att hämta rabattkoden och applicerar sedan rabatten på det slutgiltiga priset. Då det är samma varor varje gång bör testet ske automatiskt (så länge inte priserna ändras eller är del av en annan kampanj). |
| MT-13 | Ersätts | Komponent | Behöver egentligen bara kontrollera en enda funktion. |
| MT-14 | Kompletteras | GUI, API | Fallet är egentligen uppdelat i två delar: funktionaliteten och upplevelsen. Funktionaliteten kan testas automatiskt, medan hurvida betalningen upplevdes "smidig" behöver en riktig människa ta ställning till. |
| MT-19 | Behålls manuellt | GUI | Då detta test delvis inte sker regelbundet (såvida kampanjer inte följer varandra) så kan detta test fortfarande vara manuellt. Dessutom så är det bättre om en människa bedömer utseendet och hurvida bannern är läsbar på de olika operativsystemen. |
| MT-20 | Behålls manuellt | GUI, API | Dåligt definierat test och behöver skrivas om för att tydligare sätta upp mål, tillvägagångssätt, teststeg och förväntade resultat. I sin nuvarande form kan bara en människa utföra testet. |
| MT-22 | Behålls manuellt | ??? | Ospecifierat test med osäker struktur. Behöver dock bara göras en gång så det finns ingen poäng med att automatisera. |

# Fördjupning 1

| Testfall | Kriterium | Kostnad | Hur Karin gör idag |
|---|---|---|---|
| MT-22 | Frekvens. Idag så beskrivs testfallet som att det bara ska ske en gång totalt. Vid sådana fall så är det uppenbart att det hade kostat mer att automatisera testet framför att göra det manuellt. Vi kan med ganska stor säkerthet utgå ifrån att i detta fall så hade automatisering tagit längre tid än att utföra testet manuellt. Om situationen skulle förrändras, till exempel om ledningen bestämmer att jämförelsen ska ske med jämna mellanrum, eller om samma test förväntas att utföras någon gång i framtiden, om det planeras ännu en flytt av databas, eller att "versioner" av katalogen förväntas förändras så att resultatet inte är lika självklart. | Att skriva ett jämförelsetest är ganska simpelt i teorin, men kan påverkas av hur man hämtar datan att jämföra. | Idag gör Karin testet manuellt, och att den tar 60 minuter att utföra gör den till en kandidat för automatisering, om det inte var så att testet bara behöver köras en enda gång. |
| MT-19 | Determinism. Då det delvis handlar om grafisk utformning och att varje kampanj förväntas ha en unik banner och textinnehåll så är det starkaste argumentet emot automatisering att det i slutändan skulle behövas en människas omdöme för att säga om en kampanjbanner ser bra ut eller inte, att texten går att läsa och att bilden inte är beskuren. Då testet bara behöver göras en gång i relation till en kampanj så finns det inte heller en koppling till kriterium Frekvens och Värde av snabb återkoppling | Utöver att testa så att relevanta filer, text och länkar skrivs ut korrekt så hade det krävts ett ganska sofistikerat bildanalysprogram för att granska den grafiska komponenten och göra en tillgänglighetsbedömning där den jämför textens färg med färgen i bakgrunden, att fonten är tillräckligt stor och tydlig etc. Att utveckla ett sådant program är dyrt och onödigt i detta fall då en människa kan göra bedömningen på ett ögonblick (med viss förberedelse i form av lista på kriterier). Om bannern "ser bra ut" är mycket mer komplicerat och kan (bör) bedömas av en människa. | Idag så testar Karin genom att öppna startsidan på både iPhone och Android, och testet förväntas ta 15, och bara utförs en gång varje kampanj. |

# Fördjupning 2
| Testfall | Klass (ersätts / kompletteras / behålls manuellt) | Nivå | Motivering |
|---|---|---|---|
| MT-02 | ersätts | GUI och API | Felmeddelandet visas mot användaren och funktionen måste därför kollas ifrån GUI-nivån, samtidigt så ska funktionen för att faktiskt få fram det meddelandet testas, och det sker genom anrop mot vår API. |
| MT-12 | ersätts | API | Då anropandet av rabattkoderna sker systematiskt med tydligt definierade svar så kan testning ske automatiskt direkt mot vårat API. |
| MT-16 | ersätts | GUI (API) | Testningen sker på själva hemsidan och direkt mot användaren, därför bör testet uföras på GUI-nivå. Så som jag hade gjort hemsidan så hade inte kundvagnen sparats på server-nivå utan istället lokalt på användarens dator, och då bör man självklart inte kunna se en annan användares kundvagn (I de fall då kundvagnen hade sparats på servern så hade det passat bättre med API, då användarens ID kontrolleras mot kundvagnens relaterade kund-ID så att bara den användare med samma ID som den hos kundvagnen kan hämta den.)
| MT-21 | kompletteras | API | Test kan först ske automatiskt (köp, sedan kontroll), bör också kompletteras med en människa då man kan med fördel testa saker som berör användare och spårbarheten |
| MT-24 | kompletteras | GUI | Kan både testas med hjälp av automatiserat test i chattfönstret (eller direkt mot chattbotten), en människa bör också med jämna mellanrum kontrollera så att chattbotten faktiskt säger det den ska och att det stämmer överens med manualen.

| Manuellt fall | Krav | Automatiserat test|
|---|---|---|
| MT-11 | ?? | tests/unit/test_pricing.py och test_dra_av_10_procent_med_rabattkod_TECH10 |
| MT-13 | ?? | tests/unit/test_pricing.py och test_frakt_49_kr_strax_under_500, test_fri_frakt_precis_vid_500 |

# Nästa steg i mognad
Steg 1. Karin och en utvecklare bör gemensamt arbeta ihop för att skriva ett eller fler automatiska tester. Karin kan dela med sig av sin expertis genom att förklara steg-för-steg hur testerna utförs, och utvecklaren kan översätta stegen till kod. Anna kommer senare att se att tester och resultat börjar att rulla in.
Steg 2. Röda tester måste dokumenteras och följas upp, gärna samma dag och av den personen som gjort ändring så att testet blir rött. Istället för att en person testar och löser problemen så blir det istället ett gemensamt ägande. Anna kommer att se att röda tester rättas snabbt.

Inledningsvis kommer kostnaden att vara ganska hög. Tid kommer att gå ifrån att utveckla till att testa och fixa, och att dokumentera, men nyttan blir att det blir mindre technical debt, kunskapen sprids i utvecklarteamet och man blir mindre beroende av en person som kan allt.

## 3. Testnivåer och verktyg

*Hur fördelar du testerna på testpyramidens nivåer komponent (enhet), API och GUI? Ge exempel ur ditt eget repo för varje nivå. Vilka verktyg använder du, och vad körs vid varje push respektive nattligt?*
| Nivå | Exempel i mitt repo | Verktyg | 
|---|---|---| 
| Komponent | tests/unit/test_pricing.py | pytest | 
| API | (lektion 4) | | 
| GUI | tests/gui/test_produkt.py | Playwright med Page Objects | 
Verktyg för GUI-tester: Playwright. De mest relevanta föredelarna med Playwright over Selenium var i ämnena Väntan och Stabilitet (sparar oss mycket tid och frustration om vi använder ett verktyg som aktivt lyssnar efter att elementen laddats in klart framför att behöva vänta en satt tid.), och Felsökning (Playwrights Trace-funktion är mer detaljerad och lättläst snarare än loggar som Selenium använder.) Selenium har vissa fördelar när det kommer till kriteriet "Webbläsare och enheter" eftersom att den tillåter att man testar riktiga mobiler med hjälp av Appium.
Fall som testas i webbläsaren: MT-01, MT-04, MT-08, MT-11, MT-25. MT-13 är ett komponenttest.
Kvar för Karin: Karin behöver göra GUI-testerna på Android och iPhone eftersom att Playwright inte täcker dessa.


Vad i utkastet går sönder först om butiken ändras, och vad händer om tjugo tester är skrivna såhär?
Svar: Testet "test_example" är inte bra implementerat av flera anledningar och vi bör inte använda den som en mall för att skriva fler tester just nu. För tillfället är det största problemet att adressen till webbsidan är hårdkodad, och utifall att vi ändrar namnen på våra produktsidor (idag "produkter") så kommer vi att behöva skriva om alla test för hand för att reflektera denna ändring så att testen kan köras. Om vi till exempel har 20 tester som är uppbyggda på detta sätt med direkt hårdkodad adress så kommer de alla att behöva ändras för hand om vi ändrar hur man navigerar på webbsidan. Den enda fördelen är att vi kan, genom att hårdkoda adressen, få bättre läsbarhet och att det kan vara snabbare att skriva utifall att det rör sig om ett testplats som vi inte har implementerat i något Page Object än. Men nackdelarna väger fortfarande tyngre än fördelarna.

Vad gör ditt Page Object bättre, och vad koster det att ha det?
Svar: Med hjälp av mitt Page Object så behöver vi bara ändra på en enda plats utifall navigationen på webbsidan ändras. Alla adresser som pekar mot produktsidor bör komma ifrån product_page.py, så det är där som koden för att navigera, och interagera med sidan bör ligga. Detta gäller inte bara för navigering, utan vi kan också skapa referenser till olika element på sidan, exempelvis kvantitets-fältet och "lägg till i kundvagn"-knappen, så att vi i tester kan referera till dessa variabler som tillhör Page Object:et istället för att skriva referenser för hand (som kan innehålla stavfel och vara känsliga för förändringar). Kostnaden är såklart att vi behöver lägga tid för att göra variabler för alla element som vi vill använda. Enkla sidor med varningstext behöver inte någon detaljerat Page Object, men sidor som produktsidan där det finns flera stycken intressanta element är en mycket stark kandidat för att utformas på detta sätt. Den initiala kostnaden är såklart högre än att skriva testen manuellt som i exemplet, då tid lägs på annat än att skriva de faktiska testerna, men man tjänar på att ha det utifall följande är sann: tid för att skapa Page Object + tid för att ändra Page Object när butiken ändras < (tid för att implementera test med codegen * antalet tester) + (tid för att ändra codegen-skrivna tester när butiken ändras * antalet tester).

När är codegen ändå värt att använda?
Svar: Codegen är bättre för att göra många, små och utforskande tester. Temporära tester som sedan ska tas bort eller dylikt. Codegen kan hjälpa oss att skriva grunden för tester på ett intuitivt sätt, precis som våra användare gör, genom att skriva, klicka och navigera på vår webbsida. Codegen genererar stegen, som vi sedan kan skriva om till "riktiga" tester med hjälp av Page Object, och det kan i vissa fall gå mycket snabbare att göra det på detta sätt, speciellt om det krävs många steg som kan vara svårt för en utvecklare att ha koll på i huvudet, och det gör också att inte steg hoppas över lika lätt, som det hade kunnat göras om man skrev testen för hand från början.

Fördjupningskort:
Lista på Page Objects:
login_page, home_page, product_list_page, product_page, page_header

Lokaliserare:
login_page:
    page.get_by_role("input", name="email")
    page.get_by_test_id("login-button")

    Skör lokaliserare:
        page.get_by_text("Logga in")
            Anledning: Att leta efter en knapp med hjälp av dess text är i många fall tillräckligt, men om texten av någon anledning kommer att ändras så kommer testet inte längre att fungera.

product_list_page:
    page.get_by_test("search-input")
    page.get_by_test_id("result-count")

    Skör lokaliserare:
        page.get_by_text("9 produkter")
            Anledning: Det är ett för föränderligt attribut. Beroende på innehållet på sidan så kan det finnas väldigt många olika antal produkter, så att söka på en attribut efter texten "10 produkter" kan i många fall leda till misslyckade lokaliseringar. Speciellt eftersom att när sidan öppnas så står det "10 produkter" istället för 9.

product_page:
    page.get_by_label("Antal")
    page.get_by_test_id("product-price")

    skör lokaliserare:
        page.get_by_text("129,00 kr")
            Anledning: Om produkten på sidan inte kostar exakt 129,00 kr och har det i "product-price" fältet så kommer inte elementet att hittas

page_header:
    page.get_by_test_id("login-link")
    page.get_by_test_id("cart-link")

    skör lokaliserare:
        page.locator("Xpath=//logga-in)
            Anledning: Från lösningsförslaget "En XPath genom sidhuvudets delar går sönder när menyn byggs om"

MT-25 i ord:
Arrange:
    Skapa Page Object product_page för produktsidan Multiverktyg 300W genom open(n)

Act:
    hämta "lägg-i-kundvagnen"-knappen, och kör ".click()" på den.

Assert:
    expect att "lägg-i-kundvagnen" ska vara disabled.
    expect_cart_count ska vara 0
    Elementet associerat med test_id "stock-status" ska ha texten "Slut i lager".

Vad kostar GUI-testerna:
    GUI-tester kostar i regel mycket mer tid än att bara köra komponenttester, därför bör inte alla våra testfall också innehålla GUI-tester om det inte är explicit motiverat.
    
    Rimligtvis bör MT-4 göras en gång som ett GUI-test för att se att webbsidan agerar som förväntat och visar rätt resultet, men om man vill göra många tester mot själva sök-systemet bör de göras som API-tester fortsättningsvis.

    Test för olika felinloggningar kan göras med hjälp av API-tester. Man behöver bara göra ett GUI-test i dessa fall då vi redan känner till resultatet från login-anropet vid fel, och GUI-t förväntas reagera på samma sätt oavsett vilken permutation som skapar felet.

Det vi vinner på detta är snabbare tester och snabbare återkoppling. Vi kan göra fler tester under kortare tid, testa bredare utan att påverka testtiderna speciellt mycket. GUI-test behövs fortfarande för att kontrollera att GUI-t agerar som förväntat, då API-tester förbipasserar webbgränssnittet och gör direkta anrop till våran kod utan att involvera front-end:en.




## 4. AI-användning

*Hur använder du AI för att ta fram och förbättra tester? Hur granskar du resultatet med GRANSKA-kortet? Hänvisa till poster i `ai/AI-logg.md`.*

## 5. Icke-funktionella tester – prestanda och säkerhet

*Vilken prestandabudget gäller (till exempel p95 och felandel), och hur kontrollerar du den? Vilka säkerhetsrisker testar du, och med vilka verktyg?*

## 6. Hållbarhet – mätning före och efter

*Vilken resursbesparande åtgärd har du gjort (till exempel kortare körtid, färre CI-minuter, smartare testurval)? Vad visade mätningen före och efter? Vad kostade AI-användningen?*

Förslag: vid varje push kör vi endast röktesterna, och hela sviten körs nattligt och före release. 
Före: hela sviten tog 9,34 sekunder lokalt (29 tester). 
Efter: röktesterna tog 1,01 sekunder lokalt (3 tester). 
Pipelinen på GitHub tog 34 sekunder. 
Risk: ett fel som endast GUI-testerna hittar syns först i nattkörningen. Med snabbare pipeline så kan också Rebound-effekten uppstå, så att utvecklare pushar fler committs och oftare och potentiellt gör att vi använder fler CI-minuter än innan uppdelningen. 
