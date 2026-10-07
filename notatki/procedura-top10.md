# Top 10

Dwa rodzaje zestawień, ten sam format (README, „Zestawienia Top 10”):

- **Kroczące** – `dane/top/biezace.json`: dziesięć najważniejszych spraw z ostatnich 30 dni, odświeżane codziennie rano. Okno: `do` = data ostatniego wydania dziennego, `od` = `do` − 29 dni (build.py to sprawdza). Strona `top/biezace.html` i blok na stronie głównej.
- **Archiwum** – `dane/top/RRRR-MM-01_RRRR-MM-OSTATNI.json`: zamknięte zestawienie za miesiąc kalendarzowy, tworzone 1. dnia następnego miesiąca i potem niezmieniane.

## Przebieg porannej aktualizacji

1. `python3 narzedzia/top_kandydaci.py` – okno, obecne pozycje (z oznaczeniem tych, które wypadły z okna) i pozycje z wydań od ostatniej aktualizacji. Pierwszy raz albo przy wątpliwości: `--wszystkie`.
2. Zaktualizuj `biezace.json`: przesuń `od`/`do`, ustaw `opublikowano` i `godzina`. Pozycja bez faktu w oknie wypada (walidacja jej nie przepuści). Nowy fakt w sprawie już obecnej – dopisz wiersz `przebieg` i odnośnik `w_wydaniach`, popraw lead. Nowa sprawa – wchodzi, jeśli spełnia kryteria i jest ważniejsza od ostatniej na liście. Zmień kolejność, jeśli waga się zmieniła. Popraw `wstep` tak, by opisywał obecne okno.
3. Jeśli nic istotnego się nie zmieniło, ogranicz się do przesunięcia okna i usunięcia pozycji, które z niego wypadły.
4. **1. dnia miesiąca dodatkowo:** utwórz archiwum za miniony miesiąc (`top_kandydaci.py --miesiac RRRR-MM --wszystkie`), wychodząc od listy kroczącej i przycinając ją do miesiąca kalendarzowego: daty przebiegu w miesiącu (dopuszczalny tydzień kontekstu przed), kryteria liczone dla tego miesiąca. Archiwum nazywa się miesiącem („Październik 2026”).
5. `python3 narzedzia/build.py`, commit „Top 10 – RRRR-MM-DD” (1. dnia: „Top 10 – <miesiąc RRRR>”), push na main jak w `notatki/procedura.md`, krok 5.

## Kryteria – trzy warunki naraz

1. **Trwała zmiana w okresie**: decyzja przyjęta, zmiana władzy, nowa zdolność wojskowa, incydent z realnym następstwem. Retoryka i zapowiedzi bez terminu nie wystarczą.
2. **Skutek dla Polski lub Europy albo dla sytuacji międzynarodowej** (układ sił, wojny i rozejmy, relacje mocarstw, globalna gospodarka), nazwany w jednym zdaniu.
3. **Co najmniej dwie pozycje** w wydaniach dziennych z okresu.

Wątki wielomiesięczne (wojna, Iran, Królewiec): wchodzi zmiana w okresie, nie wątek.

Kolejność: (1) wpływ na bezpieczeństwo i interesy Polski, (2) waga dla sytuacji międzynarodowej i skala, (3) trwałość skutków. Zwykle 2–3 sprawy o wadze globalnej, nawet przy pośrednim skutku dla Polski. Ranking to ocena redakcji – opisz ją w polu `kryteria`. Najwyżej 10 pozycji; miejsca 11+ można wymienić w `czego_nie_ma` z progiem „następstwo”.

## Weryfikacja

Wydań dziennych nie weryfikujemy od nowa i nie czytamy ich w całości. Wiersze `przebieg` biorą tekst w skrócie i źródła z pozycji dziennych; każdy wiersz musi spełniać zasadę rankingu – jeśli pozycja dzienna jej nie spełnia (wydania sprzed 1.10.2026), dobierz drugie źródło albo pomiń wiersz. Ponownie sprawdź tylko: korekty z wydań dziennych, funkcje osób z kartami starszymi niż 7 dni, rozstrzygnięcia zapowiedzi pokazywanych jako zamknięte. Lead i omówienie – tylko fakty z wierszy przebiegu; interpretacja w `oceny` (z autorem) i w „Dla Polski”.

## Historia

- Sprawa kontynuowana – **to samo `id`** we wszystkich zestawieniach (odznaka „ponownie”, gdy była już w archiwum).
- Nowa sprawa – nowe `id` (odznaka „nowe”).
- Sprawa zamknięta – `"rozstrzygniete": true`.
