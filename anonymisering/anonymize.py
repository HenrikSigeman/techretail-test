"""Anonymiseringsskriptet (lektion 5).

Mohammed Hassan (CISO) har sagt nej till att använda en export från produktionen som
testdata. Ditt skript gör om exporten så att den kan användas i testmiljön.

Begrepp (se kursens definitioner):
  pseudonymisering  identifierare byts mot en pseudonym med HMAC och en hemlig nyckel som
                    förvaras separat. Samma indata ger samma pseudonym. Fortfarande personuppgift.
  maskning          delar av ett värde döljs, här de fyra sista siffrorna i ett personnummer.
  syntetisk data    påhittad data med realistisk form (Faker, sv_SE).
  testpersonnummer  Skatteverkets testpersonnummer – de enda personnummer som får användas.

Kör:  make anonymisera
Nyckeln läses från miljövariabeln TECHRETAIL_HMAC_NYCKEL. Skriv den aldrig i koden eller i git.
    export TECHRETAIL_HMAC_NYCKEL="$(python -c 'import secrets; print(secrets.token_hex(32))')"
"""

from __future__ import annotations

import csv
import hashlib
import hmac
import os
import re
import sys
from pathlib import Path

from faker import Faker

HERE = Path(__file__).resolve().parent
TEST_PNR_FILE = HERE / "testpersonnummer.txt"

# Personnummer: ÅÅÅÅMMDD-NNNN, ÅÅMMDD-NNNN, med eller utan bindestreck (eller + för personer över 100 år).
PNR_PATTERN = re.compile(r"\b(\d{2})?(\d{6})([-+]?)(\d{4})\b")


# ------------------------------------------------------------------ givet

def luhn_ok(digits10: str) -> bool:
    """Kontrollsiffran (Luhn-algoritmen) på de tio sista siffrorna ÅÅMMDDNNNK."""
    if len(digits10) != 10 or not digits10.isdigit():
        return False
    total = 0
    for i, ch in enumerate(digits10):
        d = int(ch) * (2 if i % 2 == 0 else 1)
        total += d - 9 if d > 9 else d
    return total % 10 == 0


def load_test_personnummer() -> list[str]:
    """Skatteverkets testpersonnummer (12 siffror, utan bindestreck)."""
    lines = TEST_PNR_FILE.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def get_key() -> bytes:
    key = os.environ.get("TECHRETAIL_HMAC_NYCKEL", "")
    if len(key) < 32:
        raise SystemExit("Sätt miljövariabeln TECHRETAIL_HMAC_NYCKEL (minst 32 tecken). Se instruktionen överst i filen.")
    return key.encode()


# ------------------------------------------------------------------ din uppgift

def pseudonymize_email(email: str, key: bytes) -> str:
    normalized = email.strip().lower().encode() 
    digest = hmac.new(key, normalized, hashlib.sha256).hexdigest() 
    return f"kund-{digest[:16]}@example.com"


def mask_personnummer(text: str) -> str:
    def replace(match: re.Match) -> str: 
        century, date_part, sep, last4 = match.groups() 
        if not luhn_ok(date_part + last4): 
            return match.group(0) 
        return f"{century or ''}{date_part}{sep}****" 
 
    return PNR_PATTERN.sub(replace, text)


def synthetic_customer(fake: Faker, test_personnummer: list[str]) -> dict[str, str]:
    pnr = fake.random_element(test_personnummer) 
    return { 
        "namn": fake.name(), 
        "gatuadress": fake.street_address(), 
        "postnummer": fake.postcode(), 
        "ort": fake.city(), 
        "telefon": f"070-174 06 {fake.random_int(5, 99):02d}", 
        "personnummer": f"{pnr[:8]}-{pnr[8:]}", 
    } 


# ------------------------------------------------------------------ givet: hela flödet

def anonymize_rows(rows: list[dict[str, str]], key: bytes) -> list[dict[str, str]]:
    """Samma kund (samma e-post) får samma pseudonym och samma syntetiska uppgifter på alla rader."""
    test_pnr = load_test_personnummer()
    result = []
    for row in rows:
        pseudonym = pseudonymize_email(row["epost"], key)
        fake = Faker("sv_SE")
        fake.seed_instance(int(hashlib.sha256(pseudonym.encode()).hexdigest()[:12], 16))
        customer = synthetic_customer(fake, test_pnr)
        result.append({
            "ordernummer": row["ordernummer"],
            "kund_id": pseudonym,
            **customer,
            "kommentar": mask_personnummer(row["kommentar"]),
        })
    return result


def read_export(path: Path) -> list[dict[str, str]]:
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if not line.startswith("#")]
    return list(csv.DictReader(lines))


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Användning: python -m anonymisering.anonymize <indata.csv> <utdata.csv>")
        return 2
    source, target = Path(argv[0]), Path(argv[1])
    rows = anonymize_rows(read_export(source), get_key())
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as f:
        f.write("# ANONYMISERAD TESTDATA – genererad av anonymisering/anonymize.py\n")
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} rader anonymiserade -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
