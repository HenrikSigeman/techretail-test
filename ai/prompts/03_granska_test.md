# Prompt: be AI:n granska ett test

AI:n kan hjälpa till att granska, men beslutet är ditt. Kör alltid steget Bryt själv.

---

Granska testet nedan som en erfaren testautomatiserare. Leta särskilt efter:
- fasta väntetider, sköra lokaliserare (XPath, långa CSS-kedjor)
- assertioner som inte kontrollerar något väsentligt (bara statuskod, eller inget alls)
- try/except som sväljer fel
- testdata som inte ägs av testet, eller persondata
- funktioner som inte finns i systemet

Svara med en lista: problem, varför det är ett problem, förslag på rättning.

[Klistra in testet]
