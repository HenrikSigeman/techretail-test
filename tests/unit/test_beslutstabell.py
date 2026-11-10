"""Beslutstabell för frakt och rabatt – givet exempel för lektion 3.

En beslutstabell listar alla kombinationer av villkor och vad som ska hända.
Varje kolumn (regel) blir ett testfall. Med pytest.mark.parametrize blir
tabellen ett enda test med fyra fall.

| Regel                          | R1  | R2  | R3  | R4  |
|--------------------------------|-----|-----|-----|-----|
| Rabatt används?                | Nej | Nej | Ja  | Ja  |
| Belopp efter rabatt >= 500 kr? | Nej | Ja  | Nej | Ja  |
| Frakt 49 kr?                   | Ja  | Nej | Ja  | Nej |
"""

import pytest

from techretail.pricing import apply_discount, shipping_cost


def att_betala(delsumma: float, rabatt_procent: float) -> float:
    efter_rabatt = apply_discount(delsumma, rabatt_procent)
    return round(efter_rabatt + shipping_cost(efter_rabatt), 2)


@pytest.mark.parametrize(
    "delsumma, rabatt_procent, forvantat",
    [
        pytest.param(400, 0, 449.0, id="R1-ingen-rabatt-under-500-ger-frakt"),
        pytest.param(600, 0, 600.0, id="R2-ingen-rabatt-over-500-fri-frakt"),
        pytest.param(550, 10, 544.0, id="R3-rabatten-tar-beloppet-under-500-ger-frakt"),
        pytest.param(1000, 10, 900.0, id="R4-rabatt-och-fortfarande-over-500-fri-frakt"),
    ],
)
def test_exempel_beslutstabell_att_betala(delsumma, rabatt_procent, forvantat):
    assert att_betala(delsumma, rabatt_procent) == forvantat


# TODO 1 (lektion 3): Markera minst ett av dina snabba tester med @pytest.mark.smoke.
#   Kör sedan bara röktesterna:  uv run pytest -m smoke
#
# TODO 2 (lektion 3): Skriv en egen fixture i tests/unit/conftest.py och använd den i minst ett test.
#   Exempel på idé: en fixture som returnerar en lista med rabattkoder och procentsatser.
