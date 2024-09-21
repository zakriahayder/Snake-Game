from turtle import Turtle
from random import randint
#just a comment
class Food(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = randint(-270,270)
        new_y = randint(-270,270)
        self.goto(new_x, new_y)
