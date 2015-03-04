
import unittest

from model import Car


class MyTestCase(unittest.TestCase):
    def test_change_velocity(self):
        car = Car(velocity=30, acceleration=-0.3)
        car.change_velocity(60)
        self.assertEqual(car.velocity, 12)

if __name__ == '__main__':
    unittest.main()
