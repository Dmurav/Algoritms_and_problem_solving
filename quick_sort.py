import datetime

start = datetime.datetime.now()
steps = 0


def quicksort(lst) -> list:
    """Функция получает на вход несортированный список,
    возвращает отсортированный список"""
    less = []
    equal = []
    greater = []
    global steps
    if len(lst) > 1:
        pivot = lst[0]
        for item in lst:
            steps += 1
            if item < pivot:
                less.append(item)
            elif item == pivot:
                equal.append(item)
            else:
                greater.append(item)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return lst


end = datetime.datetime.now()


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 45, 22, 8, 3, 43, 22, 11, 23]
    print(quicksort(array))
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд(ы)')
    print('Алгоритм провёл сортировку списка за ' + str(steps) + ' шага(ов)')
    print('Поскольку число элементов списка - ' + str(len(array)) + ', a количество шагов алгоритма - ' '\n'
          + str(steps) + ', следует, что вычислительная сложность алгоритма - O(nlogn)')

