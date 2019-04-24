import datetime

start = datetime.datetime.now()


def binary_search(lst, x) -> int:
    """осуществляет бинарный поиск элемента со значением равным x
    в сортированном списке"""
    steps = 0
    lower_bound = 0
    upper_bound = len(lst) - 1
    while lower_bound <= upper_bound:
        steps += 1
        index_medium = int((upper_bound + lower_bound) // 2)
        medium_number = lst[index_medium]
        if x < medium_number:
            upper_bound = index_medium - 1
        elif x > medium_number:
            lower_bound = index_medium + 1
        else:
            print('Алгоритм нашёл искомый элемент за ' + str(steps) + ' шага(ов)')
            print('Поскольку число элементов списка - ' + str(len(lst)) + ', a количество шагов алгоритма - ' '\n'
                  + str(steps) + ', следует, что вычислительная сложность алгоритма - O(log n)')
            return lst.index(medium_number)
    print('Алгоритм нашёл искомый элемент за ' + str(steps) + ' шага(ов)')
    print('Поскольку число элементов списка - ' + str(len(lst)) + ', a количество шагов алгоритма - ' '\n'
          + str(steps) + ', следует, что вычислительная сложность алгоритма - O(log n)')
    return None


end = datetime.datetime.now()


if __name__ == '__main__':
    array = [1, 2, 3, 3, 4, 7, 8, 11, 22, 22, 23, 43, 45]
    index = binary_search(array, 22)
    if index != None:
        print('Индекс искомого числа - ' + str(index))
    else:
        print('В списке нет искомого числа')
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд')


