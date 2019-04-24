import datetime

start = datetime.datetime.now()


def linear_search(lst, x) -> int:
    """функция берёт на вход несортированный список и искомый элемент и
    возвращает индекс искомого элемента"""
    steps = 0
    for number in lst:
        steps += 1
        if x == number:
            print('Алгоритм нашёл искомый элемент за ' + str(steps) + ' шага(ов)')
            print('Пскольку количество шагов алгоритма - ' + str(steps) + ' и искомый элемент имеет индекс ' + str(lst.index(x)) + ', ' + '\n'
                  + 'следует, что вычислительная сложность алгоритма - O(n)')
            return lst.index(number)
            break
    print('Алгоритм проверил список за ' + str(steps) + ' шага(ов)')
    return None


end = datetime.datetime.now()


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 45, 22, 8, 3, 43, 22, 11, 23]
    index = linear_search(array, 12)
    if index != None:
        print('Индекс искомого числа - ' + str(index))
    else:
        print('В списке нет искомого числа')
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд')


