"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
"""


def is_int_plus(number):
    try:
        int(number)
    except ValueError:
        return False
    if int(number) > 0:
        return True
    else:
        return False


def is_int_minus(number):
    try:
        int(number)
    except ValueError:
        return False
    if int(number) < 0:
        return True
    else:
        return False


def my_func(x, y):
    result = x
    for i in range(1, -y):
        result *= x
    return 1 / result


x = input("Введите число, которые хотите возвести в степень: ")
while not is_int_plus(x):
    print(f"Вы ввели: {x}")
    x = input("Введите целое положительное число: ")
x = int(x)

y = input("Введите целое отрицательное число - степень: ")
while not is_int_minus(y):
    print(f"Вы ввели: {y}")
    y = input("Введите целое отрицательное число: ")
y = int(y)

print(f"Результат возведения числа {x} в степень {y} равен: {my_func(x, y)}")


