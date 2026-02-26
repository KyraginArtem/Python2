# b = [1, 5, 1, -4, 6, 7]
#
# for i in range(5):
#     a = int(input('Введите число: '))
#     b.append(a)
#
# for number in b:
#     print(number, '** 2 =', number ** 2)

##############################

# books_ID = [10, 20, 30, -1, 2, 1, -1, -1]
# new_books_ID = []
# returned = 0
#
# for _ in range(10):
#     id = int(input('ВВЕДИТЕ ID книги: '))
#     books_ID.append(id)
#
# for id in books_ID:
#     if id == -1:
#         returned += 1
#     else:
#         new_books_ID.append(id)
#
# print('Новый список выданных книг:', new_books_ID)
# print('Вернули за день: ', returned)

#########################

numbers = [3,7,5]

while True:
    number = int(input('Новое число: '))
    numbers.append(number)

    print('Текущий список чисел: ', numbers)

    for i in numbers:
        print( i ** 2, i ** 3, i ** 4)
    print()