'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество 
d
d известных нам слов, после чего на 
d
d строках указываются эти слова. Затем передаётся количество 
l
l строк текста для проверки, после чего 
l
l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:
stepic
champignons
the

'''

string_1 = []
string_2 = []
lst= []
d = int(input())

for i in range(d):
    string_1.append(input().lower())

l = int(input())

for j in range(l):
    string_2.append(input().lower())

for word in string_2:
    for i in word.split():
        if i not in string_1 and i not in lst:
            lst.append(i)
            print(i)
