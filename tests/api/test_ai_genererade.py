"""API-tester för rabattkoder och inloggning (TR-13 och TR-03).""" 
 
import pytest 
 
 
@pytest.mark.ai_genererad 
def test_ny_giltig_rabattkod_ersatter_den_tidigare(logged_in_api_client): 
    # Arrange 
    logged_in_api_client.add_to_cart(4, quantity=10) 
    logged_in_api_client.apply_discount("TECH10") 
    # Act 
    response = logged_in_api_client.apply_discount("VINTER15")
    # Assert 
    assert response.status_code == 200
    kundvagn = response.json() 
    assert kundvagn["discount_code"] == "VINTER15" 
    assert kundvagn["discount_percent"] == 15 

@pytest.mark.ai_genererad 
def test_okand_rabattkod_avvisas(logged_in_api_client): 
    # Act 
    response = logged_in_api_client.apply_discount("FINNSINTE") 
    # Assert 
    assert response.status_code == 422 
    assert response.json()["detail"] == "Rabattkoden är ogiltig eller har gått ut." 
 
 
@pytest.mark.ai_genererad 
def test_okand_epost_ger_samma_besked_som_fel_losenord(api_client): 
    # Act 
    response = api_client.login("finns.inte@example.com", "Test1234!") 
    # Assert 
    assert response.status_code == 401 
    assert response.json()["detail"] == "Fel e-post eller lösenord."