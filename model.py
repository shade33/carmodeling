# -*- coding: utf-8 -*-

# вычисление комфортной дистанции: расстояние, которое при текущей скорости
# проезжает машина за 2 секунды
comfort_distance = lambda x: 2*x


MAX_ALLOWED_VELOCITY = 60 / 3.6

class Car:
    # координаты
    coords = []
    # направление, вектор единичной длины
    direction = []
    # скорость, м/c
    velocity = 0
    # ускорение, м/c^2
    acceleration = 0
    # поведенческие параметры, случайные значения определяющие вероятность
    # того или иного действия
    behaviour = ()

    def __init__(self, coords=None,
                 direction=None, velocity=0,
                 acceleration=0, behaviour=()):
        self.coords = list(coords) if coords else [0]
        self.direction = list(direction) if direction else [1]
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
                self.acceleration += 3
            else:
                self.acceleration += 2
        else:
            self.acceleration = (self.velocity - MAX_ALLOWED_VELOCITY) / 2
        # рандомное изменение в предалах от -1 до 1

    def change_coords(self, dt):
        delta_c = self.velocity * dt + self.acceleration * (dt ** 2) / 2
        n = len(self.coords)
        for i in range(n):
            self.coords[i] += delta_c*self.direction[i]

    def change_velocity(self, delta_t):
        self.velocity += self.acceleration * delta_t
        if self.velocity < 0:
            self.velocity = 0

def find_nearest(cars, car):
    """
    Ищем ближайшую машину по направлению движения

    :param cars:
    :param car:
    :return:
    """
    if not cars:
        return None

    # сортируем список машин по координате
    # ищем положение нашей машины в массиве
    # берем следующую машину
    # если ее нет, то возвращаем None

    return None


