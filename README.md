# NLP - Projekt 1 | Michał Swędrowski, Michał Pogoda

# 1. Tokenizer
Celeme zadania jest zbudowanie tokenizatora, pozwalającego segmentować ciągły tekst na pojedyńcze tokeny. 

# 2. Morfeusz
Zapoznać się z narzędziem morfeusz

# 3. Ewaluacja 3 taggerów
Do zadania użyto tagerów :
- Morphodita
- WCRFT
- CMCT
Do tagowania użyto serwisów udostępnionych przez organizację CLARIN. Serwisy te podejmują całościową analizę morfosyntaktyczną, więc obejmują również proces tokenizacji. Z tego powodu określone zostały metryki dolne (przy założeniu że wszystkie różniące się tokeny zostały sklasyfikowane źle) i górne (wszystkie różniące tokeny sklasyfikowane dobrze). 

# 4. Wykorzystanie i porównanie taggerów w zadaniu klasyfikacji
Do przeprowadzenia klasyfikacji został użyty klasyfikator wieloklasowy naiwnego bayesa z bibliteki \href{https://scikit-learn.org/stable/modules/multiclass.html}{scikit-learn}. Do ewaluacji posłużą dane "Wikipedia 34". 

