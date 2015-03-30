import csv
from model import Car
import model


time = 180
distance = 2000


def experiment():
    cars = [Car(id=i, coords=[0-2.5*i, 0], behaviour={'random': 0})
            for i in xrange(80)]
    t = -1
    gone = {}

    while True:
        for car in cars:
            car.update_state(1, cars, False)

        for car in cars:
            car.fill_state()
            if car.coords[0] >= distance:
                gone[car.id] = 1

                if len(gone) == 1:
                    #print car
                    t = 0
            #print car

        if t >= 0:
            t += 1
        if t == time:
            break

    return len(gone)

for x in range(10, 145, 5):
    model.MAX_ALLOWED_VELOCITY = x/3.6
    l = experiment()
    print x, l
