"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def decimal_to_binary(user_number):
    binary = []
    while user_number > 1:
        binary.insert(0, user_number % 2)
        user_number //= 2
    binary.insert(0, user_number)
    return binary


def binary_str(user_number):
    result = ""
    while user_number > 1:
        result = str(user_number % 2) + result
        user_number //= 2
    result = str(user_number) + result
    return result


print(f"45 -> {decimal_to_binary(45)} -> {binary_str(45)}")
print(f"3 -> {decimal_to_binary(3)} -> {binary_str(3)}")
print(f"2 -> {decimal_to_binary(2)} -> {binary_str(2)}")

