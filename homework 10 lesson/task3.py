import copy

def sdvig_spiska():
    spisok = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']
    n = int(input('vvedite koli4estvo simvolov: '))
    array = copy.deepcopy(spisok)
    if n > 0:
        for i in range(len(spisok)):
            # первый иф проверяет если мы хотим сдвинуть список из 5 элементов на 8 позиций и оставляет 8-5 = 3, чтоб внутри не ломалось
            if abs(n) > int(len(spisok)):
                n = abs(n) - (abs(n) // int(len(spisok))) * int(len(spisok))
            if i + n < int(len(spisok)):
                spisok[i] = array[i + n]
            else:
                spisok[i] = array[i + n - int(len(spisok))]
    if n < 0:
        for i in range(len(spisok)):
            # тут первый иф аналогичная проверка но для отрицатеотных чисел
            if abs(n) > int(len(spisok)):
                n = -(abs(n) - (abs(n) // int(len(spisok))) * int(len(spisok)))
            if i - n > 0:
                 spisok[i] = array[i - abs(n)]
            else:
                spisok[i] = array[i - abs(n) + int(len(spisok))]
    print(spisok)


sdvig_spiska()