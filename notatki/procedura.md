# Prasówka – procedura wydania

Wydanie dzienne ok. 20:00, publikowane na https://news-26.github.io/news/. Format danych: README. Przy wątpliwości co do typu twierdzenia: `notatki/procedura-typy.md`. Top 10: `notatki/procedura-top10.md`. PDF tylko na żądanie (`python3 narzedzia/pdf.py SLUG`).

## Zasady treści

- **Tylko informacje potwierdzone**, bez etykiet NIEPOTWIERDZONE / SPRZECZNE. Wypowiedź strony zainteresowanej (Kreml, Mińsk, Teheran, Biały Dom, Pekin) – tylko jako fakt, że padła, z atrybucją.
- **Ranking** (`dane/zrodla.json`): pozycja = źródło z poziomu 1 albo dwa niezależne z poziomów 1–2; poziomy 3–5 nie są podstawą, 5 tylko jako wersja strony. Przedruk: „Reuters (za …)”. Nowe źródło dopisuj świadomie, z poziomem i uzasadnieniem.
- **Każde źródło podstawy zawiera główne twierdzenie pozycji** – nie sam temat i nie wydarzenia z innego dnia. Szczegół, który ma tylko jedno źródło, podaj z atrybucją w tekście („według …”) albo przenieś do „W obserwacji”. Artykuł redakcji z rankingu cytujący instytucję lub agencję ma poziom tej redakcji; zapis „X (za Y)” oznacza wyłącznie przedruk tekstu X u pośrednika lub agregatora (build.py liczy tak poziom od wydań z 10.10.2026).
- **Trzy progi:**
  1. *dokumentacja* – strona otwarta, nie tytuł. Blokada (403, robots, paywall) to nie brak dokumentacji: sprawdź komunikaty instytucji obu stron, przedruki agencji, inne redakcje z poziomu 2;
  2. *następstwo* – co się zmieniło i co z tego wynika dla Polski/Europy albo dla sytuacji międzynarodowej;
  3. *kompletność* – osoby z funkcją; uzbrojenie z nazwą systemu, liczbą, jednostką, pochodzeniem; liczby z datą i źródłem.
- **Fakty oddzielone od ocen.** Oceny (OSW, PISM, ISW, analitycy) tylko w analizach, z autorem i datą.
- **Poprzednie wydania i notatki nie są źródłem.** Statusy osób, etapy decyzji i daty sprawdzaj w dniu wydania.
- **Błędy prostuj jawnie** (`korekty`; pominięcie – pozycja + korekta).

## Tytuły

Dotyczy każdego tytułu i podpisu: pozycji Top 10, analiz, podpisów w kalendarium. Tytuł mówi jasno, co zaszło – zrozumiały bez czytania dalszego tekstu:
- konkretny podmiot i czasownik w czasie teraźniejszym;
- osoby z nazwiskiem i krótką funkcją, państwa i instytucje z nazwy;
- bez metafor, gier słów i ogólników;
- dwie sprawy – dwa człony po średniku, każdy z podmiotem;
- tylko fakty z tekstu i źródeł; czasownik oddaje etap decyzji.
- długość podporządkowana jasności: tytuł może być dłuższy, jeśli bez tego nie mówi w pełni, co zaszło.

## Dwie perspektywy

(a) Co ważne dla Polski i Europy; (b) najważniejsze dla sytuacji międzynarodowej, także bez skutku dla Polski. Pozycję albo wpis w sekcji „W obserwacji” zawsze mają:
- **incydenty w Polsce i przy jej granicach wynikające z sytuacji międzynarodowej** – drony, rakiety i ich szczątki na terytorium lub wodach RP albo do ok. 50 km od granicy; naruszenia przestrzeni powietrznej i poderwania lotnictwa; ataki na transport do i z Polski (pociągi, statki, przejścia graniczne); sabotaż, dywersja, szpiegostwo i cyberataki przypisane obcym służbom (zatrzymania, zarzuty, wyroki); presja na granicy z Białorusią; zakłócenia GPS i incydenty z infrastrukturą bałtycką; Polacy poszkodowani w konfliktach za granicą. Blok `polska`, tagi `obronnosc-polski` lub `hybryda` + miejsce. Bez krajowej polityki, gospodarki i legislacji;
- wojny i konflikty na świecie (Bliski Wschód, Sudan, Kongo, Sahel, Kaszmir, Tajwan, Korea) – eskalacja, rozejm, przełom, nowa strona;
- relacje mocarstw (USA, Chiny, Rosja, Indie, UE, Japonia) – szczyty, porozumienia, sankcje i cła dużej skali;
- zmiany władzy w G20 i kluczowych państwach regionalnych (wybory, przewroty, kryzysy konstytucyjne);
- broń jądrowa i proliferacja;
- decyzje globalne: Fed, OPEC+, MFW/Bank Światowy, RB ONZ, WTO;
- kryzysy humanitarne o skali międzynarodowej;
- szczyty G7/G20/APEC/UE/NATO/ONZ, spotkania przywódców mocarstw, wybory w regionie.

Filtr szumu: pozycja wchodzi, gdy zmienia decyzję, termin lub stan rzeczy i da się powiedzieć, co z niej wynika.

## Układ

- **W skrócie** – 3–5 zdań, w tym co najmniej jedno o najważniejszym wydarzeniu globalnym dnia, jeśli było.
- **I. Zarys** – 8–14 pozycji w blokach: wojna i sankcje / Polska / instytucje i Europa / świat (zwykle 2–4) / gospodarka (tylko zdarzenia nadzwyczajne). Kolejność według wagi dla Polski. Każda pozycja: data zdarzenia, hashtagi, 1–2 zdania o zmianie, **wyróżnione słowo kluczowe**, etap decyzji, wszystkie źródła potwierdzające.
- **II. Analizy** – 3–5, każda z autorem oceny i „Dla Polski” (przy sprawach globalnych – skutek pośredni).
- **III.** Kalendarz 7–10 dni, poza oknem, OSW i PISM z 3 dni (jeśli nic – wprost), „W obserwacji”, rozstrzygnięcia, nota.
- Bez emoji.

## Kalendarium (`dane/terminy.json`, pół roku naprzód)

- Przy każdym wydaniu dopisz nowe zapowiedziane wydarzenia międzynarodowe o dużym znaczeniu, popraw zmienione daty, usuń odwołane. Bez krajowych spraw polskich (RPP, GUS, krajowa legislacja); Polska tylko jako uczestnik wydarzenia międzynarodowego.
- Pola: `id`, `od`, `do`, `kategoria` (szczyt / wybory / banki / instytucje / inne), `tekst`, `krotko` (do ok. 25 znaków), `tagi`, `zrodla`, opcjonalnie `uwaga`. Źródło: poziom 1 albo dwa z poziomów 1–2.
- Terminy obowiązkowe (domyślne: szczyty G7/G20/APEC/UE/NATO/ONZ, spotkania przywódców mocarstw, wybory w regionie i w G20) same trafiają do kalendarza wydania na 7 dni przed. Pozostałe mają `"obowiazkowy": false`.
- 1. dnia miesiąca uzupełnij na 2 miesiące naprzód, także o terminy globalne (wybory w G20, RB ONZ, OPEC+, COP).
- Brakuje (dopisz, gdy znajdzie się źródło): szczyt ASEAN (16–18.11), Monachijska Konferencja Bezpieczeństwa 2027, wybory prezydenckie w Serbii (do końca 2026), marcowa Rada Europejska 2027.

## Straże kompletności (pilnuje build.py)

- „W obserwacji” z progiem dokumentacja: `id` + `sprawdzono` (min. 3 miejsca). Następne wydanie rozlicza wpis w `rozstrzygniecia`: UZUPEŁNIONE (`pozycja`) / NIE DO POTWIERDZENIA (`sprawdzono`, `powod`) / ODPADA (`powod`).
- Termin z kalendarza po 2 dniach: pozycja albo wpis z polem `kalendarz`. Jeden wiersz kalendarza = jedno wydarzenie.
- Termin z `terminy.json` po zakończeniu: pozycja albo wpis z polem `termin`.
- Rewizja nie wycofa pozycji bez `sprawdzono` (min. 3 miejsca).
- build.py odrzuca też publikowane pliki z adresem e-mail, ścieżką lokalną, zasobem z zewnątrz lub bez `no-referrer`. Nie obchodź walidacji.

## Strona

Wszystko lokalnie albo inline: bez skryptów, czcionek, analityki i osadzeń z zewnątrz, bez ciasteczek, formularzy i komentarzy. Linki zewnętrzne z `rel="noopener noreferrer"`. Nowa funkcja, która musiałaby coś pobierać z zewnątrz – tylko po zgodzie właściciela.

## Kroki

**0. Start.** Data i godzina Europe/Warsaw. `python3 narzedzia/kontekst.py RRRR-MM-DD` (numer, „Do sprawdzenia”, wpisy do rozstrzygnięcia, kalendarz, karty osób do odświeżenia, ranking). Nie czytaj w całości README, `dane/*.json`, poprzednich wydań ani rejestru – używaj `kontekst.py --osoby ID / --zrodlo NAZWA / --szukaj FRAZA` albo grep. Potem `python3 narzedzia/nowe_wydanie.py RRRR-MM-DD` (szkielet).

**1. Materiał.** Najpierw – priorytetowo – dział Świat Onetu (https://wiadomosci.onet.pl/swiat): każdy temat stamtąd od poprzedniego wydania kończy jako pozycja albo wpis w sekcji „W obserwacji”. Onet ma poziom 2 – priorytet dotyczy doboru tematów, nie progu dokumentacji; depesza agencji w Onecie to „AGENCJA (za Onet)”. Gdy strona jest zablokowana, przegląd nagłówków działu wyszukiwarką jest obowiązkowy (co najmniej dwa zapytania z datą dnia); sam nagłówek nie jest źródłem – dokumentacja z innych miejsc. Nota podaje, czy dział otwarto, czy przejrzano go wyszukiwarką i ile tematów z niego trafiło do wydania. Potem przegląd tematów od poprzedniego wydania: Reuters, AP, Al Jazeera, PAP (świat/Europa, a w Reuters i AP także Bliski Wschód, Azja, Afryka, Ameryki) – 12–18 tematów, w tym wszystkie z „Dwóch perspektyw”; każdy kończy jako pozycja albo wpis w sekcji „W obserwacji”. Potem incydenty w Polsce (od poprzedniego wydania): PAP Kraj oraz komunikaty DO RSZ, MON, Straży Granicznej, Żandarmerii Wojskowej, Prokuratury Krajowej, ABW/SKW i rzecznika ministra koordynatora służb. Incydent w Polsce prawie zawsze ma komunikat instytucji (poziom 1) – szukaj go najpierw; relacja RMF24, TVN24, Polsat News czy Interii (poziom 3) to sygnał do szukania komunikatu, nie powód do pominięcia. Potem OSW i PISM (3 dni), Kyiv Independent, AFP, ISW (ocena), GUS/NBP, MON/DO RSZ przy uzbrojeniu, punkty z kontekst.py.

**2. Weryfikacja.** Statusy osób i etapy decyzji – dziś, chyba że karta/rejestr ma ≤ 7 dni. Co nie przechodzi – do „W obserwacji” dopiero po sprawdzeniu źródeł zastępczych, z `sprawdzono`.

**3. Pisanie.** Uzupełnij szkielet przez Edit. Osoby `{{o:id|forma}}`, pojęcia `{{p:id|forma}}`; nowe karty i hasła dopisuj punktowo; karty starsze niż 7 dni sprawdź, jeśli osoba występuje. Nowy hashtag – świadomie, ze `stan_data`. `tagi.json`: stan wątków z wydania. `do_sprawdzenia`: lista na jutro. Kalendarium. Rejestr `notatki/rejestr-faktow.md` – tylko zmiany punktowe. `python3 narzedzia/build.py`.

**4. Kontrola niezależna – obowiązkowa przed publikacją.** Bez niej nie pushuj; jeśli agent dwukrotnie nie zdoła jej przeprowadzić, opublikuj, a pierwsze zdanie noty mówi, że kontroli nie było i dlaczego. Agent general-purpose, który nie widział pisania, dostaje **ścieżkę** `dane/wydania/SLUG.json` (nie treść). Zadania: typy A, D, E, G, H i uzbrojenie; pozycje na jednym źródle, tytule albo poziomach 3–5, także gdy drugie źródło nie zawiera głównego twierdzenia; kompletność – tematy z działu Świat Onetu oraz główne tematy z Reutersa, AP, Al Jazeery, PAP od poprzedniego wydania (także globalne), których nie ma ani w zarysie, ani w nocie, oraz incydenty w Polsce i przy jej granicach z komunikatów DO RSZ, MON, SG, ŻW, prokuratury i z PAP Kraj; wpisy „dokumentacja”, które da się udokumentować. Najpierw WebSearch, WebFetch tylko dla twierdzeń niejasnych, każdy adres raz, raport < 400 słów. Popraw dane, przebuduj. Podgląd wizualny (render PNG) tylko gdy zmieniono build.py lub styl.css.

**5. Publikacja.** Commit „Wydanie nr N, RRRR-MM-DD”, `git fetch origin main` + rebase, `git push origin HEAD:main`. Tylko `main`: bez gałęzi, tagów, issues, PR i wydań GitHub. Przy błędzie ponów raz po 10 s; jeśli dalej nie przechodzi – nie obchodź (żadnych tokenów, forków, innych zdalnych), zgłoś w pierwszym zdaniu odpowiedzi z dosłownym komunikatem. Sprawdź stronę jednym WebFetch. Nie twórz osobnych notatek z przebiegu – „Do sprawdzenia” jest w danych, przebieg w nocie.

**Odpowiedź:** 3–4 zdania – najważniejsze wydarzenia, OSW/PISM, korekta, publikacja.

## Oszczędność

- Czytaj fragmenty, nie całe pliki; nie czytaj ponownie pliku, który właśnie zapisałeś. Edytuj punktowo.
- WebFetch z wąskim pytaniem; każdy adres raz; strona zablokowana – od razu inne źródło.
- Ok. 35–45 wywołań narzędzi na wydanie; w niedziele i dni bez decyzji mniej.
