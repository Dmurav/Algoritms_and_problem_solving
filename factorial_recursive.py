#!/usr/bin/python3

steps = 0


def factorial(n):
    """Функция принмает на вход число
            и возвращает факториал данного числа"""
    global steps
    steps += 1
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    n = int(input("Введите число: "))
    print(factorial(n))
    print('Поскольку количество шагов алгоритма - ' '\n'
          + str(steps) + ', вычислительная сложность алгоритма - O(n)')