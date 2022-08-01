'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий: В первой строке указано целое число n n — количество завершенных игр. После этого идет n n строк, в которых записаны результаты игры в следующем формате: Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом: Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:
'''
output = {}
games = []
count_game = int(input())
for i in range(0, (count_game)):
    games.append(input().split(';'))
for game in games:    #в словарях не может быть одинаковых ключей, поэтому формируется словарь с уникальными командами
    output[game[0]] = ''    # присвоили в словрь ключ (команду) и пустое значение игр
    output[game[2]] = ''

for key in output: #для ключа (команды) из словаря
    all_games = 0
    win = 0
    draw = 0
    defeat = 0
    for game in games: #перебираем игры в списке
        all_games += game.count(key)
        if key == game[0]:
            if int(game[1]) < int(game[3]):
                draw += 1
                output[key] = str(all_games) + ' ' + str(win) + ' ' + str(defeat) + ' ' + str(draw) + ' ' + str((win * 3) + defeat)
            elif int(game[1]) > int(game[3]):
                    win += 1
                    output[key] = str(all_games) + ' ' + str(win) + ' ' + str(defeat) + ' ' + str(draw) + ' ' + str((win * 3) + defeat)
            else:
                defeat += 1
                output[key] = str(all_games) + ' ' + str(win) + ' ' + str(defeat) + ' ' + str(draw) + ' ' + str((win * 3) + defeat)
        if key == game[2]:
            if int(game[1]) < int(game[3]):
                win += 1
                output[key] = str(all_games) + ' ' + str(win) + ' ' + str(defeat) + ' ' + str(draw) + ' ' + str((win * 3) + defeat)
            elif int(game[1]) > int(game[3]):
                    draw += 1
                    output[key] = str(all_games) + ' ' + str(win) + ' ' + str(defeat) + ' ' + str(draw) + ' ' + str((win * 3) + defeat)
            else:
                defeat += 1
                output[key] = str(all_games) + ' ' + str(win) + ' ' + str(defeat) + ' ' + str(draw) + ' ' + str((win * 3) + defeat)
    print(key + ':' + output[key])

