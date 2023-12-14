
import pygame

x = 900
y = 900
width = 400
height = 600 
vel = 150

bg = pygame.image.load('static/RoundBackground.png')
char = pygame.image.load('static/PlayerCar.png')


bg_size = (1920,1080)
bg = pygame.transform.scale(bg,bg_size)


from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player = Player()


def redrawGameWindow():
    screen.blit(bg, (0,0))
    screen.blit(char, (x,y))

    pygame.display.update()
    


running = True 

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

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    
    if pressed_keys[pygame.K_RIGHT] and x < 1920 - vel - width:
        x += vel
        left = False
        right = True 




    redrawGameWindow()


import pygame

x = 50
y = 50
width = 40
height = 60 
vel = 5



bg = pygame.image.load('static/RoundBackground.png')
char = pygame.image.load('static/PlayerCar.png')

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75,25))
#         self.surf.fill((255, 255, 255))
#         self.rect = self.surf.get_rect()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player = Player()

running = True 

while running:
    pygame.time.delay(100)
    screen.blit(char, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
        
            if event.key == K_ESCAPE:
                running = False 
        
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT] and x > vel:
        x -= vel
    
    if pressed_keys[pygame.K_RIGHT] and x < 800 - vel - width:
        x += vel 



    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(char, (x,y))
    pygame.display.update()


