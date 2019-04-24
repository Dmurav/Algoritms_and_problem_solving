#!/usr/bin/python3

steps = 0


def fibonacci_recursive(n) -> int:
    """Функция принмает на вход номер числа
    в последовательности Фибоначчи и возвращает
    число Фибоначчи"""
    global steps
    steps += 1
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == '__main__':
    n = int(input("Введите номер числа в последовательности Фибоначчи: "))
    print(fibonacci_recursive(n))
    print('Поскольку количество шагов алгоритма - ' '\n'
          + str(steps) + ', вычислительная сложность алгоритма - O(n2)')

