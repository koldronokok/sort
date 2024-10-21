#first Ukrainian word second English word or other
#don't worry about up or low figures
#creat new def, I think,don't use sort()
from googletrans import Translator

transl = Translator()

MyList = ['English', 'інформація', 'android', 'Windows', 'Добрий день', 'матриця',
'актова зала', 'біоресурси', 'єдиний', 'кава']
#transl.detect(text)).lang
sort1 = []
sort2 = []
sort3 = []
for word in MyList:
    if (transl.detect(word).lang == 'uk'):
        sort1.append(word)
    elif (transl.detect(word).lang == 'en'):
        sort2.append(word)
# Український алфавіт
ukrainian = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя'
english = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
sort_uk = []
sort_en = []
for figures in ukrainian:
    for word in sort1:
        if figures == word[0]:
            sort_uk.append(word)
for figures in english:
    for word in sort2:
        if figures == word[0]:
            sort_en.append(word)
sort=sort_uk+sort_en
print(sort)




