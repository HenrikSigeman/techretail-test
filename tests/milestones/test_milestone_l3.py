"""Milstolpe lektion 3 – kontrolleras med:  make milstolpe L=3

Att pipelinen är grön ser du på GitHub under fliken Actions. Här kontrolleras resten.
"""

import csv

import pytest

from tests.milestones.hjalp import ROOT, GIVEN_FIXTURES, collected, own_fixtures_used, run_pytest, section_words, summary

pytestmark = [pytest.mark.milestone, pytest.mark.milestone_l3]

CI = ROOT / ".github" / "workflows" / "ci.yml"


def test_l3_ci_kor_gui_testerna():
    text = CI.read_text(encoding="utf-8")
    missing = [part for part in ("playwright install", "scripts/shop.py start", "tests/gui") if part not in text.replace("# ", "#")
               or all(line.lstrip().startswith("#") for line in text.splitlines() if part in line)]
    assert not missing, f"TODO 1 i ci.yml är inte klar. Det saknas aktiva steg med: {', '.join(missing)}"


def test_l3_ci_sparar_testresultat():
    lines = [line for line in CI.read_text(encoding="utf-8").splitlines() if not line.lstrip().startswith("#")]
    assert any("actions/upload-artifact@v7" in line for line in lines), (
        "TODO 2 i ci.yml är inte klar: lägg till ett steg med actions/upload-artifact@v7 och if: always()."
    )
    assert not any("pip-install" in line or "@v4" in line for line in lines), "ci.yml innehåller gamla versioner (@v4 eller pip-install)."


def test_l3_minst_ett_smoke_test():
    smoke = collected("-m", "smoke", "tests")
    assert smoke, "Inget test är markerat med @pytest.mark.smoke (TODO 1 i tests/unit/test_beslutstabell.py)."


def test_l3_egen_fixture_anvands():
    used = own_fixtures_used()
    assert used, (
        "Hittar ingen egen fixture som används av ett test. Skriv en i tests/unit/conftest.py "
        f"(de givna räknas inte: {', '.join(sorted(GIVEN_FIXTURES))})."
    )


def test_l3_korttid_matt_fore_och_efter():
    file = ROOT / "docs" / "matningar.csv"
    assert file.exists(), "docs/matningar.csv saknas. Kör  make matning ETIKETT=fore  före din optimering."
    labels = [row["etikett"].lower() for row in csv.DictReader(file.open(encoding="utf-8"))]
    assert any(lbl.startswith(("fore", "före")) for lbl in labels), "Ingen mätning med etiketten fore. Kör  make matning ETIKETT=fore"
    assert any(lbl.startswith("efter") for lbl in labels), "Ingen mätning med etiketten efter. Kör  make matning ETIKETT=efter"


def test_l3_teststrategin_om_hallbarhet():
    words = section_words(6)
    assert words >= 30, f"Avsnitt 6 (Hållbarhet) i docs/teststrategi.md har {words} egna ord. Skriv minst 30: vad mätte du före och efter?"


def test_l3_alla_komponenttester_grona():
    result = run_pytest("tests/unit", "-q")
    assert result.returncode == 0, "Minst ett komponenttest fallerar.\n\n" + summary(result)
