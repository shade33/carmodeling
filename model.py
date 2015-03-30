# -*- coding: utf-8 -*-
"""
Модель машины с функциями ее поведения.
"""
import random
from math import sqrt


# вычисление комфортной дистанции: расстояние, которое при текущей скорости
# проезжает машина за 2 секунды
comfort_distance = lambda x: 2*x

MAX_ALLOWED_VELOCITY = 100 / 3.6
CONST_DISTANCE = 2  # Расстояние, которое должно постоянно сохраняться
                    # между автобилями


class Car:
    # идентификатор машины
    id = 0
    # координаты
    coords = None
    # направление, вектор единичной длины
    direction = None
    # скорость, м/c
    velocity = 0
    # ускорение, м/c^2
    acceleration = 0
    # поведенческие параметры, случайные значения определяющие вероятность
    # того или иного действия
    behaviour = None
    # промежуточное состояние
    future_state = None

    def __init__(self, id=0, coords=(0, 0), direction=(1, 0), velocity=0,
                 acceleration=0, behaviour={}):
        self.id = id
        self.coords = list(coords)
        self.direction = list(direction)
        self.velocity = velocity
        self.acceleration = acceleration
        self.behaviour = dict(behaviour)
        self.future_state = dict()

    def _change_acceleration(self, cars):
        """
        """
        another_car = find_nearest(cars, self)
        dist = distance(self, another_car) if another_car else 0
        if not another_car or dist >= comfort_distance(self.velocity):
            # Расстояние до ближайшей по ходу движения машины
            # больше, чем комфортное. Тогда руководствуемся только
            # ограничением максимальной скорости
            if self.velocity < MAX_ALLOWED_VELOCITY:
                # если текущая скорость меньше допустимой, то разгоняемся -
                # задаем положительное ускорение. Причем, до 50 км/ч
                # (прим. 14 м/с) можем разгоняться быстрей.
                if self.velocity < 14:
                    self.future_state['acceleration'] = 3
                else:
                    self.future_state['acceleration'] = 2
            else:
                # иначе замедлемся так, чтобы за 2 секунды наша скорость
                # стала разрешенной
                self.future_state['acceleration'] = -(
                    self.velocity - MAX_ALLOWED_VELOCITY) / 2
        else:
            # Рассматриваем случай, когда расстояние между машинами меньше
            # комфортного. Тогда мы меняем ускорение так, чтобы через
            # 1 секунду текущее расстояние стало комфортным
            self.future_state['acceleration'] = (
                dist + CONST_DISTANCE)/2. - self.velocity

        # рандомное изменение в предалах от -2 до 2
        if self.behaviour.get('random') > 0:
            r = self.behaviour['random']
            self.future_state['acceleration'] += random.uniform(-r, r)

    def _change_coords(self, dt):
        """
        Изменение координат машины за время dt секунд при текущих ускорении
        и скорости. Вычисляется по формулe S = V*T+A*T^2/2
        """
        delta_c = self.velocity * dt + self.acceleration * (dt ** 2) / 2
        n = len(self.coords)
        self.future_state['coords'] = [0]*n
        for i in range(n):
            self.future_state['coords'][i] = (
                self.coords[i] + delta_c*self.direction[i]
            )

    def _change_velocity(self, dt):
        """
        Изменение скорости машины за время dt секунд.
        Вычисляется по формуле V = V_0 + A*T
        """
        self.future_state['velocity'] = (
            self.velocity + self.acceleration * dt
        )
        if self.future_state['velocity'] < 0:
            self.future_state['velocity'] = 0

    def update_state(self, dt=1, cars=[], full=True):
        self._change_acceleration(cars)
        self._change_coords(dt)
        self._change_velocity(dt)
        if full:
            self.fill_state()

    def fill_state(self):
        self.velocity = self.future_state['velocity']
        self.acceleration = self.future_state['acceleration']
        self.coords = list(self.future_state['coords'])

    def __str__(self):
        return "Car ({0}): coords {1}, v={2}, mav={3}".format(self.id, self.coords,
                                                       self.velocity,
                                                       MAX_ALLOWED_VELOCITY)


def distance(car_1, car_2):
    dim = len(car_1.coords)
    res = 0
    for i in xrange(dim):
        res += (car_1.coords[i] - car_2.coords[i])**2
    return sqrt(res)


def find_nearest_2(cars, car):
    if not cars:
        return None

    if car.id == 0:
        return None

    return cars[car.id-1]

def find_nearest(cars, car):
    """
    Для машин движущихся по многополосной дороге ищем ближайшую машину по
    направлению движения.

    Сначала сортируем по первой координате, а потом ищем следующую машину,
    у которой совпадает вторая координата.

    :param cars: массив машин, среди которых ищем
    :param car: машина, для которой ищем ближайшую
    :return: ближайшую машину или None, если такой есть
    """
    if not cars:
        return None
    in_cars = sorted(cars, key=lambda x: x.coords[0])

    i = 0
    for c in in_cars:
        if c.id == car.id:
            break
        i += 1

    nearest = None
    for j in xrange(i+1, len(in_cars)):
        if in_cars[j].coords[1] == car.coords[1]:
            nearest = in_cars[j]
            break

    return nearest
