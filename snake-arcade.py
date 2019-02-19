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
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.width = 17
        self.height = 17
        self.color = WHITE

    def move(self, dirnx, dirny):
        self.x += dirnx
        self.y += dirny

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                    self.color)
class Snake:
    def __init__(self, position):
        self.body = []
        head = Unit(position)
        self.body.append(head)
        self.dirnx = 0
        self.dirny = 1
        self.key = None
        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0],c.rows-1)
                else:
                    c.move(c.dirnx,c.dirny)

    def draw(self):
        for unit in self.body:
            unit.draw()

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
        self.food = Food((100, 250))
        self.snake = Snake((300, 200))
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
