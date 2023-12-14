import pygame
from random import randint

x = 900
y = 900
width = 400
height = 600 
vel = 150


lives = 1


white = (255, 255, 255)


black = (0, 0, 0)
transparent = (0, 0, 0, 0)

blue = pygame.image.load('static/CarBlockBlue.png')
green = pygame.image.load('static/CarBlockGreen.png')
darkorange = pygame.image.load('static/CarBlockDarkOrange.png')
orange = pygame.image.load('static/CarBlockOrange.png')
red = pygame.image.load('static/CarBlockRed.png')
yellow = pygame.image.load('static/CarBlockYellow.png')

present = pygame.image.load('static/Pressie1.png')

all_sprites_list = pygame.sprite.Group()

class Brick(pygame.sprite.Sprite): 
    
    def __init__(self, colour, width, height, cartype):
        super().__init__()
        self.cartype = cartype
        self.image = self.cartype
        self.image = pygame.transform.scale(self.image, [width, height])
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, present):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        self.color = colour

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-8, 8)]
        
        self.rect = self.image.get_rect()

        self.radius = 5

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
    
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.rect.x,self.rect.y), self.radius)

bg = pygame.image.load('static/RoundBackground.png')
char = pygame.image.load('static/PlayerCar.png')

char_size = (150, 100)
char = pygame.transform.scale(char, char_size)

bg_size = (1920,1080)
bg = pygame.transform.scale(bg,bg_size)

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("placeholder")

class projectile(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)


def redrawGameWindow():
    screen.blit(bg, (0,0))
    screen.blit(char, (x,y))
    all_sprites_list.draw(screen)
    for ball in balls:
        ball.draw(screen)

    pygame.display.update()

ball = Ball(white, 10, 10, present)
ball.rect.x = 350
ball.rect.y = 560

balls = []

running = True 

all_bricks = pygame.sprite.Group()
for i in range(14):
        brick = Brick(transparent, 120, 100, red)
        brick.rect.x = 120 + i* 120
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 120, 100, darkorange)
        brick.rect.x = 120 + i* 120
        brick.rect.y = 120
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 120, 100, orange)
        brick.rect.x = 120 + i* 120
        brick.rect.y = 170
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 120, 100, yellow)
        brick.rect.x = 120 + i* 120
        brick.rect.y = 230
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 120, 100, green)
        brick.rect.x = 120 + i* 120
        brick.rect.y = 285
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 120, 100, blue)
        brick.rect.x = 120 + i* 120
        brick.rect.y = 345
        all_sprites_list.add(brick)
        all_bricks.add(brick)

screen.blit(bg, (0,0))

while running:

    FPS = 60

    pygame.time.delay(100)

    screen.blit(char, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
        
            if event.key == K_ESCAPE:
                running = False 
        
        elif event.type == QUIT:
            running = False
        
        for ball in balls:
            if ball.rect.x < 500 and ball.rect.x > 0:
                ball.rect.x += ball.vel
            #  

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_SPACE] and balls == []:
        balls.append(Ball('red', 5, 5, present=present))
    else:
        print("Balls full")


    if ball.rect.x >= 1570:


    if ball.rect.x >= 1770:

    if ball.rect.x <= 1570:

        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x >= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 0:
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y >= 1080:


    if ball.rect.y > 1080:

    if ball.rect.y >= 1080:

        ball.velocity[1] = -ball.velocity[1]

    if pressed_keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    
    if pressed_keys[pygame.K_RIGHT] and x < 1920 - vel - 200:
        x += vel
        left = False
        right = True 


    print(balls)


    redrawGameWindow()


    redrawGameWindow()

