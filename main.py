import pygame,math

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
BLUE = (0, 255, 255)

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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        self.x += self.xvel/10
        self.y += self.yvel/10
        #friction #
        if gamecontrol %15 == 0:
            if self.xvel == 0: pass
            elif self.xvel<0:
                self.xvel+=0.5*speed
            
            elif self.xvel>0:
                self.xvel-=0.5*speed
            
            if self.yvel == 0: pass
            elif self.yvel<0:
                self.yvel+=0.5*speed
            elif self.yvel>0:
                self.yvel-=0.5*speed
        if self.x >800 or self.x<0:
            self.x *=-1
        if self.y >800 or   self.y<0:
            self.y *=-1
        
    def kinenergy(self):
        asq = self.xvel**2
        bsq = self.yvel**2
        c = math.sqrt(asq+bsq)
        return (self.mass*0.5)*(c**2)
        
    def is_collided_with(self, other):
        
        if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(other):
            other.xvel = (self.xvel+other.xvel)/2
            other.yvel = (self.yvel+other.yvel)/2
            self.xvel = (self.xvel+other.xvel)/2
            self.yvel = (self.yvel+other.yvel)/2
            return True
        
    
        
        

        

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


player =Cube(BLUE,200,200,10,0,0,20)
othercubes = []
for i in range(3):
    othercubes.append(Cube(WHITE,400,400+(i*15),10,0,0,20))
clock = pygame.time.Clock()
running = True

gamecontrol = 0
font = pygame.font.Font('freesansbold.ttf', 32)
speed = 3

print(othercubes)
while running:
    
    if gamecontrol ==60:
        gamecontrol = 0
    else: gamecontrol+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #controls
    if gamecontrol % 10 == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.xvel -= speed
        if keys[pygame.K_RIGHT]:
            player.xvel += speed
        if keys[pygame.K_UP]:
            player.yvel -= speed
        if keys[pygame.K_DOWN]:
            player.yvel += speed
    
    
        

    player.draw(screen)
    player.update()
    
    for cube in othercubes:
        cube.draw(screen)
        cube.update()
        player.is_collided_with(cube)
        for cubex in othercubes:
            if cubex == cube:
                pass
            else: cube.is_collided_with(cubex)
            player.is_collided_with(cube)
      
    
    print(player.x,player.y)
    # Update the display
    pygame.display.flip()
    screen.fill(BLACK)
    # Cap the frame rate
    clock.tick(60)