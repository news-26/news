#!/usr/bin/env python3
"""Szkielet nowego wydania dziennego – mniej przepisywania (oszczędność tokenów wyjściowych).

Użycie: python3 narzedzia/nowe_wydanie.py RRRR-MM-DD [--godzina 20:00] [--rano]

Dwa wydania dziennie (od 5.10.2026): poranne ok. 6:00 (--rano → plik RRRR-MM-DD-rano.json, godzina 06:00)
i wieczorne ok. 20:00 (plik RRRR-MM-DD.json). Poprzednie wydanie = ostatnie wcześniejsze wg (data, godzina).

Tworzy dane/wydania/RRRR-MM-DD[-rano].json (nie nadpisuje istniejącego) z:
- numerem kolejnym, datą, godziną, typem,
- kalendarzem przeniesionym z poprzedniego wydania (terminy od dziś) i z terminami obowiązkowymi
  z dane/terminy.json, które wypadają w ciągu 7 dni, a nie ma ich w kalendarzu,
- „poza_oknem” przeniesionym z poprzedniego wydania (bez minionych),
- stubami „rozstrzygniecia” dla każdego wpisu „dokumentacja” z poprzedniego wydania (wynik do uzupełnienia),
- pustymi polami: w_skrocie, zarys, analizy, zrodla_analityczne, czego_nie_ma, do_sprawdzenia, nota.
Pola oznaczone „DO UZUPEŁNIENIA” trzeba wypełnić; build.py nie przepuści stubów bez wyniku.
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dzien")
    ap.add_argument("--godzina")
    ap.add_argument("--rano", action="store_true", help="wydanie poranne: plik RRRR-MM-DD-rano.json, godzina 06:00")
    a = ap.parse_args()
    a.godzina = a.godzina or ("06:00" if a.rano else "20:00")
    dane = B.REPO / "dane"
    cel = dane / "wydania" / (f"{a.dzien}-rano.json" if a.rano else f"{a.dzien}.json")
    if cel.exists():
        sys.exit(f"{cel} już istnieje – edytuj go (Edit), nie twórz od nowa")
    tagi, osoby, pojecia, wydania, rewizje, topy = B.wczytaj(dane)
    terminy = B.wczytaj_terminy(dane)
    dzis = dt.date.fromisoformat(a.dzien)
    dzienne = [w for w in wydania if w.get("typ", "dzienne") == "dzienne" and (w["data"], w.get("godzina", "")) < (a.dzien, a.godzina)]
    prev = dzienne[-1] if dzienne else {}
    nr = max((w.get("nr", 0) for w in wydania), default=0) + 1

    def czysc(k):
        return {x: v for x, v in k.items() if not x.startswith("_")}
    kal = [czysc(k) for k in prev.get("kalendarz", []) if k["data"] >= a.dzien]
    for t in terminy:
        if not B.obowiazkowy(t):
            continue  # pozostałe terminy kalendarium – tylko jako podpowiedź w kontekst.py
        od = dt.date.fromisoformat(t["od"])
        if dzis <= od <= dzis + dt.timedelta(days=7) and not any(k["data"] == t["od"] and set(t["tagi"]) & set(k.get("tagi", [])) for k in kal):
            kal.append({"data": t["od"], "tekst": t["tekst"], "tagi": t["tagi"], "zrodla": t.get("zrodla", [])})
    kal.sort(key=lambda k: k["data"])
    poza = [czysc(k) for k in prev.get("poza_oknem", []) if k["data"] > (dzis + dt.timedelta(days=10)).isoformat()]
    rozs = [{"dotyczy": f"{prev['_slug']}#{c['id']}", "wynik": "DO UZUPEŁNIENIA", "powod": c["tekst"][:120]}
            for c in prev.get("czego_nie_ma", []) if c.get("prog") == "dokumentacja" and c.get("id")]
    w = {"nr": nr, "data": a.dzien, "godzina": a.godzina, "typ": "dzienne",
         "w_skrocie": [], "korekty": [], "zarys": [], "analizy": [],
         "kalendarz": kal, "poza_oknem": poza,
         "zrodla_analityczne": {"osw": [], "pism": []},
         "czego_nie_ma": [], "rozstrzygniecia": rozs, "do_sprawdzenia": [], "nota": ""}
    cel.write_text(json.dumps(w, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"Utworzono {cel.name}: nr {nr}, kalendarz {len(kal)} (przeniesiony – sprawdź aktualność), "
          f"poza oknem {len(poza)}, rozstrzygnięcia do uzupełnienia {len(rozs)}")


if __name__ == "__main__":
    main()
