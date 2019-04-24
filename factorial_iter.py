#!/usr/bin/python3

steps = 0


def factorial(n):
    """Функция принмает на вход число
        и возвращает факториал данного числа"""
    prod = 1
    global steps
    for i in range(1, n+1):
        steps += 1
        prod *= i
    return prod


if __name__ == '__main__':
    n = int(input("Введите число: "))
    print(factorial(n))
    print('Поскольку количество шагов алгоритма - ' '\n'
          + str(steps) + ', вычислительная сложность алгоритма - O(n)')
