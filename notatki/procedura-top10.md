# Top 10 miesięczne

Zestawienie za poprzedni miesiąc kalendarzowy, publikowane 1. dnia miesiąca rano. Plik `dane/top/RRRR-MM-01_RRRR-MM-OSTATNI.json`, format w README („Zestawienia Top 10”); strona nazywa zestawienie miesiącem („Październik 2026”). `python3 narzedzia/build.py`, commit „Top 10 – <miesiąc RRRR>”, push na main (jak w `notatki/procedura.md`, krok 5). Tygodniówek nie bierz pod uwagę.

## Kryteria – trzy warunki naraz

1. **Trwała zmiana w tym miesiącu**: decyzja przyjęta, zmiana władzy, nowa zdolność wojskowa, incydent z realnym następstwem. Retoryka i zapowiedzi bez terminu nie wystarczą.
2. **Skutek dla Polski lub Europy albo dla sytuacji międzynarodowej** (układ sił, wojny i rozejmy, relacje mocarstw, globalna gospodarka), nazwany w jednym zdaniu.
3. **Co najmniej dwie pozycje** w wydaniach dziennych z tego miesiąca.

Wątki wielomiesięczne (wojna, Iran, Królewiec): wchodzi zmiana w danym miesiącu, nie wątek.

Kolejność: (1) wpływ na bezpieczeństwo i interesy Polski, (2) waga dla sytuacji międzynarodowej i skala, (3) trwałość skutków. Zwykle 2–3 sprawy o wadze globalnej, nawet przy pośrednim skutku dla Polski. Ranking to ocena redakcji – opisz ją w polu `kryteria`. Najwyżej 10 pozycji; miejsca 11+ można wymienić w `czego_nie_ma` z progiem „następstwo”.

## Weryfikacja

Wydań dziennych nie weryfikujemy od nowa. Kandydatów wyciągnij skryptem z `dane/wydania/` (id, data, hashtagi, początek tekstu), bez czytania plików w całości. Wiersze `przebieg` biorą tekst w skrócie i źródła z pozycji dziennych; każdy wiersz musi spełniać zasadę rankingu – jeśli pozycja dzienna jej nie spełnia (wydania sprzed 1.10.2026), dobierz drugie źródło albo pomiń wiersz. Ponownie sprawdź tylko: korekty z wydań dziennych, funkcje osób z kartami starszymi niż 7 dni, rozstrzygnięcia zapowiedzi pokazywanych jako zamknięte. Lead i omówienie – tylko fakty z wierszy przebiegu; interpretacja w `oceny` (z autorem) i w „Dla Polski”.

## Historia

- Sprawa kontynuowana – **to samo `id`** (odznaka „ponownie”); wraca tylko z nowym faktem z bieżącego miesiąca.
- Nowa sprawa – nowe `id` (odznaka „nowe”).
- Sprawa zamknięta w tym miesiącu – `"rozstrzygniete": true`.
