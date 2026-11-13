"""Komponenttester (enhetstester) för src/techretail/pricing.py – lektion 1.

De tre testerna som börjar med test_exempel_ är givna. Läs dem först.
Varje test följer AAA: Arrange (förbered) – Act (gör en sak) – Assert (kontrollera).
"""

import pytest

from techretail.pricing import apply_discount, shipping_cost


@pytest.mark.smoke
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


# Lösning lektion 1: egna tester med gränsvärden och ekvivalensklasser.


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


def test_negativt_pris_ger_valueerror():
    # Arrange
    pris = -0.01
    # Act och Assert
    with pytest.raises(ValueError):
        apply_discount(pris, 10)


def test_rabatt_avrundas_till_hela_oren():
    # Arrange: 99,99 kr minus 15 % = 84,9915 kr, som avrundas till 84,99 kr
    pris = 99.99
    # Act
    resultat = apply_discount(pris, 15)
    # Assert
    assert resultat == 84.99


def test_exakt_halvt_ore_avrundas_uppat():
    # Arrange: 0,10 kr minus 25 % = 0,075 kr, som avrundas uppåt till 0,08 kr
    pris = 0.10
    # Act
    resultat = apply_discount(pris, 25)
    # Assert
    assert resultat == 0.08


def test_frakt_tas_ut_strax_under_gransen():
    # Arrange
    ordervarde = 499.99
    # Act
    frakt = shipping_cost(ordervarde)
    # Assert
    assert frakt == 49.0

@pytest.mark.smoke
def test_fri_frakt_precis_pa_gransen():
    # Arrange
    ordervarde = 500
    # Act
    frakt = shipping_cost(ordervarde)
    # Assert
    assert frakt == 0.0


@pytest.mark.parametrize("ordervarde, frakt", [(0, 49.0), (250, 49.0), (500.01, 0.0), (10_000, 0.0)])
def test_frakt_for_ekvivalensklasser(ordervarde, frakt):
    # Arrange: ordervarde och frakt kommer från parametriseringen
    # Act och Assert
    assert shipping_cost(ordervarde) == frakt
