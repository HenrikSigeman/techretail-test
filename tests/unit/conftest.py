"""Fixtures för komponenttesterna (lektion 3).

En fixture förbereder något som flera tester behöver (Arrange). Testet ber om
fixturen genom att ha samma namn som parameter.

TODO (lektion 3): Skriv minst en egen fixture här och använd den i ett test.

    import pytest

    @pytest.fixture
    def rabattkoder():
        return {"TECH10": 10, "VINTER15": 15}

    # I ett test:  def test_tech10_ger_tio_procent(rabattkoder): ...
"""
