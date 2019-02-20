import math
import random
import arcade

WIDTH = 480
HEIGHT = 800
TITLE = 'SNAKE GAME'

BLACK = arcade.color.BLACK
WHITE = arcade.color.WHITE
RED = arcade.color.RED

GRID = 16
COUNT = 0


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 4
        self.color = RED
        self.timer = 0.0

    def reset(self):
        self.x = random.randrange(WIDTH)
        self.y = random.randrange(HEIGHT)
        self.timer = 0.0

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

class Unit:
    def __init__(self):
        self.color = RED

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # snake velocity. moves one grid length every frame in either the x or y direction
        self.dx = GRID
        self.dy = 0
        # keep track of all grids the snake body occupies
        self.cells = []
        # length of the snake. grows when eating an apple
        self.maxCells = 4

    def move(self):
        self.x += = self.dx
        self.y += = self.dy

        # check horizontally edges
        if self.x < 0:
            self.x = WIDTH - GRID
        elif self.x > WIDTH:
            self.x = 0
        # check vertically edges
        if self.y < 0:
            self.y = HEIGHT - GRID
        elif self.y > HEIGHT:
            self.y = 0

    def update(self):
        self.cells.append({x: self.x, y: self.y})
        if len(self.cells) > self.maxCells:
            self.cells.pop()


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.snake = None
        self.food = None

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.food = Food(100, 250)
        self.snake = Snake(300, 200)

    def update(self, delta_time):
        self.food.timer += delta_time
        seconds = int(self.food.timer) % 60
        if seconds >= 2:
            self.food.reset()

def main():
    window = Window(WIDTH, HEIGHT, TITLE)
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
