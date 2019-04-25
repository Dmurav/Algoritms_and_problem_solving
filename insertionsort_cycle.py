import datetime

start = datetime.datetime.now()

steps = 0


#Сортировка вставками работает очень быстро на почти упорядоченных массивах
def insertion(arr):
    """Функция получает на вход неотсортированный список,
        а возвращает отсортированный методом вставок"""
    global steps
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for g in range(0, i):
                if arr[g] > arr[i]:
                    steps += (i - g)
                    arr.insert(g, arr.pop(i))
    return arr


end = datetime.datetime.now()


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 45, 22, 8, 3, 43, 22, 11, 23]
    print(insertion(array))
    print('Алгоритм провёл сортировку списка за ' + str(steps) + ' шага(ов)')
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд')
    print('Поскольку число элементов списка - ' + str(len(array)) + ', a количество шагов алгоритма - ' '\n'
          + str(steps) + ', следует, что вычислительная сложность алгоритма - O(n2)')