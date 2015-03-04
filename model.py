# -*- coding: utf-8 -*-

# вычисление комфортной дистанции: расстояние, которое при текущей скорости
# проезжает машина за 2 секунды
comfort_distance = lambda x: 2*x

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
        if coords:
            self.coords = list(coords)
        if direction:
            self.direction = list(direction)
        self.velocity = velocity
        self.acceleration = acceleration
        self.behaviour = tuple(behaviour)

    def change_acceleration(self):
        pass

    def change_coords(self, dt):
        delta_c = self.velocity * dt + self.acceleration * (dt ** 2) / 2
        n = len(self.coords)
        for i in range(n):
            self.coords[i] += delta_c*self.direction[i]

    def change_velocity(self, delta_t):
        self.velocity += self.acceleration * delta_t
        if self.velocity < 0:
            self.velocity = 0
