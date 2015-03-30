# -*- coding: utf-8 -*-
import unittest

from model import Car, find_nearest
import model


class MyTestCase(unittest.TestCase):
    def test_change_velocity(self):
        car = Car(velocity=30, acceleration=-0.3)
        car.update_state(60)
        self.assertEqual(car.velocity, 12)

        car = Car(velocity=101, acceleration=-0.5)
        car.update_state(57)
        self.assertEqual(car.velocity, 72.5)

        car = Car(velocity=5, acceleration=2.3)
        car.update_state(23)
        self.assertEqual(car.velocity, 57.9)

        car = Car(velocity=50, acceleration=3)
        car.update_state(12.3)
        self.assertEqual(car.velocity, 86.9)

    def test_change_coords(self):
        """
        Тестируем функцию изменения скорости
        """
        car = Car(velocity=45, acceleration=-0.8)
        car.update_state(60)
        self.assertEqual(car.coords[0], 1260)

        car = Car(velocity=10, acceleration=1.2)
        car.update_state(16)
        self.assertEqual(car.coords[0], 313.6)

        car = Car(velocity=90, acceleration=-3.4)
        car.update_state(12.7)
        self.assertEqual(car.coords[0], 868.807)

        # проверяем двумерный случай
        car = Car(velocity=45, acceleration=-0.8,
                  direction=(0.8, 0.6))
        car.update_state(60)
        self.assertEqual(car.coords, [1008, 756])

    def test_change_acceleration_single(self):
        model.MAX_ALLOWED_VELOCITY = 60/3.6
        car = Car(velocity=5)
        car.update_state()
        self.assertEqual(car.acceleration, 3)
        car.update_state()
        self.assertEqual(car.velocity, 8)
        car.update_state(2)
        self.assertEqual(car.acceleration, 3)
        self.assertEqual(car.velocity, 14)

        car.update_state()
        self.assertEqual(car.acceleration, 2)
        self.assertEqual(car.velocity, 17)

    def test_change_acceleration_double(self):
        car_1 = Car(acceleration=0, velocity=20, coords=[100, 0], id=1)
        car_2 = Car(acceleration=0, velocity=30, coords=[150, 0], id=2)
        cars = [car_1, car_2]
        model.MAX_ALLOWED_VELOCITY = 70
        for car in cars:
            car.update_state(1, cars, False)
        for car in cars:
            car.fill_state()
        self.assertEqual(car_1.acceleration, 2)

        car_1 = Car(acceleration=0, velocity=30, coords=[100, 0], id=1)
        car_2 = Car(acceleration=0, velocity=20, coords=[150, 0], id=2)
        cars = [car_1, car_2]
        model.MAX_ALLOWED_VELOCITY = 24

        for car in cars:
            car.update_state(1, cars, False)

        for car in cars:
            car.fill_state()

        self.assertEqual(car_1.acceleration, -3)

        car_1 = Car(acceleration=0, velocity=10, coords=[100, 0], id=1)
        car_2 = Car(acceleration=0, velocity=15, coords=[140, 0], id=2)
        cars = [car_1, car_2]
        model.MAX_ALLOWED_VELOCITY = 70
        for car in cars:
            car.update_state(1, cars, False)
        for car in cars:
            car.fill_state()
        self.assertEqual(car_1.acceleration, 3)


        car_1 = Car(acceleration=0, velocity=30, coords=[80, 0], id=1)
        car_2 = Car(acceleration=0, velocity=25, coords=[120, 0], id=2)
        cars = [car_1, car_2]
        model.MAX_ALLOWED_VELOCITY = 70
        for car in cars:
            car.update_state(1, cars, False)
        for car in cars:
            car.fill_state()
        self.assertEqual(car_1.acceleration, -10)

    def test_find_nearest(self):
        """
        Тестируем функцию нахождения ближайшей машины
        """
        cars = [
            Car(coords=(2, 0)), Car(coords=(5, 1)),
            Car(coords=(0, 0)), Car(coords=(5, 0)),
            Car(coords=(1, 1)), Car(coords=(7, 1))
        ]

        for i, car in enumerate(cars):
            car.id = i

        self.assertIsNone(find_nearest(cars, cars[3]))
        self.assertEqual(find_nearest(cars, cars[1]).id, 5)
        self.assertIsNone(find_nearest(cars, cars[5]))
        self.assertEqual(find_nearest(cars, cars[0]).id, 3)

if __name__ == '__main__':
    unittest.main()
