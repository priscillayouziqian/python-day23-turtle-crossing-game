COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager():  # don't put Turtle in the ()
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # the chance to get the number 1 is fairly 1/6, this way we don't create new cars too often
            new_car = Turtle("square")  # put the Turtle class here, because we need lots of car instance created
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            # new_car.goto(random.randint(-250, 300), random.randint(-250, 250))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            # backward is going forward to the left side
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
