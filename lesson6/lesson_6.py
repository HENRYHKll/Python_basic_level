# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


traffic = TrafficLight()
traffic.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить
# работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def CalcMass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м. * {wid} м. * {w} кг. * {dep} см. = ", total, "т.")


result = Road(20, 5000, 25, 5)
result.CalcMass()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).
class Worker:

    name = "Вальдемар"
    surname = "Зведачетов"
    position = "Астрофизик"
    profit = 20000
    bonus = 2000
    _income = {"Оклад": profit,
               "Премия": bonus
               }
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_profit(self):
        self.total_profit = self.profit + self.bonus
        return ", доход с учётом премии: {}".format(self.total_profit)


ob1= Worker()
print(ob1.name)
print(ob1.surname)
print(ob1.position)
print(ob1.profit)

ob2 = Position()
print("\n<< Общая информация по сотруднику >>")
print(ob2.get_full_name() + str(ob2.get_full_profit()) + " " + str(ob1._income))

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Vehicle:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return 'Полицейская машина'
        else:
            return 'Гражданская машина'

    def full_info(self):
        return " {} {} Максимальная скорость {} км/ч ".format(self.color, self.name, str(self.speed))

    def go(self):
        return "Машина поехала"

    def stop(self):
        return"Машина остановилась"

    def turn(self):
        return"Машина повернула"


class TownCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_c = TownCar(240, "Black", "Land Rover", False)
print(t_c.police() + t_c.full_info() + t_c.turn())

s_c = SportCar(250, "Red", "Audi", False)
print(s_c.police() + s_c.full_info() + s_c.go())

w_c = WorkCar(250, "Brown", "Mazda", False)
print(w_c.police() + w_c.full_info() + w_c.stop())

p_c = PoliceCar(180, "White", "KIA", True)
print(p_c.police() + p_c.full_info() + p_c.go())

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    title = "\n<< Канцелярская принадлежность >>"

    def draw(self):
        print("Родительский метод класса Stationery")
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("\nРодительский метод класса Pen")
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("\nРодительский метод класса Pencil")
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("\nРодительский метод класса Handle")
        print("Запуск отрисовки маркером")


st = Stationery()
print(st.title)
st.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

han = Handle()
han.draw()