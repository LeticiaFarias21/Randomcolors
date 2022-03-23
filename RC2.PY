import random
import pygame
pygame.init()

#deve ter um melhor modo de organizar as randoms variables
Rred = random.randint(0, 255)
Rgreen = random.randint(0, 255)
Rblue = random.randint(0, 255)

Rtextcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
Rrectcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGH = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption('Random Color')

FPS = 60
FONT = pygame.font.SysFont('comicsans', 60)

TITLE  = FONT.render('Random Colors', True, Rtextcolor, Rrectcolor)
TITLERECT = TITLE.get_rect()
TITLERECT.center = (WIDTH // 2, HEIGH // 4)

#CORES ESTATICAS
RECTANGLER = pygame.Rect( 87, 400, 180, 180)
RECTANGLEG = pygame.Rect( 309, 400, 180, 180)
RECTANGLEB = pygame.Rect( 533, 400, 180, 180)

REFRESHBUTTONIMG = pygame.image.load('refreshbutton.png').convert_alpha()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw_button(self):
        global Rblue, Rred, Rgreen
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print('refresh')
                
        if action == True:
            Rred = random.randint(0, 255)
            Rgreen = random.randint(0, 255)
            Rblue = random.randint(0, 255)
            
        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False
        
        WIN.blit(self.image, (self.rect.x, self.rect.y))

        return action, Rred, Rgreen, Rblue

REFRESHBUTTON = Button(340, 300, REFRESHBUTTONIMG)

#NUMEROS E RECTS DAS CORES
#MOVEL
def color_value_red():    
    COLORVALUERED = FONT.render(str(Rred), True, BLACK, WHITE)
    global COLORVALUEREDRECT
    COLORVALUEREDRECT = COLORVALUERED.get_rect()
    COLORVALUEREDRECT.center = (177, 630) 

    return COLORVALUERED

def color_value_green():    
    COLORVALUEGREEN = FONT.render(str(Rgreen), True, BLACK, WHITE)
    global COLORVALUEGREENRECT
    COLORVALUEGREENRECT = COLORVALUEGREEN.get_rect()
    COLORVALUEGREENRECT.center = (399, 630) 

    return COLORVALUEGREEN
    
def color_value_blue():    
    COLORVALUEBLUE = FONT.render(str(Rblue), True, BLACK, WHITE)
    global COLORVALUEBLUERECT
    COLORVALUEBLUERECT = COLORVALUEBLUE.get_rect()
    COLORVALUEBLUERECT.center = (623, 630) 

    return COLORVALUEBLUE

def draw_window():
    WIN.fill((Rred, Rgreen, Rblue))
    REFRESHBUTTON.draw_button()
    WIN.blit(TITLE, (TITLERECT))
    WIN.blit(color_value_red(), COLORVALUEREDRECT)
    WIN.blit(color_value_green(), COLORVALUEGREENRECT)
    WIN.blit(color_value_blue(), COLORVALUEBLUERECT)
    pygame.draw.rect(WIN, RED, RECTANGLER)
    pygame.draw.rect(WIN, GREEN, RECTANGLEG)
    pygame.draw.rect(WIN, BLUE, RECTANGLEB)
    
    
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
        
        # for para updated da cor e dos objetos na tela

        

    pygame.quit()

main()