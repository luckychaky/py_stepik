'''
Выведите таблицу размером 
n
×
n
n×n, заполненную числами от 
1
1 до 
n
2
n 
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь 
n
=
5
n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

'''
number = int(input())
new_matrix = [[0]*number for i in range(number)]
count = 0
m = 0
n = 0

while count != number ** 2:
    for j in range(m, number + n): # движение вправо
        count += 1
        new_matrix[0 + m][j] = count
    for i in range(1 + m, number + n): # движение вниз
        count += 1
        new_matrix[i][number -1 + n] = count   
    for j in range(number - 2 + n, - 1 + m, -1): # движение влево
        count += 1
        new_matrix[number - 1 + n][j] = count
    for i in range(number - 2 + n, 0 + m, -1): # движение вверх
        count += 1
        new_matrix[i][0 + m] = count  
    m += 1 # для перехода на следующий виток
    n -= 1 # для перехода на следующий виток
for i in new_matrix: # вывод полученной матрицы
    print(*i)
