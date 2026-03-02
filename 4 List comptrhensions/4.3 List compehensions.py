#Задача 1. Кубы и квадраты
#Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка: в первом лежат кубы чисел
# в диапазоне от А до В, во втором — квадраты чисел в этом же диапазоне. Выведите списки на экран.
# Для генерации используйте list comprehensions (как и в следующих задачах).

first_number = int(input('Введите число: '))
second_number = int(input('Введите число: '))

cube_number = [x ** 3 for x in range(first_number, second_number + 1)]
squad_number = [x ** 2 for x in range(first_number, second_number + 1)]

print(f'Квадраты чисел раны: {cube_number}')
print(f'Кубы чисел раны: {squad_number}')