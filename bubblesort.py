import datetime

start = datetime.datetime.now()


def bubble_sort(lst)->list:
    """Возвращает отсортированный список"""
    steps = 0
    for number in lst:
        for index in list(range(len(lst) - 1)):
            steps += 1
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    print('Алгоритм провёл сортировку списка за ' + str(steps) + ' шага(ов)')
    print('Поскольку число элементов списка - ' + str(len(lst)) + ', a количество шагов алгоритма - ' '\n'
          + str(steps) + ', следует, что вычислительная сложность алгоритма - O(n2)')
    return lst

end = datetime.datetime.now()

if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 45, 22, 8, 3, 43, 22, 11, 23]
    print(bubble_sort(array))
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд')
