"""Milstolpe lektion 4 – kontrolleras med:  make milstolpe L=4   (butiken måste vara igång)"""

import ast

import pytest

from tests.milestones.hjalp import ROOT, functions_with_marker, outcomes, own_tests, section_words

pytestmark = [pytest.mark.milestone, pytest.mark.milestone_l4]

MIN_OWN_API_TESTS = 6
NEGATIVE = {400, 401, 403, 404, 409, 422, 423}


def _own_api_files():
    return [p for p in (ROOT / "tests" / "api").glob("test_*.py") if p.name not in {"test_exempel_api.py", "test_orderhistorik.py"}]


def test_l4_minst_sex_egna_api_tester():
    own = [t for t in own_tests("tests/api") if "test_orderhistorik.py" not in t]
    assert len(own) >= MIN_OWN_API_TESTS + 1, (
        f"Du har {len(own)} egna API-tester. Det krävs minst {MIN_OWN_API_TESTS} plus IDOR-testet. Skriv dem i tests/api/test_api.py."
    )


def test_l4_minst_ett_negativt_fall():
    found = False
    for path in _own_api_files():
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.Constant) and node.value in NEGATIVE:
                found = True
    assert found, "Inget av dina API-tester kontrollerar en felkod (till exempel 401, 404, 409 eller 422)."


def test_l4_idor_test_markerat_som_kant_fel():
    marked = [name for p in _own_api_files() for name in functions_with_marker(p, "xfail")]
    assert marked, "Hittar inget IDOR-test markerat med @pytest.mark.xfail(strict=True, reason=\"IDOR: ...\")."
    text = "\n".join(p.read_text(encoding="utf-8") for p in _own_api_files())
    assert "strict=True" in text and "IDOR" in text, "xfail-markeringen ska ha strict=True och en reason som nämner IDOR."
    assert "1002" in text or "OTHER_USER" in text, "IDOR-testet ska försöka läsa en annan kunds order, till exempel 1002."


def test_l4_api_testerna_ger_ratt_utfall():
    results = {k: v for k, v in outcomes("tests/api").items() if "test_orderhistorik" not in k}
    failed = [k for k, v in results.items() if v in {"FAILED", "ERROR", "XPASS"}]
    assert results, "Inga API-tester kördes. Är butiken igång (make shop)?"
    assert not failed, "De här API-testerna gick fel: " + ", ".join(failed)
    assert "XFAIL" in results.values(), "IDOR-testet ska bli XFAIL (ett känt fel). Kör  make test-api  och titta."


def test_l4_teststrategin_om_testnivaer():
    words = section_words(3)
    assert words >= 40, f"Avsnitt 3 (Testnivåer och verktyg) i docs/teststrategi.md har {words} egna ord. Skriv minst 40."
