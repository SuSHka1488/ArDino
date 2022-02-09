import random
import pygame

pygame.init()

### Перменные для иницилизации ###
FPS = 60
WIDTH = 320
HEIGHT = 128
Window = pygame.display.set_mode((WIDTH, HEIGHT))

### Изображения ###
image_Dino = pygame.image.load("images/Dino_image.png") #Изображение динозавра
image_Cactus1 = pygame.image.load("images/Cactus1_image.png") #Изображение первого кактуса
image_Cactus2 = pygame.image.load("images/Cactus2_image.png") #Изображение второго кактуса
image_Cactus3 = pygame.image.load("images/Cactus3_image.png") #Изображение третьего кактуса
image_Road = pygame.image.load("images/Road_image.png") #Изображение дороги

### Перменные ###
PressSPACE = False
lose_var = False

### Классы ###
## Класс динозавра ##
class Dino_CLASS(pygame.sprite.Sprite):
    def __init__(self, X_Dino, Y_Dino, image):
        self.X_Dino = X_Dino
        self.Y_Dino = Y_Dino
        self.image = image
        self.IsJump = False
        
    def update(self):
        global PressSPACE
        if PressSPACE == True and self.Y_Dino >= 4 and self.Y_Dino == 66 or self.IsJump == True:
            self.Y_Dino-=4
            if (self.Y_Dino >= 4):
                self.IsJump=True
            else:
                self.IsJump=False
        if self.IsJump == False and self.Y_Dino < 66:
            self.Y_Dino+=2
    
    def draw(self):
        Window.blit(self.image, (self.X_Dino, self.Y_Dino))
        
    def CheckY(self):
        return self.Y_Dino

## Класс кактусов ##
class Cactus_CLASS(pygame.sprite.Sprite):
    def __init__(self, X_Cactus, Y_Cactus, image, WidthCactus):
        self.X_Cactus = X_Cactus
        self.Y_Cactus = Y_Cactus
        self.image = image
        self.Y_Dino = 0
        self.ChoseImage = 0
        self.WidthCactus = WidthCactus
        
    def update(self, Y_Dino):
        global lose_var
        self.Y_Dino = Y_Dino
        if self.X_Cactus > 0:
            self.X_Cactus-=3
        else:
            self.ChoseImage = random.randint(0,2)
            if self.ChoseImage == 0:
                self.image = image_Cactus1
                self.WidthCactus = 16
            elif self.ChoseImage == 1:
                self.image = image_Cactus2
                self.WidthCactus = 32
            elif self.ChoseImage == 2:
                self.image = image_Cactus3
                self.WidthCactus = 32
            self.X_Cactus = 320
        if self.X_Cactus <= 46 and self.X_Cactus >= 46-self.WidthCactus and self.Y_Dino+24 >= self.Y_Cactus or self.X_Cactus <= 32 and self.X_Cactus >= 46-self.WidthCactus and self.Y_Dino+24 <= self.Y_Cactus and self.Y_Dino+48 >= self.Y_Cactus:
            lose_var = True
    
    def draw(self):
        Window.blit(self.image, (self.X_Cactus, self.Y_Cactus))

Dino = Dino_CLASS(46, 66, image_Dino)
Cactus1 = Cactus_CLASS(320, 74, image_Cactus1, 16)
Cactus2 = Cactus_CLASS(480, 74, image_Cactus3, 32)

def Game():
    global PressSPACE, lose_var
    #Куча нужных параметров
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  

        PressKeyboardButton = pygame.key.get_pressed()
        if PressKeyboardButton[pygame.K_SPACE]:
            PressSPACE = True
        else:
            PressSPACE = False
    
        Dino.update()
        Cactus1.update(Dino.CheckY())
        Cactus2.update(Dino.CheckY())
       
        print(lose_var)
       
        Window.fill((0,0,0))
        Dino.draw()
        Cactus1.draw()
        Cactus2.draw()
        Window.blit(image_Road, (1, 108))
        pygame.display.update()
Game()