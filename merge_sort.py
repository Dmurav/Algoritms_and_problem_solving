import datetime

start = datetime.datetime.now()

steps = 0

def mergesort(lst) -> list:
    """Функция принимает на вход список,
    возвращает сортированный список"""
    global steps
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            steps += 1
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            steps += 1
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            steps += 1
            lst[k] = right[j]
            j += 1
            k += 1
    return lst


end = datetime.datetime.now()


if __name__ == '__main__':
    array = [4, 2, 7, 1, 3, 45, 22, 8, 3, 43, 22, 11, 23]
    print(mergesort(array))
    print('Алгоритм провёл сортировку списка за ' + str(steps) + ' шага(ов)')
    print("Алгоритм справился за " + str((end - start).microseconds) + ' микросекунд')
    print('Поскольку число элементов списка - ' + str(len(array)) + ', a количество шагов алгоритма - ' '\n'
          + str(steps) + ', следует, что вычислительная сложность алгоритма - O(nlogn)')