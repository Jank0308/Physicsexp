import pygame,time,random

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
class Cube():
    def __init__(self,color,x,y,mass,xvel,yvel,size):
        self.color = color
        self.x = x
        self.y = y
        self.mass = mass
        self.xvel = xvel
        self.yvel = yvel
        self.size = size
        self.height = size
        self.width = size
    def update(self):
        self.x += self.xvel
        self.y += self.yvel
    def is_collided_with(self, other):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(other)
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    
cube = Cube(WHITE,400,400,10,0.1,0.1,20)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cube.draw(screen)
    cube.update()
        