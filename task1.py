"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def division(a, b):
    return a / b


number_a = input("Введите числитель (делимое): ")
while not is_float(number_a):
    print(f"Вы ввели: {number_a}")
    number_a = input("Введите число: ")
number_a = float(number_a)
number_b = input("Введите числитель (делимое): ")
while not is_float(number_b) or int(number_b) == 0:
    print(f"Вы ввели: {number_b}")
    number_b = input("Введите число, отличное от нуля: ")
number_b = float(number_b)

result = round(division(number_a, number_b), 2)
print(f"Результат деления {number_a} на {number_b} равен {result}")


