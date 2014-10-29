# -*- coding:UTF-8 -*-
__author__ = 'User'

#нужно выделить из строки с количеством результатов числовое значение
text = "Найдено: 1000"
text = text[16:]
print text
if int(text)>0:
    print "Yes"
else:
    print "No"

int(text[16:])