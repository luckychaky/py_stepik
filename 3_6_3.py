'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests
with open('/Users/vitalyskiba/Downloads/dataset_3378_3.txt') as inf:
    s = inf.read().strip().split()
r = requests.get(s[0])
print(r.text) # содерит ИМЯ в виде конца ссылки вида урл/ + ИМЯ
while not r.text.startswith('We'):
    r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + r.text)
print(r.text)

'''
We are the champions, my friends,
And we'll keep on fighting 'til the end.
We are the champions.
We are the champions.
No time for losers
'Cause we are the champions of the world.
'''
