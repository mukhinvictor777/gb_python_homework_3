"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def uneven_numbers(incoming_list):
    result = []
    i = 1
    while i < len(incoming_list):
        result.append(incoming_list[i])
        i += 2
    return result


task_list = [2, 3, 5, 9, 3]
print(f"[2, 3, 5, 9, 3] - > на нечетных позициях элементы {uneven_numbers(task_list)},"
      f" ответ: {sum(uneven_numbers(task_list))}")
