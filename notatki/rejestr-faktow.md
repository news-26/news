# Rejestr faktów – notatki robocze

Przeniesiony z projektu do repozytorium 4.10.2026 (oszczędność tokenów: zmiany punktowe przez Edit, bez przepisywania całości; czytanie przez `python3 narzedzia/kontekst.py --szukaj FRAZA`). Nie trafia na stronę.

Zasada: fakt z rejestru wchodzi do wydania bez ponownego sprawdzenia tylko wtedy, gdy „zweryfikowano” nie jest starsze niż 7 dni. Funkcje osób żyją w `dane/osoby.json` (pole `zweryfikowano`), stan wątków w `dane/tagi.json` („Na czym stoimy”), terminy obowiązkowe w `dane/terminy.json` – tu tylko to, czego tam nie ma: statusy spraw, rozbieżności i notatki. Wpisy oznaczone „jedno źródło”, „tylko tytuł” lub z rozbieżnością nie wchodzą do wydania, dopóki nie zostaną potwierdzone. Wpisy starsze niż 30 dni bez użycia – usuwać.

Format: fakt | stan | zweryfikowano | źródło

## Statusy osób i spraw
- Andrzej Poczobut | WOLNY od 28.04.2026 (wymiana więźniów PL–BY z udziałem USA); 8–15.09.2026 odwiedził Grodno i wrócił do Polski. Uwaga: WebFetch RMF24 podał błędnie rok 2024 | 26.09.2026 | gov.pl 28.04; Reuters 8.09; Belsat 15 i 23.09
- Péter Magyar | premier Węgier od maja 2026; 28.09 parlament zawiesił jego immunitet oraz immunitety b. ministrów Hankó i Sesztáka; odrzucono kandydata prezydenta na PG (Szathmáry, 138 przeciw) | 28.09.2026 | AP/WaPo 28.09; Euronews 28.09
- András Baka | prezydent Węgier od 11.08.2026; nowego kandydata na PG do 3.10 nie ogłoszono (tylko BBJ) | 03.10.2026 | CNN 11.08; BBJ 28.09
- Miklós Seszták | 30.09 areszt na 30 dni (nieprawomocny); kwota 11 vs 12 mld Ft – bez kwoty | 30.09.2026 | Index; Portfolio 30.09
- Balázs Hankó | zatrzymany 28.09 (Reuters 29.09); 1.10 areszt tymczasowy na miesiąc (Kecskemét), nieprawomocny – tylko MTI/BBJ, Telex, OCCRP | 03.10.2026 | Reuters (Internazionale) 29.09; BBJ/MTI 1.10
- István Lajtár | zastępca PG Węgier, p.o. PG | 29.09.2026 | Brussels Signal 29.09 (poziom 4 – potwierdzić)
- Aleksandar Vučić | dymisja 27.09.2026; lider listy SNS w wyborach 25.10 | 02.10.2026 | Danas; Euronews; OSW 28.09; PISM 1.10
- Ana Brnabić | przewodnicząca parlamentu Serbii, p.o. prezydenta od 27.09; wybory prezydenckie nierozpisane do 3.10 | 03.10.2026 | N1 28.09
- Merz – sondaże | ARD-DeutschlandTrend 28–30.09: 10% zadowolonych, AfD 27%, CDU/CSU 20% – tylko Tagesspiegel, Al Jazeera | 03.10.2026
- Hashim Thaçi | skazany 16.09.2026 na 25 lat (nieprawomocnie) | 24.09.2026 | Al Jazeera 16.09; OSW 24.09
- Ksienija Fiodorowa | na liście sankcyjnej UE od 24.09.2026 | 25.09.2026 | Euronews 24.09
- Wielka Brytania – sondaże 30.09 | Survation Lab 29/Reform 23; YouGov Reform 25/Lab 24 | 30.09.2026 | Al Jazeera 30.09
- Francja – budżet 2027 | 1.10 PROPOZYCJA: deficyt 5,0% PKB, wysiłek 54 mld euro, wzrost 1,0%, dług 121,7%; obrona +6,4 vs +6,5 mld (bez liczby) | 02.10.2026 | Euronews 2.10; Agence Europe 1.10; Reuters 1.10
- Słowacja | 2.10 rada koalicyjna: budżet 2027 (deficyt 4,94% PKB), podatek transakcyjny zniesiony od 1.01.2028; rząd 5.10: budżet i zmiany w MŚ; Kuffa (SNS) jedyny kandydat na ministra środowiska; Taraba odwołany 29–30.09 | 03.10.2026 | TASR 30.09–2.10; Pravda.sk
- Czechy | 1.10 rząd Babiša przetrwał wotum nieufności (83 za, potrzeba 101); numer próby rozbieżny (ČTK vs AP) – bez numeru | 02.10.2026 | AP; ČTK 1.10
- Rumunia | 30.09 parlament odrzucił rząd Mureșana (182, potrzeba 233), trzecia próba; 5.10 prezydent Dan wskazuje kandydata | 03.10.2026 | Agerpres; AFP 30.09; Romania Insider 1.10
- Estonia | 29.09 podpalenie Milrem Robotics (15.08) przypisane Rosji; wezwano chargé | 30.09.2026 | Estonian World 29.09
- Szwecja | Andersson – misja od 5.10, raport do 12.10; głosowanie nad premierem najwcześniej 14.10 (SVT); rząd tymczasowy Kristerssona | 03.10.2026 | riksdagen.se 2.10; SVT 2.10
- Sikorski | MSZ G20 w Atlancie 30–31.10; zaproszenie Putina na G20 „złym pomysłem”, bez bojkotu | 02.10.2026 | WP 30.09; rp.pl 2.10
- Nawrocki | planuje udział w G20 w Miami 14–15.12 (Przydacz 23.09 – do potwierdzenia); 1.10 ustawa o nadmiarowych zyskach koncernów paliwowych podpisana i skierowana do TK | 02.10.2026 | Interia 1.10
- Bartosz Grodecki | szef BBN – do potwierdzenia (prezydent.pl 403) | 02.10.2026
- Siergij Koreckij | wg Reutersa (ABC 1.10) premier Ukrainy – NIEZWERYFIKOWANE | 02.10.2026
- Łukaszenka – ułaskawienia | 24.09 ułaskawił 15 osób; czy są Polacy – nie ustalono | 29.09.2026 | RMF24; Meduza 24.09

## Decyzje i stany spraw
- Ostrzeżenie Rosji dla NATO ws. Kaliningradu | ujawnione 30.09 (Reuters, AP); Pieskow potwierdził; NATO i Rutte potępiają; MSZ RP (Wewiór) 2.10 | 03.10.2026 | AP 30.09; KI 30.09; PAP 2.10
- Putin – Wałdaj 1.10 | groźba użycia „wszystkich rodzajów broni” przy ataku na FR; „nie zamierzamy nikogo atakować” | 02.10.2026 | Euronews 2.10; AFP 1.10
- Mosty w Kijowie | od 1.10 codzienne uderzenia: Południowy (1–2.10), Północny (3 i 4.10) | 04.10.2026 | KI; AP
- MSZ Rosji – ostrzeżenie dla cudzoziemców | ponowione 3.10 | 03.10.2026 | Reuters; AFP 3.10
- Mołdawia | noc 2/3.10: 5 rosyjskich środków napadu eksplodowało na terytorium, bez ofiar | 03.10.2026 | KI; AP 3.10
- URIF (USA–Ukraina) | 2.10 zatwierdzona pierwsza inwestycja (surowce krytyczne; magazyn DTEK 200 MW/400 MWh); kwot nie sprawdzono w komunikacie | 03.10.2026 | DFC; treasury.gov 2.10
- Wypłata KE dla Ukrainy | 2.10: 2,9 mld euro, w tym 800 mln z Ukraine Facility w ramach Ukraine Support Loan | 02.10.2026 | KE IP/26/2047
- G7 – energia | 2.10 PRZYJĘTE: MAE uwalnia 100 mln baryłek w 4 miesiące; utrzymanie sankcji wobec Rosji | 03.10.2026 | consilium 2.10
- Sankcje Wielkiej Brytanii wobec Rosji | 1.10: 31 wpisów; 2.10: 2 statki | 03.10.2026 | gov.uk 1.10 i 2.10
- Estonia – zakaz tranzytu zboża z Rosji i Białorusi | PRZYJĘTE 1.10 | 01.10.2026 | ERR 1.10
- Gripeny nad Polską | od 1.10 na ok. 2 miesiące, F 17; liczby maszyn brak w źródłach urzędowych | 02.10.2026 | regeringen.se 30.09
- Rozporządzenie powrotowe UE | przyjęte ostatecznie 1.10 | 02.10.2026 | consilium 1.10
- Procedury OPL (identyfikacja pozytywna) | w mocy od 1.10.2026 | 02.10.2026 | Reuters 30.09; KI 28.09
- „Ustawa przedwojenna” MON | projekt bez tekstu i komunikatu MON | 03.10.2026 | PAP 2.10; rp.pl 2.10
- Budżet Polski 2027 | przyjęty przez RM 29.09: deficyt 281,2 mld zł, obrona 198,1 mld (4,51% PKB) | 01.10.2026 | KPRM/PAP 29.09
- Dekret Putina o liczebności armii | 28.09: 2 441 630 etatów, w tym 1 550 500 wojskowych | 29.09.2026 | OSW 29.09
- Budżet Rosji 2027–2029 | projekt w Dumie; obrona 2027 17,1 bln rub.; I czytanie 29.10 (Interfax) – brak dwóch niezależnych źródeł | 02.10.2026 | Meduza 30.09; Reuters 28.09
- Iran – USA | 26.09 Trump odrzucił irańską propozycję ws. Ormuzu (AP); 2.10 narada w Camp David (Axios, CBS); tankowiec trafiony u Omanu noc 2/3.10 (UKMTO pośrednio) | 03.10.2026
- Sankcje USA (Iran) | 1.10 Departament Skarbu: 27 podmiotów i osób | 02.10.2026 | treasury.gov 1.10
- USA – finansowanie rządu | do 11.12.2026 (H.R. 6500) | 02.10.2026 | whitehouse.gov
- Oferta produkcji PAC-3 w Polsce | PROPOZYCJA; brak odpowiedzi USA do 2.10 | 02.10.2026
- Rozmowy USA–Rosja–Ukraina | brak nowego terminu do 3.10 | 03.10.2026 | AP 3.10
- Dron w Instytucie Badań Jądrowych w Kijowie | 30.09; reaktor nieuszkodzony; komunikatu MAEA nie otwarto | 03.10.2026 | KI 1.10
- Rozejm handlowy USA–ChRL | przedłużony z 10.11.2026 do 10.01.2027 (Bessent 23.09); dialog o superinteligencji – runda do listopada | 04.10.2026 | Reuters 23.09; ABC 23.09; Biały Dom 25.09
- Ustawa Grahama | podpis 18.09; wdrożenie do 18.10.2026 | 30.09.2026 | PISM Biuletyn 64
- Fundusze UE dla Węgier | 4,2 mld euro – PROPOZYCJA KE 23.09; GAC 13.10 (praworządność HU) | 03.10.2026 | Euronews 23.09; consilium 2.10
- EPF 6,6 mld euro | 25.09 porozumienie polityczne w KPiB; formalnej decyzji Rady brak do 3.10 | 03.10.2026 | Euronews 25.09
- Sankcje UE | 21. pakiet (lipiec 2026); nowego brak do 3.10 | 03.10.2026 | consilium 23.07
- WRF 2028–34 | propozycja KE ok. 1,76 bln euro; Polska 123 mld (PAP 30.09); list 17 państw Przyjaciół Spójności 2.10 – tylko Agence Europe | 03.10.2026
- Budżet Ukrainy 2027 | projekt rządu: obrona 4,8 bln UAH (wg PISM 1.10) | 02.10.2026 | PISM 1.10
- AfD – rozmowy gazowe z Rosją | Reuters 18.09; Frohnmaier 28.09 | 01.10.2026 | ANSA 29.09
- Umowa USA–Dania–Grenlandia | podpisana 22.09.2026 | 25.09.2026
- Litwa – art. 137 | głosowania 6.10.2026 i 12.01.2027 wg LRT (jedno źródło); potrzeba 94 ze 141 | 03.10.2026 | LRT 22.09
- Rada UE (Forward look 2.10) | 8.10 Eurogrupa; 9.10 ECOFIN; 12.10 FAC; 13.10 GAC; 15–16.10 Rada Europejska | 03.10.2026 | consilium 2.10
- Inne terminy | MSZ G20 Atlanta 30–31.10; EPC Dublin 12.11 (agent – potwierdzić); zgromadzenia MFW/BŚ 12–18.10 (imf.org); midterms USA 3.11 | 30.09.2026
- Stopy | NBP 3,75%; Fed 3,75–4,00% (FOMC 27–28.10); EBC depozytowa 2,50% (28–29.10, 16–17.12); RPP 6–7.10, 3–4.11, 1–2.12 (nbp.pl 403) | 03.10.2026
- CPI Polska | flash wrzesień 4,0% r/r; pełne dane 14.10 | 03.10.2026 | GUS 30.09
- Podpalenie stacji Starlink, Wola Krobowska | 23.09; brak zatrzymań do 2.10 | 02.10.2026 | rp.pl 2.10

## Oceny (z autorem i datą)
- DDIS (Ahrenkiel), 24.09: ryzyko ograniczonego ataku Rosji na państwa NATO graniczące z Rosją „niskie, ale rosnące”
- ISW 29–30.09: zimowa kampania uderzeń na infrastrukturę; ISW 1.10 (za Kyiv Post): wrzesień – najwyższe w 2026 straty Rosji
- OSW, Strachota, 1.10: Iran – walka o Ormuz i wyczerpanie gospodarcze (omówione w wyd. 14)
- PISM, Balawajder, Biuletyn 67 (3201), 1.10: „strategiczna stabilizacja” USA–Chiny (omówione w wyd. 14)
- PISM, Zając, Komentarz 1.10: RN w Senacie (omówione w wyd. 14)
- Rutte, 30.09: „preferencja europejska” to „luksus”

## Rozbieżności
- Ostrzeżenie ws. Kaliningradu – forma i data wysłania pisma | 02.10.2026
- Seszták – kwota 11 vs 12 mld Ft | 30.09.2026
- Dekret Putina – suma zwiększeń w 2026 | 30.09.2026
- Serbia – ostatni termin wyborów prezydenckich: 26.12 vs 27.12 | 28.09.2026
- Czechy – która to próba wotum nieufności | 01.10.2026
- Francja – obrona +6,4 vs +6,5 mld | 02.10.2026
- Łotwa – podział mandatów mniejszych partii LSM vs Al Jazeera; frekwencja 51,8% tylko Reuters | 04.10.2026
- Bośnia – frekwencja rozbieżna w mediach lokalnych | 04.10.2026

## Do weryfikacji
- Łotwa – oficjalne wyniki CVK i koalicja; Bośnia – wyniki CIK; OPEC+ 4.10 – drugie źródło z poziomów 1–2
- Rumunia – kandydat na premiera 5.10; Słowacja – rząd 5.10 i nominacja Kuffy; Costa w Warszawie 5.10 – przebieg
- Litwa 6.10 – czy głosowanie się odbyło; Szwecja – misja Andersson
- Budżet Rosji 2027–29 – drugie niezależne źródło; dron w Instytucie Badań Jądrowych – komunikat MAEA
- Węgry – Hankó (poziom 1–2), kandydat na PG; Bergen Group w Polsce – MON/DoD; „ustawa przedwojenna” – tekst MON
- WRF – stanowisko rządu RP przed RE 15–16.10; odpowiedź USA na ofertę PAC-3; Polacy wśród ułaskawionych na Białorusi
- Serbia – rozpisanie wyborów prezydenckich; formalna decyzja Rady ws. EPF 6,6 mld; status premiera Ukrainy (Koreckij?)
- APEC Shenzhen 18–19.11 – udział Trumpa (źródło poziomu 1–2)

## Dziennik korekt (skrót; pełny rejestr korekt na stronie korekty.html)
- 24.09 (wyd. 4–5): Poczobut; fundusze dla Węgier (propozycja); data dymisji Vučicia.
- 25.09 (tygodniówka nr 2): Jedna Rosja 355→349; Sikorski 25.09→24.09.
- 01.10: rewizja archiwum (dane/rewizje.json) – w tym błędne wycofanie szczytu Trump–Xi (2026-09-25#z1), przywrócone 4.10.
- 01.10 (wyd. 12): Biuletyn PISM nr 65 to (3199).
- 04.10 (wyd. 15): korekta – szczyt Trump–Xi przywrócony w wydaniu z 25.09; straże kompletności od 5.10.
