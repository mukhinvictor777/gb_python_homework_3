"""
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def diff_max_min(incoming_list):
    max_el = incoming_list[0] % 1
    min_el = incoming_list[0] % 1
    for i in range(1, len(incoming_list)):
        if incoming_list[i] % 1 > max_el:
            max_el = round(incoming_list[i] % 1, 4)
        if min_el > incoming_list[i] % 1:
            min_el = incoming_list[i] % 1
    return max_el - min_el


task_list = [1.1, 1.6, 3.2, 5.05, 10.5]
print(f"{task_list} => {diff_max_min(task_list)}")