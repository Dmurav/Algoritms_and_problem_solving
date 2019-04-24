#!/usr/bin/python3

steps = 0


def fibonacci(n):
    """Функция принмает на вход номер числа
        в последовательности Фибоначчи и возвращает
        число Фибоначчи"""
    global steps
    a = 0
    b = 1
    for number in range(n):
        steps += 1
        a = a + b
        b = a - b
    return a


if __name__ == "__main__":
    n = int(input("Введите номер числа в последовательности Фибоначчи: "))
    print(fibonacci(n))
    print('Поскольку количество шагов алгоритма - ' '\n'
          + str(steps) + ', вычислительная сложность алгоритма - O(n)')

