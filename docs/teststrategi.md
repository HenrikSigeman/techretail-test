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

## 3. Testnivåer och verktyg

*Hur fördelar du testerna på testpyramidens nivåer komponent (enhet), API och GUI? Ge exempel ur ditt eget repo för varje nivå. Vilka verktyg använder du, och vad körs vid varje push respektive nattligt?*

## 4. AI-användning

*Hur använder du AI för att ta fram och förbättra tester? Hur granskar du resultatet med GRANSKA-kortet? Hänvisa till poster i `ai/AI-logg.md`.*

## 5. Icke-funktionella tester – prestanda och säkerhet

*Vilken prestandabudget gäller (till exempel p95 och felandel), och hur kontrollerar du den? Vilka säkerhetsrisker testar du, och med vilka verktyg?*

## 6. Hållbarhet – mätning före och efter

*Vilken resursbesparande åtgärd har du gjort (till exempel kortare körtid, färre CI-minuter, smartare testurval)? Vad visade mätningen före och efter? Vad kostade AI-användningen?*
