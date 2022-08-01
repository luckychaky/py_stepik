'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac
'''

s1 = input()
s2 = input()
s3 = input()
s4 = input()
string_output = []
dict_encrypt = {}
dict_decipher = {}
# s1 = 'abcd'
# s2 = '*d%#'
# s3 = 'abacabadaba'
# s4 = '#*%*d*%'
for i in range(len(s1)):
    dict_encrypt[s1[i]] = s2[i]
for i in range(len(s3)):
    print(dict_encrypt[s3[i]], end= "")
print()    
def get_key(dict, chr):
    for key, value in dict.items():
        if value == chr:
            return key
for i in range(0, len(s4)):
    print(get_key(dict_encrypt, s4[i]), end= '')
