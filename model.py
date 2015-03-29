# -*- coding: utf-8 -*-
"""
Модель машины с функциями ее поведения.
"""

# вычисление комфортной дистанции: расстояние, которое при текущей скорости
# проезжает машина за 2 секунды
comfort_distance = lambda x: 2*x

MAX_ALLOWED_VELOCITY = 100 / 3.6
CARS = []


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
    behaviour = ()

    def __init__(self, id=0, coords=(0, 0), direction=(1, 0), velocity=0,
                 acceleration=0, behaviour=()):
        self.id = id
        self.coords = list(coords)
        self.direction = list(direction)
        self.velocity = velocity
        self.acceleration = acceleration
        self.behaviour = tuple(behaviour)

    def change_acceleration(self):
        """
        another_car = find_nearest(cars, cars)
        if(another_car.x - self.x >= comfort_distance):
        # рассматриваем случай, при котором расстояние между машинами больше, чем комфортное для нас
            if(self.v < 14):
            # 14 м\с примерно равно 50 км\ч
            # разделяем на 2 случая, так как
            # от о до 50 км\ч при нажатии на педаль газа машина ускоряется быстро
            # а от 50 до 100 км\ч медленнее
                self.a += 3
            # присваиваем ускорение 3 м\с = 11 км\ч*с
            else:
                self.a += 2
                # присваиваем ускорение 2 м\с = 7 км\ч*с
        else:
        # рассматриваем случай, когда расстояние между машинами меньше комфортного
            self.a = (another_car.x - self.x)/2 - self.v
            # присваиваем ускорение, которое придаст нашей машине скорость
            # при которой она будет ровно в 2-х секундах от впереди едущей машины
        pass
        """
        if self.velocity < MAX_ALLOWED_VELOCITY:
            if self.velocity < 14:
                self.acceleration = 3
            else:
                self.acceleration = 2
        else:
            self.acceleration = -(self.velocity - MAX_ALLOWED_VELOCITY) / 2
        # рандомное изменение в предалах от -1 до 1

    def change_coords(self, dt):
        """
        Изменение координат машины за время dt секунд при текущих ускорении
        и скорости. Вычисляется по формулe S = V*T+A*T^2/2
        """
        delta_c = self.velocity * dt + self.acceleration * (dt ** 2) / 2
        n = len(self.coords)
        for i in range(n):
            self.coords[i] += delta_c*self.direction[i]

    def change_velocity(self, delta_t):
        """
        Изменение скорости машины за время dt секунд.
        Вычисляется по формуле V = V_0 + A*T
        """
        self.velocity += self.acceleration * delta_t
        if self.velocity < 0:
            self.velocity = 0

    def __str__(self):
        return "Car: coords {0}".format(self.coords)


def find_nearest(car):
    """
    Для машин движущихся по многополосной дороге ищем ближайшую машину по
    направлению движения.

    Сначала сортируем по первой координате, а потом ищем следующую машину,
    у которой совпадает вторая координата.

    :param cars: массив машин
    :param car: машина, для которой ищем ближайшую
    :return: ближайшую машину или None, если такой есть
    """
    if not CARS:
        return None
    CARS.sort(key=lambda x: x.coords[0])
    for i, c in enumerate(CARS):
        if c.id == car.id:
            break

    nearest = None
    for j in xrange(i+1, len(CARS)):
        if CARS[j].coords[1] == car.coords[1]:
            nearest = CARS[j]
    return nearest
