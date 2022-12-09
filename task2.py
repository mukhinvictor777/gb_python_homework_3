"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name, surname, year, city, email, phone):
    print(f"имя: {name}, фамилия: {surname}, год рождения: {year}, "
          f"город проживания: {city}, email: {email}, телефон: {phone}")


user_name = input("Напишите Ваше имя: ")
user_surname = input("фамилию: ")
user_year = input("год рождения: ")
user_city = input("город проживания: ")
user_email = input("email: ")
user_phone = input("и номер телефона: ")
print("Ваши данные:")
user_data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone)
