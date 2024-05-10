import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_tail(position)

    def add_tail(self, position):
        piece_of_snake = t.Turtle(shape="square")
        piece_of_snake.color("blue")
        piece_of_snake.penup()
        piece_of_snake.goto(position)
        self.snake.append(piece_of_snake)

    def extend(self):
        self.add_tail(self.snake[-1].position())
    # position() will Move the turtle forward by the specified distance, in the direction the turtle is headed.

    def move(self):
        for piece_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece_num - 1].xcor()
            new_y = self.snake[piece_num - 1].ycor()
            self.snake[piece_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for piece_of_snake in self.snake:
            piece_of_snake.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
