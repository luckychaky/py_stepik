'''
Напишите программу, которая считывает список чисел 
l
s
t
lst из первой строки и число 
x
x из второй строки, которая выводит все позиции, на которых встречается число 
x
x в переданном списке 
l
s
t
lst.

Позиции нумеруются с нуля, если число 
x
x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5
Sample Input 2:
5 8 2 7 8 8 2 4
10
Sample Output 2:
Отсутствует
'''

list = [int(i) for i in input().split()]
number = int(input())
new_list = []
start = 0
if number in list:
    for i in list:
        if i == number:
          ind = list.index(i, start)
          new_list.append(ind)
          start = ind + 1
    print(*new_list)
else:
    print("Отсутствует")
