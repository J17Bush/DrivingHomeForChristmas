import pygame

x = 900
y = 900
width = 400
height = 600 
vel = 150

black = (0, 0, 0)
transparent = (0, 0, 0, 0)

blue = pygame.image.load('static/CarBlockBlue.png')
green = pygame.image.load('static/CarBlockGreen.png')
darkorange = pygame.image.load('static/CarBlockDarkOrange.png')
orange = pygame.image.load('static/CarBlockOrange.png')
red = pygame.image.load('static/CarBlockRed.png')
yellow = pygame.image.load('static/CarBlockYellow.png')

all_sprites_list = pygame.sprite.Group()

class Brick(pygame.sprite.Sprite): 
    
    def __init__(self, colour, width, height, cartype):
        super().__init__()
        self.cartype = cartype
        self.image = self.cartype
        self.image = pygame.transform.scale(self.image, [width, height])
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

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

balls = []

running = True 

all_bricks = pygame.sprite.Group()
for i in range(14):
        brick = Brick(transparent, 100, 60, red)
        brick.rect.x = 80 + i* 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 100, 60, darkorange)
        brick.rect.x = 80 + i* 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 100, 60, orange)
        brick.rect.x = 80 + i* 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 100, 60, yellow)
        brick.rect.x = 80 + i* 100
        brick.rect.y = 180
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 100, 60, green)
        brick.rect.x = 80 + i* 100
        brick.rect.y = 220
        all_sprites_list.add(brick)
        all_bricks.add(brick)
for i in range(14):
        brick = Brick(transparent, 100, 60, blue)
        brick.rect.x = 80 + i* 100
        brick.rect.y = 260
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
            if ball.x < 500 and ball.x > 0:
                ball.x += ball.vel
            else:
                balls.pop(balls.index(ball))

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_SPACE]:
        if len(balls) < 5:
            balls.append(projectile(round(x + width //2), round(y + height //2), 6, (0,0,0)))

    if pressed_keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    
    if pressed_keys[pygame.K_RIGHT] and x < 1920 - vel - width:
        x += vel
        left = False
        right = True 




    redrawGameWindow()

