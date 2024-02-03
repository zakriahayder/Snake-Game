from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import ScoreBoard

def main():
    # Set up the game window
    screen = Screen()
    screen.title("My Snake Game")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)  # Turn off screen updates


    # Initialise the snake, food, and score objects
    boundary = create_boundary()
    snake = Snake()
    food = Food()
    score = ScoreBoard()

    # Set up keyboard input
    screen.listen()
    movements = {
        "Up": snake.up,
        "Down": snake.down,
        "Left": snake.left,
        "Right": snake.right
    }
    for key, function in movements.items():
        screen.onkey(fun=function, key=key)

    game_is_on = True

    while game_is_on:
        screen.update()  # Update the screen
        time.sleep(0.1)  # Introduce a small delay
        snake.move()  # Move the snake

        # Detect collisions with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Detect collisions with the wall
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_is_on = False
            score.game_over()

        # Detect collisions with other segments
        for segment in snake.segments[1:]:  # Exclude the head
            if snake.head.distance(segment) < 15:
                game_is_on = False
                score.game_over()

    screen.exitonclick()  # Allow the user to close the window

def create_boundary():
    boundary = Turtle()
    boundary.hideturtle()
    boundary.speed("fastest")
    boundary.color("white")
    boundary.penup()
    boundary.goto(-280, -280)
    boundary.pendown()
    for _ in range(4):
        boundary.forward(560)
        boundary.left(90)
    return boundary



if __name__ == '__main__':
    main()