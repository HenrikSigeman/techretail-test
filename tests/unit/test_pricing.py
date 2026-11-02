"""Komponenttester (enhetstester) för src/techretail/pricing.py – lektion 1.

De tre testerna som börjar med test_exempel_ är givna. Läs dem först.
Varje test följer AAA: Arrange (förbered) – Act (gör en sak) – Assert (kontrollera).
"""

import pytest

from techretail.pricing import apply_discount, shipping_cost


def test_exempel_10_procent_rabatt_drar_av_en_tiondel():
    # Arrange
    pris = 200
    # Act
    resultat = apply_discount(pris, 10)
    # Assert
    assert resultat == 180.0


def test_exempel_0_procent_rabatt_ger_samma_pris():
    # Arrange
    pris = 199.90
    # Act
    resultat = apply_discount(pris, 0)
    # Assert
    assert resultat == 199.90


def test_exempel_negativ_rabatt_ger_valueerror():
    # Arrange
    pris = 100
    # Act och Assert: pytest.raises kontrollerar att rätt fel uppstår
    with pytest.raises(ValueError):
        apply_discount(pris, -1)


# TODO (lektion 1): Skriv minst 5 egna tester här under.
#
# Regler för dina tester:
#   - Namnet ska börja med test_ men INTE med test_exempel_ (då räknas de inte).
#   - Ett test kontrollerar en sak. Använd AAA-kommentarerna som i exemplen.
#
# Använd gränsvärden och ekvivalensklasser. Förslag:
#   1. Gränsvärdet 100 procent: vad ska priset bli?
#   2. Strax över gränsen: 101 procent.
#   3. Avrundning till hela ören: 15 procent på 99,99 kr.
#   4. Frakt strax under gränsen: ordervärde 499,99 kr.
#   5. Frakt precis på gränsen: ordervärde 500 kr.
#
# Kör dina tester med:  uv run pytest tests/unit -v
# Kontrollera milstolpen med:  make milstolpe L=1
def test_100_procent_rabatt_ger_pris_noll(): 
    # Arrange 
    pris = 349 
    # Act 
    resultat = apply_discount(pris, 100) 
    # Assert 
    assert resultat == 0.0


def test_101_procent_rabatt_ger_valueerror(): 
    # Arrange 
    pris = 349 
    # Act och Assert 
    with pytest.raises(ValueError): 
        apply_discount(pris, 101) 


def test_15_procent_pa_99_99_avrundas_till_hela_oren(): 
    # Arrange 
    pris = 99.99 
    # Act 
    resultat = apply_discount(pris, 15) 
    # Assert 
    assert resultat == 84.99

def test_frakt_49_kr_strax_under_500(): 
    # Arrange 
    ordervarde = 499.99 
    # Act 
    frakt = shipping_cost(ordervarde) 
    # Assert 
    assert frakt == 49.0

def test_fri_frakt_precis_vid_500(): 
    # Arrange 
    ordervarde = 501 
    # Act 
    frakt = shipping_cost(ordervarde) 
    # Assert 
    assert frakt == 00.0 

def test_nollpris_ger_noll_efter_rabatt():
    # Arrange
    pris = 0

    # Act
    resultat = apply_discount(pris, 15)

    # Assert
    assert resultat == 0.0