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

## 4. AI-användning

*Hur använder du AI för att ta fram och förbättra tester? Hur granskar du resultatet med GRANSKA-kortet? Hänvisa till poster i `ai/AI-logg.md`.*

## 5. Icke-funktionella tester – prestanda och säkerhet

*Vilken prestandabudget gäller (till exempel p95 och felandel), och hur kontrollerar du den? Vilka säkerhetsrisker testar du, och med vilka verktyg?*

## 6. Hållbarhet – mätning före och efter

*Vilken resursbesparande åtgärd har du gjort (till exempel kortare körtid, färre CI-minuter, smartare testurval)? Vad visade mätningen före och efter? Vad kostade AI-användningen?*
