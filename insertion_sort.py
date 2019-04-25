import datetime

start = datetime.datetime.now()

steps = 0

#Сортировка вставками работает очень быстро на почти упорядоченных массивах
def insertion(lst)-> list:
    """Функция получает на вход неотсортированный список,
    а возвращает отсортированный методом вставок"""
    global steps
    for i in range(len(lst)):
        j = i - 1
        key = lst[i]
        while lst[j] > key and j >= 0:
            steps += 1
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


end = datetime.datetime.now()


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 45, 22, 8, 3, 43, 22, 11, 23]
    print(insertion(array))
    print('Алгоритм провёл сортировку списка за ' + str(steps) + ' шага(ов)')
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд')
    print('Поскольку число элементов списка - ' + str(len(array)) + ', a количество шагов алгоритма - ' '\n'
          + str(steps) + ', следует, что вычислительная сложность алгоритма - O(n2)')

