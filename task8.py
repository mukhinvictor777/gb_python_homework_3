"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""


def multiply_pairs(incoming_list):
    result = []
    length = len(incoming_list)
    if length % 2 == 0:
        for i in range(0, length // 2):
            result.append(incoming_list[i] * incoming_list[length - i - 1])
    else:
        for i in range(0, length // 2 + 1):
            result.append(incoming_list[i] * incoming_list[length - i - 1])
    return result


list_a = [2, 3, 4, 5, 6]
list_b = [2, 3, 5, 6]
print(f"[2, 3, 4, 5, 6] => {multiply_pairs(list_a)}")
print(f"[2, 3, 5, 6] => {multiply_pairs(list_b)}")
