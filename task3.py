"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_a, arg_b, arg_c):
    if arg_a >= arg_b:
        if arg_b >= arg_c:
            return arg_a + arg_b
        else:
            return arg_a + arg_c
    elif arg_a >= arg_c:
        return arg_a + arg_b
    else:
        return arg_b + arg_c


print(f"Сумма двух наибольших чисел из '15' 20' '30' равна: {my_func(15, 20, 30)}")

