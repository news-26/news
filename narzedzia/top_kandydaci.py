#!/usr/bin/env python3
"""Zwięzły materiał do Top 10 – zamiast czytania całych wydań (oszczędność tokenów).

Użycie:
    python3 narzedzia/top_kandydaci.py                 # zestawienie kroczące: okno 30 dni do ostatniego wydania
    python3 narzedzia/top_kandydaci.py --miesiac 2026-10   # archiwum: pełny miesiąc kalendarzowy
    --wszystkie   pokaż wszystkie niecytowane pozycje z okresu (domyślnie, gdy zestawienie już istnieje,
                  tylko z wydań po jego ostatniej aktualizacji – reszta była już rozważona)

Drukuje: okres, obecne pozycje zestawienia (kroczącego albo za miesiąc, jeśli plik już jest) z datą ostatniego
wiersza przebiegu, oraz pozycje wydań dziennych z okresu, których zestawienie jeszcze nie cytuje
(id w formacie RRRR-MM-DD#id, data zdarzenia, hashtagi, początek tekstu). Nowe wydania od ostatniej aktualizacji
są oznaczone gwiazdką.
"""
import argparse
import calendar
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--miesiac", help="RRRR-MM – zestawienie archiwalne za ten miesiąc")
    ap.add_argument("--wszystkie", action="store_true")
    a = ap.parse_args()
    dane = B.REPO / "dane"
    tagi, osoby, pojecia, wydania, rewizje, topy = B.wczytaj(dane)
    dzienne = [w for w in wydania if w.get("typ", "dzienne") == "dzienne"]
    if not dzienne:
        sys.exit("Brak wydań dziennych.")

    if a.miesiac:
        r, m = map(int, a.miesiac.split("-"))
        od = dt.date(r, m, 1)
        do = dt.date(r, m, calendar.monthrange(r, m)[1])
        plik = dane / "top" / f"{od.isoformat()}_{do.isoformat()}.json"
    else:
        do = B.data_(dzienne[-1]["data"])
        od = do - dt.timedelta(days=B.TOP_OKNO_DNI - 1)
        plik = dane / "top" / f"{B.TOP_KROCZACE}.json"

    print(f"Okres: {od.isoformat()} – {do.isoformat()}  ->  {plik.relative_to(B.REPO)}")
    obecne = json.loads(plik.read_text("utf-8")) if plik.exists() else None
    ostatnio = obecne.get("do", "") if obecne else ""
    cytowane = set()
    if obecne:
        print(f"\nObecne zestawienie (od {obecne.get('od')} do {obecne.get('do')}, stan {obecne.get('opublikowano')}):")
        for n, p in enumerate(obecne.get("pozycje", []), 1):
            daty = sorted(x["data"] for x in p.get("przebieg", []))
            w_oknie = any(d >= od.isoformat() for d in daty)
            print(f"  {n}. [{p['id']}] {p['tytul']} | ostatni fakt {daty[-1] if daty else '—'}"
                  + ("" if w_oknie else "  <-- POZA OKNEM: usuń albo dopisz nowy fakt"))
            cytowane.update(p.get("w_wydaniach", []))
    else:
        print("\nZestawienia jeszcze nie ma – utwórz plik.")

    archiwum = [z for z in topy if not z.get("_kroczace")]
    if archiwum:
        z = archiwum[-1]
        print(f"\nOstatnie archiwum ({z['_slug']}): " + ", ".join(p["id"] for p in z["pozycje"]))

    tylko_nowe = obecne is not None and not a.wszystkie
    print("\nPozycje wydań dziennych, jeszcze nie cytowane"
          + (f" – tylko z wydań po {ostatnio} (--wszystkie: cały okres):" if tylko_nowe else " (* = wydanie po ostatniej aktualizacji):"))
    for w in dzienne:
        if not (od.isoformat() <= w["data"] <= do.isoformat()):
            continue
        nowe = "*" if w["data"] > ostatnio else " "
        if tylko_nowe and nowe == " ":
            continue
        for it in w["zarys"]:
            klucz = f"{w['_slug']}#{it['id']}"
            if klucz in cytowane:
                continue
            tekst = B.skroc(B.czysty(it["tekst"], osoby, pojecia), 110)
            print(f" {nowe}{klucz} | {it['data']} | {' '.join('#' + t for t in it['tagi'])} | {tekst}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
