import random
#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_res( div_num_a, div_num_b) :
    return div_num_a /div_num_b

def if_zero (numder_zero_result) :
    numder_zero_i = 0
    while numder_zero_result <= 0:
        print(f"Число должно быть больше нуля")
        numder_zero_result = int(input(f"Введите число любое положительное число :"))
        numder_zero_i += 1
        if numder_zero_i == 2:
            numder_zero_result = random.randint(1, 999999)
            print(f'Ладно, пусть будет {numder_zero_result}')

    return numder_zero_result

def str_to_int (str) :
    num_protec = int(str)
    if num_protec <= 0:
        num_protec = if_zero(num_protec)

    return num_protec

num_a = input(f'Введите любое положительное число А :')
num_a = str_to_int(num_a)
num_b = input(f'Введите любое положительное число B :')
num_b = str_to_int(num_b)
print(f'Результат деления {num_a} / {num_b} = ',division_res(num_a, num_b))

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def cookei_for_user (cookei_user_name, cookei_user_lastname, cookei_user_old, cookei_user_city, cookei_user_email,cookei_user_tel):

    return  f'имя - {cookei_user_name}\n' \
            f'фамилия - {cookei_user_lastname}\n' \
            f'год рождения - {cookei_user_old},\n' \
            f'город проживания - {cookei_user_city}\n' \
            f'email - {cookei_user_email}\n' \
            f'телефон - {cookei_user_tel}'

print(cookei_for_user(
    cookei_user_name = 'Chandler', # можно дописать input('Введите имя: ') и так со всеми
    cookei_user_lastname = 'Bing',
    cookei_user_old = '08.04.1968',
    cookei_user_city = 'New York',
    cookei_user_email = 'ChandlerBing@wb.com',
    cookei_user_tel = '+375 29 552266'
))
#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(var_1, var_2, var_3):
    var = [var_1, var_2, var_3]
    max_value = max(var)
    var.remove(max_value)
    return max_value + max(var)
print(my_func(16, 5, 9))

#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_x_y (x: float, y: int):
    x_y = 1
    for _ in range(abs(y)):
        x_y *= x
    return  'первый способ', x ** y,\
            'вторйо способ', 1 /x_y

print(my_func_x_y(3.2, -3))

#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func_2():
    numbers = []
    while True:
        num_input = input('Введите числа через пробел: ')
        new_numbers = num_input.split()
        for number in new_numbers:
            if number == 'q':
                print(sum(numbers))
                return
            numbers.append(int(number))
        print(sum(numbers))


my_func_2()

#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().

def capitalize_func(text):
    def int_func(word: str):
        return f'{word[0].upper()}{word[1:]}'
    words = text.split()
    return ' '.join(list(map(lambda word: int_func(word), words)))


print(capitalize_func('тестовЫЙ тЕКСТ для Проверки работы программы'))