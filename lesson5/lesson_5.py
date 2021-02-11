import json

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
file_name = 'src/task_1.txt'
with open(file_name, 'w', encoding='utf-8') as f:
    while True:
        string = input('Введите строку или нажмите ENTER для окончания ввода: ')
        if string == '':
            break
        f.write(f'{string}\n')

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
file_name2 = 'src/task_2.txt'
with open(file_name2, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'Кол-во строк в файле: {len(lines)}')
    for i, line in enumerate(lines):
        print(f'Кол-во слов в {i} строке: {len(line.split())}')


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

file_name3 = 'src/task_3.txt'
with open(file_name3, 'r', encoding='utf-8') as f:
    lines = f.readlines()

    second_names_with_low_salary = []
    average_salary = 0
    for line in lines:
        second_name, salary = line.split()
        salary = float(salary)
        average_salary += salary
        if salary < 20000:
            second_names_with_low_salary.append(second_name)

    print(f'Сотрудники с окладом меньше 20000: {second_names_with_low_salary}')
    print(f'Средний оклад: {round(average_salary / len(lines), 2)}')
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
file_name4_r = 'src/task_4r.txt'
file_name4_w = 'src/task_4w.txt'

translate_d = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open(file_name4_r, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    new_lines = [f'{translate_d[line.split(" - ")[0]]} - {line.split(" - ")[-1]}' for line in lines]

with open(file_name4_w, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
file_name5 = 'src/task_5.txt'

with open(file_name5, 'w', encoding='utf-8') as f:
    digits = input('Введите набор чисел через пробел: ')
    f.write(digits)


with open(file_name5, 'r', encoding='utf-8') as f:
    digits_str = f.read()
    print(sum([int(digit) for digit in digits_str.split()]))



# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
file_name6 = 'src/task_6.txt'


def get_count_lessons_by_subject(lesson):
    if lesson != '-':
        return int(lesson.split('(')[0])
    return 0


def get_sum_lessons(lessons):
    return sum([get_count_lessons_by_subject(lesson) for lesson in lessons])


with open(file_name6, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    res = {}
    for line in lines:
        subject, *lessons = line.strip().split()
        res[subject.split(':')[0]] = get_sum_lessons(lessons)
    print(res)



# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.


file_name7r = 'src/task_7.txt'
file_name6w = 'src/task_7.json'

with open(file_name7r, 'r', encoding='utf-8') as f:
    sum_profit = 0
    res = {}
    lines = f.readlines()
    for line in lines:
        name, form, income, outcome = line.split()
        profit = float(income) - float(outcome)
        res[name] = profit
        if profit > 0:
            sum_profit += profit

res['average_profit'] = round(sum_profit / len(lines), 2)

with open(file_name6w, 'w', encoding='utf-8') as f:
    json.dump(res, f)
