"""Komponenttester för anonymiseringsskriptet (lektion 5).

Fixturerna och de två exempeltesterna är givna. Skriv dina egna tester under TODO.
"""

import pytest

from anonymisering.anonymize import load_test_personnummer, luhn_ok


@pytest.fixture
def testpersonnummer() -> list[str]:
    """Skatteverkets testpersonnummer (12 siffror). Använd dem när ett test behöver ett giltigt personnummer."""
    return load_test_personnummer()


@pytest.fixture
def hmac_nyckel() -> bytes:
    """En nyckel som bara används i testerna. Den riktiga nyckeln finns i en miljövariabel."""
    return b"testnyckel-som-bara-finns-i-testerna-0123456789"


def test_exempel_alla_testpersonnummer_klarar_luhn(testpersonnummer):
    assert testpersonnummer, "Listan med testpersonnummer är tom"
    assert all(luhn_ok(pnr[2:]) for pnr in testpersonnummer)


def test_exempel_luhn_avvisar_fel_kontrollsiffra(testpersonnummer):
    pnr = testpersonnummer[0][2:]
    fel = pnr[:9] + str((int(pnr[9]) + 1) % 10)
    assert luhn_ok(fel) is False


# TODO (lektion 5): Skriv minst 3 egna tester, ett för varje funktion du implementerar.
# Förslag:
#   - samma e-post ger samma pseudonym, och en annan nyckel ger en annan pseudonym
#   - mask_personnummer maskerar ett testpersonnummer men lämnar ett kollinummer som inte klarar Luhn
#   - synthetic_customer ger ett personnummer som finns i fixturen testpersonnummer
