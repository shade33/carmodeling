# -*- coding: utf-8 -*-
import unittest

from model import Car


class MyTestCase(unittest.TestCase):
    def test_change_velocity(self):
        car = Car(velocity=30, acceleration=-0.3)
        car.change_velocity(60)
        self.assertEqual(car.velocity, 12)

        car = Car(velocity=101, acceleration=-0.5)
        car.change_velocity(57)
        self.assertEqual(car.velocity, 72.5)

        car = Car(velocity=5, acceleration=2.3)
        car.change_velocity(23)
        self.assertEqual(car.velocity, 57.9)

        car = Car(velocity=50, acceleration=3)
        car.change_velocity(12.3)
        self.assertEqual(car.velocity, 86.9)

    def test_change_coords(self):
        """
        Тестируем функцию изменения скорости
        """
        car = Car(velocity=45, acceleration=-0.8)
        car.change_coords(60)
        self.assertEqual(car.coords[0], 1260)

        car = Car(velocity=10, acceleration=1.2)
        car.change_coords(16)
        self.assertEqual(car.coords[0], 313.6)

        car = Car(velocity=90, acceleration=-3.4)
        car.change_coords(12.7)
        self.assertEqual(car.coords[0], 868.807)

        # проверяем двумерный случай
        car = Car(velocity=45, acceleration=-0.8,
                  direction=(0.8, 0.6))
        car.change_coords(60)
        self.assertEqual(car.coords, [1008, 756])

    def test_find_nearest(self):
        """
        Тестируем функцию нахождения ближайшей машины
        """
        #TODO
        pass

if __name__ == '__main__':
    unittest.main()
