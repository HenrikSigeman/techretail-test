"""Tester som använder fixturen rabattkoder (lektion 3).""" 
 
import pytest 
 
from techretail.pricing import apply_discount 
 

@pytest.mark.smoke 
def test_tech10_pa_199_90_kr_drar_av_tio_procent(rabattkoder): 
    # Arrange 
    procent = rabattkoder["TECH10"] 
    # Act 
    resultat = apply_discount(199.90, procent)
    199.90 - 19.99
    # Assert 
    assert resultat == 179.91