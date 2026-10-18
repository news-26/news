# Top 10

Dwa rodzaje zestawień, ten sam format (README, „Zestawienia Top 10”):

- **Kroczące** – `dane/top/biezace.json`: najważniejsze sprawy z ostatnich 7 dni (najwyżej 10), odświeżane codziennie rano. Okno: `do` = data ostatniego wydania dziennego, `od` = `do` − 6 dni (build.py to sprawdza). Strona `top/biezace.html` i blok na stronie głównej.
- **Archiwum** – `dane/top/RRRR-MM-01_RRRR-MM-OSTATNI.json`: zamknięte zestawienie za miesiąc kalendarzowy, tworzone 1. dnia następnego miesiąca i potem niezmieniane.

## Przebieg porannej aktualizacji

1. `python3 narzedzia/top_kandydaci.py` – okno, obecne pozycje (z oznaczeniem tych, które wypadły z okna) i pozycje z wydań od ostatniej aktualizacji. Pierwszy raz albo przy wątpliwości: `--wszystkie`.
2. Zaktualizuj `biezace.json`: przesuń `od`/`do`, ustaw `opublikowano` i `godzina`. Pozycja bez faktu w oknie wypada (walidacja jej nie przepuści). Tytuł i `data` każdej pozycji opisują najnowszy fakt z okna – pozycja z tytułem o wydarzeniu sprzed okna dostaje nowy tytuł albo wypada. Nowy fakt w sprawie już obecnej – dopisz wiersz `przebieg` i odnośnik `w_wydaniach`, popraw lead; jeśli zmieniasz tytuł, zmień `data` (sekcja „Data wydarzenia”). Nowa sprawa – wchodzi, jeśli spełnia kryteria; przy pełnej liście – jeśli jest ważniejsza od ostatniej. Przejrzyj też „Czego tu nie ma” z wydań w oknie: jeśli wpis był błędnie odrzucony (dwa niezależne źródła z poziomów 1–2 istnieją), popraw wydanie dzienne korektą i dopiero wtedy włącz sprawę. Zmień kolejność, jeśli waga się zmieniła. Popraw `wstep` tak, by opisywał obecne okno.
3. Jeśli nic istotnego się nie zmieniło, ogranicz się do przesunięcia okna, usunięcia pozycji, które z niego wypadły, i aktualizacji tytułów.
4. **1. dnia miesiąca dodatkowo:** utwórz archiwum za miniony miesiąc (`top_kandydaci.py --miesiac RRRR-MM --wszystkie`), z wszystkich pozycji wydań dziennych z miesiąca (nie z listy kroczącej, która obejmuje tylko tydzień): daty przebiegu w miesiącu (dopuszczalny tydzień kontekstu przed), kryteria liczone dla tego miesiąca. Archiwum nazywa się miesiącem („Październik 2026”).
5. `python3 narzedzia/build.py`, commit „Top 10 – RRRR-MM-DD” (1. dnia: „Top 10 – <miesiąc RRRR>”), push na main jak w `notatki/procedura.md`, krok 5.

## Kryteria – trzy warunki naraz

1. **Trwała zmiana w okresie**: decyzja przyjęta, zmiana władzy, nowa zdolność wojskowa, incydent z realnym następstwem. Retoryka i zapowiedzi bez terminu nie wystarczą.
2. **Skutek dla Polski lub Europy albo dla sytuacji międzynarodowej** (układ sił, wojny i rozejmy, relacje mocarstw, globalna gospodarka), nazwany w jednym zdaniu.
3. **Co najmniej dwie pozycje** w wydaniach dziennych z okresu.

Wątki wielomiesięczne (wojna, Iran, Królewiec): wchodzi zmiana w okresie, nie wątek.

Kolejność: (1) wpływ na bezpieczeństwo i interesy Polski, (2) waga dla sytuacji międzynarodowej i skala, (3) trwałość skutków. Zwykle 2–3 sprawy o wadze globalnej, nawet przy pośrednim skutku dla Polski. Ranking to ocena redakcji – opisz ją w polu `kryteria`. Najwyżej 10 pozycji, mniej, gdy w tygodniu mniej spraw spełnia kryteria – nie dopełniaj listy; miejsca 11+ można wymienić w `czego_nie_ma` z progiem „następstwo”.

## Tytuły

Według zasady „Tytuły” w `notatki/procedura.md`.

## Data wydarzenia

Każda pozycja ma pole `data` – datę wydarzenia opisanego w tytule, nie zakres całego przebiegu. Strona pokazuje ją przy tytule na wszystkich listach Top 10.

- Jedno wydarzenie – jedna data: `"data": "2026-09-30"`.
- Tytuł łączy kilka faktów („…; UE przedłuża sankcje”) – zakres od pierwszego do ostatniego z nich: `"data": ["2026-09-18", "2026-09-22"]`.
- Każda data musi być datą wiersza `przebieg` z tym faktem (build.py to sprawdza).
- Przy każdej zmianie tytułu (nowy fakt w sprawie) zmień też `data`. Data sprzed okna w zestawieniu kroczącym oznacza, że tytuł nie opisuje już najnowszego faktu – rozważ nowy tytuł.

## Weryfikacja

Wydań dziennych nie weryfikujemy od nowa i nie czytamy ich w całości. Wiersze `przebieg` biorą tekst w skrócie i źródła z pozycji dziennych; każdy wiersz musi spełniać zasadę rankingu – jeśli pozycja dzienna jej nie spełnia (wydania sprzed 1.10.2026), dobierz drugie źródło albo pomiń wiersz. Ponownie sprawdź tylko: korekty z wydań dziennych, funkcje osób z kartami starszymi niż 7 dni, rozstrzygnięcia zapowiedzi pokazywanych jako zamknięte. Lead i omówienie – tylko fakty z wierszy przebiegu; interpretacja w `oceny` (z autorem) i w „Dla Polski”.

## Historia

- Sprawa kontynuowana – **to samo `id`** we wszystkich zestawieniach (odznaka „ponownie”, gdy była już w archiwum).
- Nowa sprawa – nowe `id` (odznaka „nowe”).
- Sprawa zamknięta – `"rozstrzygniete": true`.
