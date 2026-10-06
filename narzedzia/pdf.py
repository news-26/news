#!/usr/bin/env python3
"""PDF archiwalny wydania z tych samych danych co strona i mail (bez pisania kodu PDF przy każdym wydaniu).

Użycie: python3 narzedzia/pdf.py RRRR-MM-DD [--wyjscie build]
Tworzy build/przeglad-miedzynarodowy-RRRR-MM-DD.pdf: A4, DejaVu Sans, granatowe paski sekcji,
wyróżnione słowa kluczowe, źródła kursywą mniejszą czcionką, numer strony w stopce.
"""
import argparse
import re
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402

GRANAT, ZLOTY, MORZE, SZARY = HexColor("#17243B"), HexColor("#C9A227"), HexColor("#1D5F86"), HexColor("#5C6673")
FONTY = Path("/usr/share/fonts/truetype/dejavu")


def fonty():
    for n, f in (("DV", "DejaVuSans.ttf"), ("DV-B", "DejaVuSans-Bold.ttf"), ("DV-I", "DejaVuSans-Oblique.ttf"), ("DV-BI", "DejaVuSans-BoldOblique.ttf")):
        pdfmetrics.registerFont(TTFont(n, str(FONTY / f)))
    pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV-I", boldItalic="DV-BI")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--wyjscie", type=Path, default=Path("build"))
    a = ap.parse_args()
    dane = B.REPO / "dane"
    B.RANKING = B.wczytaj_ranking(dane)
    tagi, osoby, pojecia, wydania, rewizje, topy = B.wczytaj(dane)
    w = next((x for x in wydania if x["_slug"] == a.slug), None)
    if not w:
        sys.exit(f"Brak wydania {a.slug}")
    fonty()
    st = {
        "tyt": ParagraphStyle("tyt", fontName="DV-B", fontSize=17, textColor=GRANAT, leading=21),
        "pod": ParagraphStyle("pod", fontName="DV", fontSize=9.5, textColor=SZARY, leading=13, spaceAfter=6),
        "txt": ParagraphStyle("txt", fontName="DV", fontSize=9.5, leading=13.2),
        "blok": ParagraphStyle("blok", fontName="DV-B", fontSize=10, textColor=GRANAT, spaceBefore=6, spaceAfter=2),
        "zr": ParagraphStyle("zr", fontName="DV-I", fontSize=7.6, textColor=SZARY, leading=10, spaceAfter=5),
        "dp": ParagraphStyle("dp", fontName="DV", fontSize=9, leading=12.5, leftIndent=8, textColor=MORZE),
        "meta": ParagraphStyle("meta", fontName="DV-B", fontSize=8, textColor=SZARY, leading=11),
    }

    def T(s):
        s = re.sub(r"\*\*(.+?)\*\*", "\x01\\1\x02", s)  # wyróżnienia przetrwają czyszczenie znaczników
        t = B.e(B.czysty(s, osoby, pojecia))
        return t.replace("\x01", '<font backColor="#FFE9A3"><b>').replace("\x02", "</b></font>")

    def zrodla(lst):
        return Paragraph("Źródła: " + "; ".join(f'<a href="{B.e(z["url"])}">{B.e(z["nazwa"])}, {B.data_krotka(z["data"])}</a>' for z in lst or []), st["zr"])

    def pasek(t):
        tb = Table([[Paragraph(f'<font color="#FFFFFF"><b>{B.e(t)}</b></font>', st["txt"])]], colWidths=[180 * mm])
        tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GRANAT), ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
        tb.keepWithNext = True
        return [Spacer(1, 6), tb, Spacer(1, 4)]

    rodzaj = "Wydanie tygodniowe" if w.get("typ") == "tygodniowe" else "Wydanie"
    h = [Paragraph("Prasówka – przegląd sytuacji międzynarodowej", st["tyt"]),
         Paragraph(f"{rodzaj} nr {w['nr']}, {B.data_pelna(w['data'])}, stan na {w['godzina']} CEST · {B.BASE_URL}wydania/{w['_slug']}.html", st["pod"])]
    h += pasek("W skrócie") + [Paragraph(T(s), st["txt"]) for s in w["w_skrocie"]]
    if w.get("korekty"):
        h += pasek("Korekta")
        for k in w["korekty"]:
            h += [Paragraph(f"<b>Było:</b> {B.e(k['bylo'])}<br/><b>Jest:</b> {B.e(k['jest'])}", st["txt"]), zrodla(k.get("zrodla"))]
    h += pasek("I. Zarys wydarzeń")
    for kod, nazwa in B.BLOKI:
        poz = sorted((z for z in w["zarys"] if z["blok"] == kod), key=lambda z: z["data"])
        if not poz:
            continue
        h.append(Paragraph(nazwa, st["blok"]))
        for z in poz:
            meta = f"{B.data_krotka(z['data'])} · " + " ".join("#" + tagi[t]["nazwa"] for t in z["tagi"]) + (f" · {z['etap']}" if z.get("etap") else "")
            h.append(KeepTogether([Paragraph(B.e(meta), st["meta"]), Paragraph(T(z["tekst"]), st["txt"]), zrodla(z["zrodla"])]))
    if w.get("analizy"):
        h += pasek("II. Analizy (interpretacje, nie ustalenia)")
        for x in w["analizy"]:
            h.append(KeepTogether([Paragraph(f"<b>{B.e(x['tytul'])}</b> – ocena: {B.e(x['autor'])}", st["txt"]),
                                   Paragraph(T(x["tekst"]), st["txt"]), Paragraph("<b>Dla Polski:</b> " + T(x["dla_polski"]), st["dp"]),
                                   zrodla(x.get("zrodla"))]))
    za = w.get("zrodla_analityczne") or {}
    h += pasek("III. Kalendarz i zastrzeżenia")
    for k in sorted(w.get("kalendarz", []), key=lambda k: k["data"]):
        h.append(Paragraph(f"<b>{B.data_krotka(k['data'])}</b> {T(k['tekst'])}", st["txt"]))
    if w.get("poza_oknem"):
        h.append(Paragraph("<b>Poza oknem, ale przesądzające:</b> " + "; ".join(f"{B.data_krotka(k['data'])} {T(k['tekst'])}" for k in w["poza_oknem"]), st["txt"]))
    for kl, nz in (("osw", "OSW"), ("pism", "PISM")):
        lst = za.get(kl) or []
        h.append(Paragraph(f"<b>{nz}:</b> " + ("brak nowych publikacji z ostatnich 3 dni" if not lst else
                           "; ".join(f"{B.e(p['tytul'])} ({B.e(p.get('autor', ''))}, {B.data_krotka(p['data'])})" for p in lst)), st["txt"]))
    if w.get("czego_nie_ma"):
        h.append(Paragraph("<b>W obserwacji:</b> " + "; ".join(f"{T(c['tekst'])} (próg: {c['prog']})" for c in w["czego_nie_ma"]), st["zr"]))
    if w.get("rozstrzygniecia"):
        h.append(Paragraph("<b>Rozstrzygnięcia z poprzedniego wydania:</b> " + "; ".join(f"{r['dotyczy']}: {r['wynik']}" for r in w["rozstrzygniecia"]), st["zr"]))
    if w.get("nota"):
        h.append(Paragraph("<b>Nota metodyczna:</b> " + T(w["nota"]), st["zr"]))

    def stopka(c, doc):
        c.saveState()
        c.setFont("DV", 7.5)
        c.setFillColor(SZARY)
        c.drawString(15 * mm, 9 * mm, f"Prasówka nr {w['nr']} · {B.data_krotka(w['data'])}.{w['data'][:4]}")
        c.drawRightString(195 * mm, 9 * mm, f"strona {doc.page}")
        c.restoreState()
    a.wyjscie.mkdir(parents=True, exist_ok=True)
    cel = a.wyjscie / f"przeglad-miedzynarodowy-{a.slug}.pdf"
    SimpleDocTemplate(str(cel), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm, bottomMargin=16 * mm,
                      title=f"Prasówka nr {w['nr']}").build(h, onFirstPage=stopka, onLaterPages=stopka)
    print(f"{cel} ({cel.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
