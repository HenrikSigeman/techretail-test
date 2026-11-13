"""Fixtures för komponenttesterna (lektion 3).""" 
 
import pytest 
 
 
@pytest.fixture 
def rabattkoder(): 
    """Kursens aktiva rabattkoder och deras procentsatser.""" 
    return {"TECH10": 10, "VINTER15": 15}

