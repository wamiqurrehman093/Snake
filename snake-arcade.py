import math
import random
import arcade

WIDTH = 480
HEIGHT = 800
TITLE = 'SNAKE GAME'

BLACK = arcade.color.BLACK
WHITE = arcade.color.WHITE
RED = arcade.color.RED

class Food:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.radius = 8
        self.color = RED
        self.timer = 0.0

    def reset(self):
        self.x = random.randrange(WIDTH)
        self.y = random.randrange(HEIGHT)
        self.timer = 0.0

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.snake = None
        self.food = None

    def on_draw(self):
        arcade.start_render()
        self.food.draw()

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.food = Food((100, 250))

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
