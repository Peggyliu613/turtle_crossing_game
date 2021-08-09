from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        car.setheading(180)
        car.goto(280, random.randint(-250, 250))
        self.cars.append(car)

    def drive_car(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def go_to_next_level(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []


