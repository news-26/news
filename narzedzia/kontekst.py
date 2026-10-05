#!/usr/bin/env python3
"""Zwięzły kontekst na start wydania – zamiast czytania całych plików danych (oszczędność tokenów).

Użycie:
    python3 narzedzia/kontekst.py [RRRR-MM-DD]          # kontekst na dany dzień (domyślnie dziś)
    python3 narzedzia/kontekst.py --osoby ID [ID ...]    # karty wybranych osób
    python3 narzedzia/kontekst.py --zrodlo NAZWA_LUB_URL # poziom źródła w rankingu
    python3 narzedzia/kontekst.py --szukaj FRAZA         # wpisy rejestru notatki/rejestr-faktow.md z frazą

Drukuje: numer następnego wydania, „Do sprawdzenia” i wpisy „Czego tu nie ma” (dokumentacja) z poprzedniego
wydania do rozstrzygnięcia, kalendarz poprzedniego wydania, terminy obowiązkowe w oknie 10 dni i te do rozliczenia,
karty osób starsze niż 7 dni (z ostatnich 3 wydań), listę hashtagów i skrót rankingu źródeł.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402

REJESTR = B.REPO / "notatki" / "rejestr-faktow.md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dzien", nargs="?")
    ap.add_argument("--godzina", default="20:00", help="godzina przygotowywanego wydania (poranne: 06:00)")
    ap.add_argument("--osoby", nargs="+")
    ap.add_argument("--zrodlo")
    ap.add_argument("--szukaj")
    a = ap.parse_args()
    dane = B.REPO / "dane"
    B.RANKING = B.wczytaj_ranking(dane)
    terminy = B.wczytaj_terminy(dane)
    tagi, osoby, pojecia, wydania, rewizje, topy = B.wczytaj(dane)

    if a.osoby:
        for i in a.osoby:
            o = osoby.get(i)
            print(f"{i}: " + (f"{o['imie']} – {o['funkcja']} (zweryfikowano {o['zweryfikowano']})" if o else "BRAK KARTY"))
        return
    if a.zrodlo:
        o = B.RANKING.ocen(a.zrodlo, a.zrodlo if a.zrodlo.startswith("http") else "")
        print(f"{o['nazwa']}: poziom {o['poziom']}" if o else "spoza rankingu – dopisz świadomie do dane/zrodla.json")
        return
    if a.szukaj:
        if REJESTR.exists():
            for ln in REJESTR.read_text("utf-8").splitlines():
                if a.szukaj.lower() in ln.lower():
                    print(ln)
        return

    dzis = dt.date.fromisoformat(a.dzien) if a.dzien else dt.date.today()
    dzienne = [w for w in wydania if w.get("typ", "dzienne") == "dzienne" and (w["data"], w.get("godzina", "")) < (dzis.isoformat(), a.godzina)]
    prev = dzienne[-1] if dzienne else None
    nr = max((w.get("nr", 0) for w in wydania), default=0) + 1
    print(f"# Kontekst na {dzis.isoformat()} ({B.DNI[dzis.weekday()]}) – następne wydanie nr {nr}")
    if prev:
        print(f"\n## Poprzednie wydanie: nr {prev['nr']}, {prev['data']} {prev.get('godzina', '')}")
        print("Pozycje: " + "; ".join(f"{z['id']} [{','.join(z['tagi'])}] {B.czysty(z['tekst'], osoby, pojecia)[:90]}" for z in prev["zarys"]))
        if prev.get("do_sprawdzenia"):
            print("Do sprawdzenia:\n" + "\n".join(f"- {x}" for x in prev["do_sprawdzenia"]))
        doc = [c for c in prev.get("czego_nie_ma", []) if c.get("prog") == "dokumentacja"]
        if doc:
            print("Do rozstrzygnięcia (rozstrzygniecia, dotyczy RRRR-MM-DD#id):")
            for c in doc:
                print(f"- {prev['_slug']}#{c.get('id', '?')}: {B.czysty(c['tekst'], osoby, pojecia)[:160]}")
        kal = [k for k in prev.get("kalendarz", []) if k["data"] >= (dzis - dt.timedelta(days=2)).isoformat()]
        if kal:
            print("Kalendarz poprzedniego wydania (do przeniesienia lub rozliczenia):")
            for k in sorted(kal, key=lambda k: k["data"]):
                print(f"- {k['data']} [{','.join(k.get('tagi', []))}] {B.czysty(k['tekst'], osoby, pojecia)[:140]}")
    print("\n## Terminy obowiązkowe (dane/terminy.json)")
    for t in terminy:
        od, do = dt.date.fromisoformat(t["od"]), dt.date.fromisoformat(t.get("do") or t["od"])
        if od - dt.timedelta(days=10) <= dzis <= do + dt.timedelta(days=B.DNI_NA_ROZLICZENIE_KALENDARZA):
            stan = "TRWA/ROZLICZ" if dzis >= od else f"za {(od - dzis).days} dni – musi być w kalendarzu"
            print(f"- {t['od']}–{do.isoformat()} [{','.join(t['tagi'])}] {t['tekst']} – {stan} (id {t['id']})")
    print("\n## Karty osób z ostatnich 3 wydań starsze niż 7 dni (sprawdź, jeśli występują dziś)")
    uzyte = set()
    for w in dzienne[-3:]:
        for z in w["zarys"] + [{"tekst": s} for s in w.get("w_skrocie", [])]:
            uzyte |= {m.group(2) for m in B.ZNACZNIK_RE.finditer(z.get("tekst", "")) if m.group(1) == "o"}
    stare = [o for i, o in osoby.items() if i in uzyte and o["zweryfikowano"] < (dzis - dt.timedelta(days=7)).isoformat()]
    print("; ".join(f"{o['id']} ({o['zweryfikowano']})" for o in stare) or "brak")
    print(f"\n## Hashtagi: {', '.join(sorted(tagi))}")
    print(f"## Osoby z kartą: {len(osoby)} (szczegóły: --osoby ID); pojęcia: {', '.join(sorted(pojecia))}")
    pozi = {}
    for z in B.RANKING.dane["zrodla"] if hasattr(B.RANKING, "dane") else []:
        pozi.setdefault(z["poziom"], []).append(z["nazwa"].split(" (")[0])
    for p in sorted(pozi):
        print(f"## Ranking poziom {p}: {', '.join(pozi[p])}")
    if REJESTR.exists():
        tekst = REJESTR.read_text("utf-8")
        if "## Rozbieżności" in tekst:
            sekcja = tekst.split("## Rozbieżności", 1)[1].split("\n## ", 1)[0]
            print("\n## Rozbieżności z rejestru (notatki robocze)" + sekcja.rstrip())


if __name__ == "__main__":
    main()
