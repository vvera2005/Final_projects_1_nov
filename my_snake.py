"""Snake game using python"""
import subprocess
import random
def install_library(library_name):
    """This is to install a library"""
    try:
        subprocess.check_call(['pip', 'install', library_name])
        print(f"Successfully installed {library_name}.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {library_name}.")

try:
    import pygame
    from pygame.math import Vector2
except ModuleNotFoundError:
    install_library("pygame")
    import pygame
    from pygame.math import Vector2

try:
    import sys
except ModuleNotFoundError:
    install_library("sys")
    import sys


class Fruit:
    "makes fruits"
    def __init__(self):
            self.x = random.randint(0,n-1) 
            self.y = random.randint(0,n-1) 
            self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        "create rect and draw it"
        fruit_rect = pygame.Rect(self.pos.x * s ,self.pos.y * s,s,s)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)
    def randomize(self):
        self.x = random.randint(0,n-1) 
        self.y = random.randint(0,n-1) 
        self.pos = Vector2(self.x,self.y)

class Snake:
    "makes snake"
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        "draws snake"
        for el in self.body:
            xpos = int(el.x * s)
            ypos = int(el.y * s)
            block_rect = pygame.Rect(xpos,ypos,s,s)
            pygame.draw.rect(screen,(15,112,0),block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:    
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def game_over(self):
        pygame.quit()
        sys.exit()

    def hits_itself(self):
        for i in range(1,len(self.body)):
            if self.body[0] == self.body[i]:
                self.game_over()
    def hits_wall(self):
        if not 0 <= self.body[0].x < n or not 0 <= self.body[0].y < n:
            self.game_over()



class Main:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()

    def update(self):
        self.eat()
        self.snake.move_snake()
        self.snake.hits_itself()
        self.snake.hits_wall()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()


pygame.init()
s = 20
n = 40
screen = pygame.display.set_mode((s*n,s*n))
clock = pygame.time.Clock()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)
main_game = Main()

def main():
    "snake moves"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == screen_update:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and main_game.snake.direction != (0,-1):
                    main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_UP and main_game.snake.direction != (0,1):
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT and main_game.snake.direction != (-1,0):
                    main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_LEFT and main_game.snake.direction != (1,0):
                    main_game.snake.direction = Vector2(-1,0)
        screen.fill((226,232,171))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60) #framerate


main()
