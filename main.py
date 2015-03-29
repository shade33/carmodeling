import csv
from model import Car


car = Car(velocity=0, acceleration = 0)

with open('result.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile)
    datawriter.writerow([u'time', u'velocity'])

    for i in xrange(100):
        car.change_coords(1)
        car.change_velocity(1)
        car.change_acceleration()
        datawriter.writerow([i, car.velocity])


cars = []
for i in xrange(10):
    car = Car(coords=[i])
    print car
    cars.append(car)


print cars