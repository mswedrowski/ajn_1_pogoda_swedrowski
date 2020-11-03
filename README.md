### [C]

```
Micha l Pogoda
Micha l Swedrowski
```
## Lista 1

```
Analiza jezyka naturalnego, 19/
November 3, 2020
```
# 1 Budowa w lasnego tokenizatora

## 1.1 Cel

Celeme zadania jest zbudowanie tokenizatora, pozwalajacego segmentowa ́c ciag ly tekst na pojedy ́ncze
tokeny. Token jest pojedy ́nczym s lowem lub wyra ̇zeniem i w tek ́scie poddanym tokenizacji kazdy zaczyna
sie od nowej linii. Koniec ka ̇zdego zdania jest oznaczony znakiem< eos >.

## 1.2 Opis algorytmu

1.2.1 Architektura rozwiazania

Tokenizator zaprojektowany w ramach zaje ́c posiada modu lowa architekture kaskadowa. Ka ̇zdy modu l
na wej ́sciu przyjmuje tokeny z poprzedniego etapu, a na wyj ́sciu podaje zmodyfikowane tokeny. Akcje,
jakie wykonuje ka ̇zdy modu l mo ̇zna przypisa ́c do jednej z 5 kategorii:

- Rodzielnie tokenu: Podzia l tokenu na jeden lub wiecej token ́ow
- Laczenie token ́ow: Po laczenie dw ́och lub wiecej token ́ow w jeden
- Usuniecie tokenu
- Wstawienie tokenu
- Zamiana tokenu

Podstawa takiej architektury jest idea, ̇ze ka ̇zdy z etap ́ow procesu iteracyjnie polepsza jako ́s ́c tokenizacji.
Rozwiazuja ́c pewien przypadek szczeg ́olny. Dzieki takiej architekturze mo ̇zemy t ́ownie ̇z dowolnie w lacza ́c
lub wy lacza ́c poszczeg ́olne etapy, dostosowuja ́c tokenizator do konretnych porzeb.

1.2.2 Przebieg tokenizacji

Przebieg tokenizacji mo ̇zna okre ́sli ́c w nastepujacy spos ́ob:

1. Wczytanie tekstu - W poczatkowym etapie ca ly tekst traktowany jest jako pojedy ́nczy token.
2. Podzia l na pojedy ́ncze tokeny wzgledem zak ́ow bia lych (whitespace). Przyjmujemy za lo ̇zenei, ̇ze
    znaki bia le takie jak spacje czy nowe linie stanowia najbardziej podstawowy i naturalny podzia l na
    tokeny
3. Podziale na zdania wzgledem predefiniowanych znak ́ow oznaczajacych koniec zdania - W tym etapie
    brane sa pod uwage tak ̇ze wyjatki, najcze ́sciej w postaci skr ́ot ́ow takich jak np. czy tys.
4. Zamianie skr ́ot ́ow na pe lne formy wyrazu na podstawie predefiowanych s lownik ́ow - Dzieki temu
    etapowi, mo ̇zemy ujednolici ́c forme skr ́otowa z pe lna forma wyrazu. Przyk ladowo ”tys” zamieniamy
    na ”tysiac”.
5. Konkatenacja token ́ow bedacych pojedy ́nczymi wyrazami do jednego tokenu. Bierzemy tutaj
    zwroty, w kt ́orych interpretacja poszczeg ́olnych s l ́ow nie ma wiekszego sensu. Np. ”sta lo sie”,
    czy nazwy w lasne takie jak ”Kongres Narodowy”.
6.Opcjonalnie Wszystkie tokeny moga posiada ́c tylko ma le litery
7. Opcjonalnie Usuniecie znak ́ow interpunktyjnych na podstawie predefiniowanej listy znak ́ow

W rozwiazaniach opartych na bazie wiedzy (np. lista skr ́ow, lista sformu lowa ́n) opracowane zosta ly
po 1-2 przyk ladowe przypadki, wystepujace w analizowanym tek ́scie. Jako tekst bazowy pos lu ̇zy l wpis
”Albania59.txt” ze zbioru danych ”Wiki34”,


## 1.3 Przyk ladowe dzia lanie

```
Tekst bazowy
Albania jest cz lonkiem ONZ, NATO, OBWE, Rady Europy, WTO oraz np. jednym z za lo ̇zycieli Unii
na rzecz Regionu MorzaSr ́odziemnego. ́
```
```
Uzyskane tokeny
albania — jest — cz lonkiem — organizacja narod ́ow zjednoczonych — , — nato — , — obwe — , —
rady — europy — , — wto — oraz — np — jednym — z — za lo ̇zycieli — unii — na — rzecz —
regionu — morza — ́sr ́odziemnego —< eos >
```
## 1.4 Podsumowanie

Powy ̇zsze zadanie pokaza lo, ̇ze stworzenie dobrego tokenizatora nie jest trywialnym zadaniem. Kon-
struowanie tokenizator ́ow opartych na regu lach wydaje sie by ́c zaskakujaco dobrym rozwiazaniem, nie
mniej jednak wymaga u ̇zycia sporej ilo ́sci regu l. Posiadajac odpowiednie zasoby (s lowniki) tokenizator
oparty na regu lach mo ̇ze by ́c niezwykle efektywny. Segmentacja tekstu na poziomie zda ́n czy paragraf ́ow
jest trudniejszym zadaniem ni ̇z segmentacja na pojedy ́ncze tokeny.


# 2 Por ́ownanie Tagger ́ow

## 2.1 U ̇zyte taggery

Do zadania u ̇zyto tager ́ow :

- Morphodita
- WCRFT
- CMCT

Do tagowania u ̇zyto serwis ́ow udostepnionych przez organizacje CLARIN. Serwisy te podejmuja ca lo ́sciowa
analize morfosyntaktyczna, wiec obejmuja r ́ownie ̇z proces tokenizacji. Z tego powodu okre ́slone zosta ly
metryki dolne (przy za lo ̇zeniu ̇ze wszystkie r ́o ̇zniace sie tokeny zosta ly sklasyfikowane ́zle) i g ́orne (wszys-
tkie r ́o ̇zniace tokeny sklasyfikowane dobrze).

2.1.1 Zapytania LPMN

wcrft: wcrft2({"guesser": false, "morfeusz2": true})
morphodita: morphoDita({"guesser": false, "allforms": false, "model": "XXI"})
cmct: maca({"morfeusz2": true})|cmct({"full_output": false})

## 2.2 Preprocesing

Przed wykonaniem ewaluacji do taksetu NKJP dodano nastepujace tagi: DIG i ROMANDIG oznaczajace
odpowiednio cyfry i cyfry rzymskie. Taki zabieg wynika l z faktu, ̇ze dane GOLD ze zbioru Poleval 2017
cyfry/liczby oznacza ly pe lnym tagsetem, tak jakby by ly pisane. Natomiast tagery morphodita, WCRFT
i CMCT traktowa ly cyfry jako nieodmianialne symbole. Druga zmiana by la podmiana tag ́ow wyra ̇zenia
przymiotnikowego z adjp:dat na adjp w przypadku tagera CMCT

## 2.3 Ewaluacja

Do ewaluacji tager’ ́ow wybrany zosta l zbi ́or konkursowy PolEval 2017. Sam proces ewaluacji jest wykony-
wany zgodnie ze skryptem udostepnionym przez organizatora konkursu. W ramach zaje ́c zosta lo przygo-
towane r ́ownie ́s ́srodowisko docker pozwalajace uruchomi ́c wsponiany skrypt na badanych tagerach

```
Metryka Morphodita WCRFT CMCT
POS Accuracy 90.65% 65.11% 90.00%
Lemmatization Accuracy 97.09% 90.92% 73.42%
Overall accuracy 93.87% 78.02% 81.71%
```
```
Table 1: Miary klasyfikacyjne badanych tagger ́ow na poszczeg ́olnych zadaniach
```

## 2.4 Podsumowanie

Niekwestionowalnie najlepszy, tagerem spo ́sr ́od badanych jest Morphodita, kt ́ora uzysak la najwy ̇zsze
wyniki miary Accuracy na ka ̇zdym z podzada ́n. Je ̇zeli chodzi o tagery WCRFT i CMCT, cie ̇zko obiek-
tywnie wybra ́c kt ́ory jest lepszy. Tagger WCRFT uzyska l znaczaco lepsza dok ladno ́s ́c lematyzacji, nato-
miast CMCT lepiej poradzi l sobie w zadaniu ̈Part-Of-Speech tagging ̈.


# 3 Por ́ownanie wp lywu dzia lania poszczeg ́olnych tager ́ow jako

# narzedzi wstepnego przetwarzania tekstu na wyniki klasy-

# fikacji

## 3.1 Grupowanie klas gramatycznych

W celu przeprowadzenia ́cwiczenia klasy gramatyczne domy ́slnego tagsetu nkjp zosta ly pogrupowanie w
nastepujacy spos ́ob

```
Rzeczowniki
```
- < subst >rzeczowniki
- < depr >deprecjactywna forma rzeczownika
- < ger >ods lownik
    Czasowniki
- < f in >nie przesz la forma czasownika
- < praet >pseudoimies l ́ow
- < bedzie >forma przysz la czasownika ”by ́c”
- < impt >rozka ́znik
- < imps >bezosobnik
- < inf >czasownik w formie bezokolicznika
    Przymiotniki
- < adja >przymiotnik przyprzymiotnikowy
- < adjp >przymiotnik poprzyimkowy
- < adjc >przymiotnik predykowany
- < adj >przymiotnik
- < pact >przymiotnik w formie imies lowu przymiotnikowego
- < ppas >przymiotnik w formie imies lowu przymiotnikowego w formie przesz lej


## 3.2 Klasyfikacja

Do przeprowadzenia klasyfikacji zosta l u ̇zyty klasyfikator wieloklasowy naiwnego bayesa z bibliteki scikit-
learn. Do ewaluacji pos lu ̇za dane korpusu Wikipedii z CLARIN. Prezentowane metryki to ́srednie wa ̇zone
wzgledem ilo ́sci klas.

```
Metryka Morphodita WCRFT CMCT
Precision 88.00% 88.00% 88.00%
Recall Accuracy 87.00% 87.00% 86.00%
F-score 88.00% 86.00% 86.00%
```
Table 2: Wyniki klasyfikacji kategorii tekst ́ow uzyskanych za pomoca badanych tagger ́ow na postawie
rzeczownik ́ow

```
Metryka Morphodita WCRFT CMCT
Precision 52.00% 52.00% 52.00%
Recall Accuracy 42.00% 43.00% 42.00%
F-score 41.00% 42.00% 41.00%
```
Table 3: Wyniki klasyfikacji kategorii tekst ́ow uzyskanych za pomoca badanych tagger ́ow na postawie
czasownik ́ow

```
Metryka Morphodita WCRFT CMCT
Precision 80.00% 79.00% 79.00%
Recall Accuracy 76.00% 76.00% 76.00%
F-score 76.00% 76.00% 76.00%
```
Table 4: Wyniki klasyfikacji kategorii tekst ́ow uzyskanych za pomoca badanych tagger ́ow na postawie
przymiotnik ́ow


## 3.3 Podsumowanie

Jak mo ̇zna zauwa ̇zy ́c, klasyfikowanie tekst ́ow na podstawie rzeczownik ́ow daje najlepsze efekty. Wydaje
sie to by ́c naturalne, z uwagi na fakt, ̇ze rzeczowniki dla poszczeg ́olnych temat ́ow sa zazwyczaj r ́o ̇zne,
czego nie mo ̇zna powiedzie ́c o czasownikach (przyk ladowo czasownik by ́c, kt ́ory z du ̇zym prawdopodobie ́nstwem
bedzie wystepowa l w ca lym tek ́scie. Klasyfikacja tekstu przy pomocy przymiotnik ́ow r ́ownie ̇z jest
znacznie efektywniejsza ni ̇z przy pomocy rzeczownik ́ow, co zdaje sie by ́c pochodna zale ̇zno ́sci pomiedzy
rzeczownikami a czasownikami.


