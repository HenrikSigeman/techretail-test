"""Milstolpe lektion 5 – kontrolleras med:  make milstolpe L=5"""

import re

import pytest

from tests.milestones.hjalp import ROOT, ai_log_posts, own_tests, outcomes, own_words, section_words, summary, run_pytest

pytestmark = [pytest.mark.milestone, pytest.mark.milestone_l5]

KEY = b"milstolpe-nyckel-0123456789abcdef0123456789"


def _module():
    from anonymisering import anonymize

    return anonymize


def test_l5_pseudonymisering_med_hmac():
    a = _module()
    p1 = a.pseudonymize_email("Kim.Kund@Example.com ", KEY)
    assert p1 == a.pseudonymize_email("kim.kund@example.com", KEY), "Samma e-post (oavsett versaler och mellanslag) ska ge samma pseudonym."
    assert p1 != a.pseudonymize_email("kim.kund@example.com", KEY + b"x"), "En annan nyckel ska ge en annan pseudonym."
    assert re.fullmatch(r"kund-[0-9a-f]{16}@example\.com", p1), f"Formatet ska vara kund-<16 hex>@example.com, fick {p1}"
    assert "kim" not in p1.lower(), "Pseudonymen får inte innehålla delar av den riktiga adressen."


def test_l5_maskning_av_personnummer_med_luhn():
    a = _module()
    pnr = a.load_test_personnummer()[3]
    long_form, short_form = f"{pnr[:8]}-{pnr[8:]}", f"{pnr[2:8]}-{pnr[8:]}"
    assert a.mask_personnummer(f"Ring {long_form} i dag") == f"Ring {pnr[:8]}-**** i dag"
    assert a.mask_personnummer(f"Kund {short_form}.") == f"Kund {pnr[2:8]}-****."
    assert a.mask_personnummer(f"pnr {pnr}") == f"pnr {pnr[:8]}****", "Personnummer utan bindestreck ska också maskeras."
    not_pnr = "1234567890"
    assert not a.luhn_ok(not_pnr)
    assert a.mask_personnummer(f"Kolli {not_pnr}") == f"Kolli {not_pnr}", "Tal som inte klarar Luhn ska lämnas orörda."


def test_l5_syntetisk_kund():
    from faker import Faker

    a = _module()
    test_pnr = a.load_test_personnummer()
    customer = a.synthetic_customer(Faker("sv_SE"), test_pnr)
    assert {"namn", "gatuadress", "postnummer", "ort", "telefon", "personnummer"} <= set(customer)
    assert customer["personnummer"].replace("-", "") in test_pnr, "Personnumret ska komma ur Skatteverkets testpersonnummer."
    assert customer["telefon"].startswith("070-174 06"), "Telefonnumret ska ligga i PTS-serien för fiktiv användning."


def test_l5_hela_exporten_ar_anonymiserad():
    a = _module()
    source = a.read_export(ROOT / "anonymisering" / "data" / "kundexport_syntetisk.csv")
    result = a.anonymize_rows(source, KEY)
    assert len(result) == len(source)
    text = "\n".join(",".join(r.values()) for r in result)
    for row in source:
        assert row["epost"] not in text, f"E-postadressen {row['epost']} finns kvar."
        assert row["namn"] not in text, f"Namnet {row['namn']} finns kvar."
        assert row["personnummer"] not in text, "Ett personnummer från exporten finns kvar."
    by_email = {}
    for src, out in zip(source, result):
        by_email.setdefault(src["epost"], set()).add(out["kund_id"])
    assert all(len(ids) == 1 for ids in by_email.values()), "Samma kund ska få samma kund_id på alla rader."


def test_l5_egna_tester_for_anonymiseringen():
    own = own_tests("tests/unit/test_anonymisering.py")
    assert len(own) >= 3, f"Du har {len(own)} egna tester i tests/unit/test_anonymisering.py. Minst 3 krävs."
    result = run_pytest("tests/unit/test_anonymisering.py", "-q")
    assert result.returncode == 0, summary(result)


def test_l5_tre_ai_genererade_tester_grona():
    ids = [line for line in run_pytest("--collect-only", "-q", "-m", "ai_genererad", "tests").stdout.splitlines() if "::" in line]
    assert len(ids) >= 3, f"Hittar {len(ids)} tester markerade @pytest.mark.ai_genererad. Minst 3 krävs."
    results = outcomes("-m", "ai_genererad", "tests")
    bad = [k for k, v in results.items() if v not in {"PASSED", "XFAIL"}]
    assert not bad, "De AI-genererade testerna ska vara gröna efter din granskning: " + ", ".join(bad)


def test_l5_ai_loggen_har_tre_poster():
    posts = ai_log_posts()
    assert len(posts) >= 3, f"ai/AI-logg.md har {len(posts)} egna poster under 'Mina poster'. Minst 3 krävs (en per granskat AI-test)."


def test_l5_scenarier_fran_krav():
    text = (ROOT / "docs" / "scenarier.md").read_text(encoding="utf-8")
    mine = text.split("## Mina scenarier", 1)[-1]
    assert len(re.findall(r"^\s*Scenario:", mine, re.M)) >= 3, "Skriv minst 3 scenarier under 'Mina scenarier' i docs/scenarier.md."
    assert re.search(r"TR-\d\d", mine), "Ange kravens ID (TR-xx) ovanför scenarierna."
    assert own_words("docs/scenarier.md") >= 80, "Fyll i granskningsdelen i docs/scenarier.md."


def test_l5_teststrategin_om_ai():
    words = section_words(4)
    assert words >= 40, f"Avsnitt 4 (AI-användning) i docs/teststrategi.md har {words} egna ord. Skriv minst 40."
