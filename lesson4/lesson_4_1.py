#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_mame, output_in_hours, insert_per_hour, cash_bonus = argv

def salary_func (f_output_in_hours: float, f_insert_per_hour: float, f_cash_bonus: float):
    try:
        result_salary = float(f_output_in_hours) * float(f_insert_per_hour) + float(f_cash_bonus)
    except ValueError or TypeError as om:
        result_salary = 0
        print(f'Данне не верны, провете их - {om}')
    return result_salary

print(f'Скрипт - {script_mame}\n'
      f'Заработная плата составила: {salary_func(output_in_hours, insert_per_hour, cash_bonus)}\n'
      f'Выработка в часах: {output_in_hours}\n'
      f'Ставка в час: {insert_per_hour}\n'
      f'Премия : {cash_bonus}')