""" Creating a room that I can move around in. Also needs files CONFIG"""
try:
    import sys
    # import random
    # import os
    # import getopt
    import pygame
    # import time
    # import CONFIG
    import itertools
    # import numpy as np
    # from socket import *
    # from pygame.locals import *
except ImportError:
    print("couldn't load a module.")
    sys.exit(2)
    
pygame.init()
#print(pygame.font.get_fonts())
pygame.mixer.music.load("../data/jazz.mp3")
# display_width = 640 
# display_height = 480   
display_width = 800 
display_height = 640   
White = (255,255,255)
Black = (0,0,0)
Red = (200, 0, 0)
Bright_red = (255, 0, 0)
Bright_green = (0, 255, 0)
Green = (0,200, 0)
Yellow = (204, 204, 0)
Brown = (139,69,19)

car_width = 75

SCALE = 32
gameDisplay=pygame.display.set_mode((display_width, display_height))  
pygame.display.set_caption('Explore the house to discover some science')
map = []
camera=[0,0]
map_tile_image = {
    "G" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_97.png"), ((SCALE, SCALE))),
    "L" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_376.png"), ((SCALE, SCALE))),
    "R" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_378.png"), ((SCALE, SCALE))),
    "T" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_350.png"), ((SCALE, SCALE))),
    "B" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_404.png"), ((SCALE, SCALE))),
    "C" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_349.png"), ((SCALE, SCALE))),
    "D" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_351.png"), ((SCALE, SCALE))),
    "E" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_403.png"), ((SCALE, SCALE))),
    "F" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_405.png"), ((SCALE, SCALE))),
    "a" : pygame.transform.scale(pygame.image.load("../data/flooring/wall.png"), ((SCALE, SCALE))),
    
    #bathroom floor
    "X" : pygame.transform.scale(pygame.image.load("../data/flooring/bathroom_floor.png"), ((SCALE, SCALE))),
    #bedroom floor
    "K" : pygame.transform.scale(pygame.image.load("../data/flooring/bedroom_floor.png"), ((SCALE, SCALE))),
    #lounge floor
    "Z" : pygame.transform.scale(pygame.image.load("../data/flooring/lounge_floor.png"), ((SCALE, SCALE))),
    #white
    "W" : pygame.transform.scale(pygame.image.load("../data/flooring/white.png"), ((SCALE, SCALE))),
    "H" : pygame.transform.scale(pygame.image.load("../data/flooring/black.png"), ((SCALE, SCALE))),
    "Y" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_98.png"), ((SCALE, SCALE))),
    "V" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_99.png"), ((SCALE, SCALE))), 
    #grass
    "P" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_01.png"), ((SCALE, SCALE))), 
    "S" : pygame.transform.scale(pygame.image.load("../data/flooring/sky.png"), ((SCALE, SCALE))),
    #pool greens
    "I" : pygame.transform.scale(pygame.image.load("../data/flooring/pool_green1.png"), ((SCALE, SCALE))), 
    "J" : pygame.transform.scale(pygame.image.load("../data/flooring/pool_green2.png"), ((SCALE, SCALE))),
    #mirror surface 
    "U" : pygame.transform.scale(pygame.image.load("../data/flooring/mirror_surface.png"), ((SCALE, SCALE))),
    #BATH
    "t" : pygame.transform.scale(pygame.image.load("../data/flooring/water.png"), ((SCALE, SCALE)))

}


#resources------ Here we place static game components, imagery etc.

def text_objects(text, font):
    textSurface=font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,inactive, active, a, b, action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 0:
                main(a,b)
            elif action == 1:
                pygame.quit()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, w, h))
            
    smallText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2), y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    
def return_button(msg,x,y,w,h,inactive, active, a, b, action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 0:
                main(a,b)
            elif action == 1:
                pygame.quit()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, w, h))
            
    smallText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2), y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    
def game_intro():
    """ Essential for a good start"""
    # pygame.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        image = pygame.image.load("../data/images/backgrounds/tile_73.png")
        tile_width, tile_height = image.get_width(), image.get_height()
        for x,y in itertools.product(range(0,display_width,tile_width),
                                 range(0,display_height,tile_height)):
            gameDisplay.blit(image, (x, y))
        # background = pygame.transform.scale(image, (display_width, display_height))
        # background = background.convert()
        # gameDisplay.blit(background, (0, 0))
        #gameDisplay.fill("../data/topdown-shooter/PNG/Tiles/tile73.png")
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        largeText2=pygame.font.SysFont ("bitstreamverasans", 30)
        text2=largeText2.render("Lockdown Edition", True, Yellow)
        text2 = pygame.transform.rotate(text2, -30)
        
        text3=largeText2.render("A programme developed using GitHub", True, White)
        text4=largeText2.render("compiled on ARCHER2 using BASH", True, White)

        
        TextSurf, TextRect = text_objects("The Advanced ", largeText)
        TextSurf2, TextRect2 = text_objects("Scripting Workshop", largeText)
        TextRect.center = (display_width/2, display_height/3)
        TextRect2.center = (display_width/2, display_height/3+40)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(text2, (display_width*0.65, display_height/6))
        gameDisplay.blit(text3, (display_width*0.1, display_height/1.2))
        gameDisplay.blit(text4, (display_width*0.1, display_height/1.1))
        
        button("Enter!", display_width/2-150, 300, 200, 100, Brown, Bright_green, 764, 360, 0)
        button("Quit!", display_width/2, 400, 200, 100, Brown, Bright_red, 100, 100, 1)
        
        pygame.display.update()
        clock.tick(15)
        
def computer(initial_x, initial_y):
    """ interaction with a computer """
    load_map("computer")
    background = pygame.image.load("../data/images/screens/computer/terminal.png")
    background=background.convert()
    background=pygame.transform.scale(background, (display_width, display_height))
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(background, (0, 0))
        #button(message, x, y, w, h, inactive, active, returnposx, returnposy)
        return_button("Return to game", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(15)

def window(initial_x, initial_y):
    """ interaction with a computer """
    load_map("window")
    #clouds
    cloud1 = pygame.image.load("../data/images/screens/window/cloud4.png").convert_alpha()
    cloud2 = pygame.image.load("../data/images/screens/window/cloud5.png").convert_alpha()
    cloud3 = pygame.image.load("../data/images/screens/window/cloud7.png").convert_alpha()
    #trees
    tree1 = pygame.image.load("../data/images/screens/window/tree1.png").convert_alpha()
    tree2 = pygame.image.load("../data/images/screens/window/tree2.png").convert_alpha()
    #castle
    castle = pygame.image.load("../data/images/screens/window/castle.png").convert_alpha()
    
    cloud1=pygame.transform.scale(cloud1, (int(228/2.5), int(124/2.5)))
    cloud2=pygame.transform.scale(cloud2, (int(238/1.5), int(135/1.5)))
    cloud3=pygame.transform.scale(cloud3, (int(234/3), int(118/3)))
    cloud4=pygame.transform.scale(cloud3, (int(238/1.5), int(135/1.5)))
    cloud5=pygame.transform.scale(cloud2, (int(234/3), int(118/3)))
    tree1=pygame.transform.scale(tree1, (int(129/4), int(230/4)))
    tree2=pygame.transform.scale(tree2, (int(106/4), int(241/4)))
    castle=pygame.transform.scale(castle, (int(204/4), int(182/4)))
    
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        #blit images
        gameDisplay.blit(cloud1, (100, 50))
        gameDisplay.blit(cloud2, (160, 70))
        gameDisplay.blit(cloud3, (280, 30))
        gameDisplay.blit(cloud4, (450, 50))
        gameDisplay.blit(cloud5, (650, 70))
        
        gameDisplay.blit(tree1, (3*32, 16.8*32))
        gameDisplay.blit(tree1, (7.9*32, 15.5*32))
        gameDisplay.blit(tree1, (19*32, 17*32))
        gameDisplay.blit(tree1, (14*32, 16*32))
        
        gameDisplay.blit(tree2, (20*32, 16*32))
        gameDisplay.blit(tree2, (13*32, 14*32))
        gameDisplay.blit(tree2, (15*32, 14.5*32))
        gameDisplay.blit(tree2, (6*32, 16.5*32))
        gameDisplay.blit(castle, (22.4*32, 14.6*32))
        
        # gameDisplay.blit(TextSurf, TextRect)
        
        # gameDisplay.blit(background, (0, 0))
        #button(message, x, y, w, h, inactive, active, returnposx, returnposy)
        return_button("Return to game", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(15)

def book(initial_x, initial_y):
    """ interaction with a computer """
    load_map("book")
    background = pygame.image.load("../data/images/screens/book/newspaper.png").convert_alpha()
    background=pygame.transform.scale(background, (int(display_width/1.1),int(display_height/1.1)))
    background=pygame.transform.rotate(background, 4)
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (display_width/30, display_height/30))
        gameDisplay.blit(TextSurf, TextRect)
        #button(message, x, y, w, h, inactive, active, returnposx, returnposy)
        return_button("Return to game", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(15)
        
def pool(initial_x, initial_y):
    """ interaction with a computer """
    load_map("pool")
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        11, 14.9, 0, 40, 35
        balls = pygame.image.load("../data/images/kitchen/balls.png").convert_alpha()
        balls=pygame.transform.scale(balls, (int(40*10), int(35*10)))
        
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(balls, (600, -100))
        
        gameDisplay.blit(TextSurf, TextRect)
        #button(message, x, y, w, h, inactive, active, returnposx, returnposy)
        return_button("Return to game", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(15)
    
def bath(initial_x, initial_y):
    """ interaction with a computer """
    load_map("bath")
    ducky = pygame.image.load("../data/images/screens/bath/duck.png").convert_alpha()
    ducky = pygame.transform.scale(ducky, (int(40*6), int(38*6)))
    bubble = pygame.image.load("../data/images/screens/bath/bubble.png").convert_alpha()
    bubble1 = pygame.transform.scale(bubble, (int(70), int(70)))
    bubble2 = pygame.transform.scale(bubble, (int(40), int(40)))
    
    
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        
        gameDisplay.blit(ducky, (650, 20))
        gameDisplay.blit(bubble1, (400, 100))
        gameDisplay.blit(bubble1, (600, 200))
        gameDisplay.blit(bubble1, (200, 510))
        gameDisplay.blit(bubble2, (600, 150))
        gameDisplay.blit(bubble1, (700, 500))
        gameDisplay.blit(bubble2, (260, 20))
        
        
        # gameDisplay.blit(TextSurf, TextRect)
        # gameDisplay.blit(background, (0, 0))
        #button(message, x, y, w, h, inactive, active, returnposx, returnposy)
        return_button("Return to game", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(15)
        
def mirror(initial_x, initial_y):
    """ interaction with bathroom mirror """
    load_map("mirror")
    background = pygame.image.load("../data/flooring/mirror_surface.png")
    background=background.convert()
    background=pygame.transform.scale(background, (display_width, display_height))
    
    reflection = pygame.image.load("../data/images/screens/mirror/player_transparent.png").convert_alpha()
    reflection = pygame.transform.scale(reflection, (int(64*10), int(64*10)))
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(reflection, (300, 200))
        # gameDisplay.blit(TextSurf, TextRect)
        #button(message, x, y, w, h, inactive, active, returnposx, returnposy)
        return_button("Return to game", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(15)

def render_map(screen):
        # determine_camera(hero)
        y_pos = 0
        for line in map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos*SCALE, y_pos*SCALE, SCALE,SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

def load_map(file_name):
        with open('../data/maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line)-1, 2):
                    tiles.append(line[i])
                map.append(tiles)
            # print(map)

        
class Hero:
    def __init__(self, x_pos, y_pos):
        self.position = [x_pos, y_pos]
        self.image = pygame.image.load("../data/images/player.png")
        self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        self.rect = pygame.Rect(self.position[0], self.position[1], SCALE, SCALE)
    
    
    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]


    def render(self, screen):
        #self.rect = pygame.Rect(self.position[0]*CONFIG.SCALE, self.position[1]*CONFIG.SCALE-(camera[1]*CONFIG.SCALE),CONFIG.SCALE, CONFIG.SCALE)
        self.rect = pygame.Rect((self.position[0]), (self.position[1]), SCALE, SCALE)
        screen.blit(self.image, self.rect)
        
        
        
def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('../data/animations/1.png'))
        self.images.append(load_image('../data/animations/2.png'))
        self.images.append(load_image('../data/animations/3.png'))
        self.images.append(load_image('../data/animations/4.png'))
        self.images.append(load_image('../data/animations/5.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(22*SCALE, 15*SCALE, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        timescale=10
        self.index += 1
        if int(self.index/timescale) >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index/timescale)]
        
        
def furniture(file, tilex, tiley, rotation, scalea, scaleb):
    """load furniture into a specific area"""
    image = pygame.image.load("../data/"+str(file))
    x=tilex*SCALE
    y=tiley*SCALE
    image = pygame.transform.scale(image, (scalea, scaleb))
    image = pygame.transform.rotate(image, rotation)
    rect = pygame.Rect(x, y, scalea, scaleb)
    gameDisplay.blit(image, rect)
           

clock = pygame.time.Clock()
def main(a,b):
    # camera=[0,0]
    #where to place car
    x=a
    y=b
    # x = (display_width * 0.45)
    # y = (display_height * 0.8)
    x_change = 0 
    y_change = 0
    # print(map)
    map.clear()
    load_map("myfile")
    playerspeed=4
    # print(map)
    gameExit = False
    hero = Hero(a,b)
    # print(len(map))
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)
    
    
    while not gameExit: #GAME LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
             #KEY COMMANDS   
                keys=pygame.key.get_pressed()    
                if keys[pygame.K_LEFT]:
                    x_change=-playerspeed
                elif keys[pygame.K_RIGHT]:
                    x_change=playerspeed
                elif keys[pygame.K_UP]:
                    y_change=-playerspeed
                elif keys[pygame.K_DOWN]:
                    y_change=playerspeed
                else:
                    x_change=0 
                    y_change=0
                    
             #LOCALISED COMMANDS (OBJECT INTERACTION)
             #LOUNGE  ----------
             #Window (2, 0, 0, 33, 27) (3.05, 0, 0, 33, 27)
                if keys[pygame.K_x] and 3.05*SCALE+27 > x > 2*SCALE and y < 0*SCALE+27:
                    map.clear()
                    window(x,y)
                else:
                    pass
                
             #Book 6.5, 6.7, 0, 50, 50
                if keys[pygame.K_x] and 6.6*SCALE+50 > x > 6.6*SCALE and 6.7*SCALE < y < 6.7*SCALE+50:
                    map.clear()
                    book(x,y)
                else:
                    pass
             
             #KITCHEN ----------
             #Pool  10, 14.2, 0, 117, 92       9, 15.2, 0, 117, 92
                if keys[pygame.K_x] and 9*SCALE+117 > x > 9*SCALE and 15.2*SCALE < y < 15.2*SCALE+92:
                    map.clear()
                    pool(x, y)
                else:
                    pass
             
             #BEDROOM ---------- DONE
             #computer  22.8, 0.3, 0, 40, 65
                if keys[pygame.K_x] and x > 22.8*SCALE and y < 0.31*SCALE+65:
                    map.clear()
                    computer(x, y)
                else:
                    pass
                
            #BATHROOM ---------- DONE
            #Bath 18.3, 16.7, 0, 35, 50       20.8, 16.7, 0, 35, 50)
                if keys[pygame.K_x] and 20.5*SCALE+35 > x > 20.5*SCALE and 16.5*SCALE < y < 16.5*SCALE+50:
                    map.clear()
                    bath(x,y)
                else:
                    pass
            #Mirror 18.2, 13.3, 0, 34, 54
                if keys[pygame.K_x] and 18.2*SCALE+34 > x > 18.2*SCALE and 13.3*SCALE < y < 13.3*SCALE+54:
                    map.clear()
                    mirror(x,y)
                else:
                    pass
            
            
        
        #BOUNDARIES -----------------
        #display
        if int((x+x_change)) < 0 or int((x+x_change)) > (display_width -1-SCALE):
            x_change=0
        if int((y+y_change)) < 0 or int((y+y_change)) > (display_height -5-SCALE):
            y_change=0
        
        #Walls
        #vertical bedroom
        if  15*SCALE-SCALE < x+x_change < 15*SCALE+10 and y+y_change < 8*SCALE:
            x_change=0
        #horizontal bedroom
        if  15*SCALE-SCALE < x+x_change and 10*SCALE-SCALE < y+y_change < 10*SCALE:
            y_change=0
        #vertical bathroom
        if  15*SCALE-SCALE < x+x_change < 15*SCALE+10 and y+y_change > 13*SCALE-SCALE:
            x_change=0
        #horizontal bathroom 15, 13,
        if  15.2*SCALE-SCALE < x+x_change < 21.8*SCALE and 13*SCALE-SCALE < y+y_change < 13*SCALE:
            y_change=0
        
        #*****   ITEMS   *****
        #LOUNGE
        #tv and cabinets 8.6, 0, 0, 40, 65) (13.3, 0, 0, 40, 65)
        if  8.8*SCALE-SCALE < x+x_change < 14*SCALE+10 and y+y_change < 2*SCALE:
            x_change=0
            y_change=0
        #top sofa 5.5, 4.3, 0, 100, 60)
        if  5.45*SCALE-SCALE+5 < x+x_change < 5.5*SCALE+92 and 116 < y+y_change < 4.3*SCALE:
            x_change=0
            y_change=0
        #left sofa 4.5, 6, 0, 40, 90)
        if  4.5*SCALE-SCALE < x+x_change < 4.5*SCALE+14 and 6*SCALE - SCALE< y+y_change < 6*SCALE+60:
            x_change=0
            y_change=0
        #right sofa 9.1, 6, 0, 40, 90)
        if  320-SCALE < x+x_change < 9.1*SCALE+35 and 6*SCALE - SCALE < y+y_change < 6*SCALE+60:
            x_change=0
            y_change=0
        #coffee table  6.5, 6.7, 0, 50, 50)
        if  6.5*SCALE-SCALE+8 < x+x_change < 6.5*SCALE+48 and 6.7*SCALE - SCALE < y+y_change < 6.7*SCALE+30:
            x_change=0
            y_change=0
        #stairs and plants
        if  x+x_change < 36 and 128 < y+y_change < 288:
            x_change=0
            y_change=0
            
        #BEDROOM
        #upper 22.8, 0.3, 0, 40, 65)
        if  490 < x+x_change and y+y_change < 56:
            x_change=0
            y_change=0
        
        #desk 15.5 4
        if  528 > x+x_change > 490 and 100 < y+y_change < 196:
            x_change=0
            y_change=0
            
        #BATHROOM
        #upper
        if  660 > x+x_change > 450 and 430 < y+y_change < 452:
            x_change=0
            y_change=0
            
        #bath 
        if  676 < x+x_change < 744 and 500 < y+y_change < 588:
            x_change=0
            y_change=0
            
        #vases
        if  712 < x+x_change and y+y_change > 572:
            x_change=0
            y_change=0
            
        #KITCHEN
        #table
        if  212 > x+x_change > 92 and 428 < y+y_change < 536:
            x_change=0
            y_change=0
        
        #pool
        if  424 > x+x_change > 300 and 468 < y+y_change < 552:
            x_change=0
            y_change=0
            
        #counters
        if  20 > x+x_change and y+y_change > 408:
            x_change=0
            y_change=0
        if  84 > x+x_change and y+y_change > 584:
            x_change=0
            y_change=0
            
        
        
        
        
        
            
        # print('x is ' + str(int(((x+x_change)/display_width)*len(map[0]))))
        # print('y is ' +str(int(  ((y+y_change)/display_height)*len(map))))
        # if map[int((y+y_change)/CONFIG.SCALE)][int((x+x_change)/CONFIG.SCALE)] == 'W':
        #     y_change=0
        #     x_change=0
        # try:    
        #     if map[int((y+y_change)/CONFIG.SCALE+0.5)][int((x+x_change)/CONFIG.SCALE+0.5)] == 'W':
        #         y_change=0
        #         x_change=0  
        # except IndexError:
        #     pass          
        x+=x_change
        y+=y_change
        gameDisplay.fill(Black)
        render_map(gameDisplay)
        
        # ---------  LOUNGE  ------------
        #sofa 1
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_447.png", 2, 4, -90, 50, 50)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_448.png", 2, 5, -90, 50, 50)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_449.png", 2, 6, -90, 50, 50)
        furniture("../data/images/lounge/sofa_left.png", 4.5, 6, 0, 40, 90)
        #armchair
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_450.png", 3, 2, -160, 50, 50)
        furniture("../data/images/lounge/poof.png", 9, 5.1, 0, 40, 40)            
        #sofa 2
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_449.png", 7, 3, 90, 50, 50)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_448.png", 7, 4, 90, 50, 50)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_448.png", 7, 5, 90, 50, 50)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_447.png", 7, 6, 90, 50, 50)
        furniture("../data/images/lounge/sofa_right.png", 9.1, 6, 0, 40, 90)
        #sofa top
        furniture("../data/images/lounge/sofa_top.png", 5.5, 4.3, 0, 100, 60)       
        #coffee table
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_452.png", 3.75, 4, 90, 100, 100)
        # furniture("../data/tiles1/Tilesheets/table_middle.png", 4.5, 5, 0, 40)
        # furniture("../data/tiles1/Tilesheets/table_legs.png", 4.5, 6, 0, 40)
        furniture("../data/images/lounge/coffee_table.png", 6.5, 6.7, 0, 50, 50)
        #TV
        furniture("../data/images/lounge/tv_unit.png", 10, 0.3, 0, 100, 60)
        #cabinets
        furniture("../data/images/lounge/cabinet.png", 8.6, 0, 0, 40, 65)
        furniture("../data/images/lounge/cabinet.png", 13.3, 0, 0, 40, 65)
        #window 
        furniture("../data/images/lounge/window.png", 2, 0, 0, 33, 27)
        furniture("../data/images/lounge/window.png", 3.05, 0, 0, 33, 27)
        #lamp
        furniture("../data/images/lounge/lamp.png", 4, 4, 0, 34, 70)
        #tv rug
        furniture("../data/images/lounge/tv_rug.png", 9.5, 2.3, 0, 128, 64)
        #book
        furniture("../data/images/lounge/book.png", 6.6, 6.7, 15, 15, 20)
        #tv chair 
        # furniture("../data/images/lounge/chair.png", 12.2, 3, 2, 33, 30)
        #plants
        furniture("../data/images/lounge/plant3.png", 0.1, 0.2, 0, int(33*1.1), int(59*1.1))
        furniture("../data/images/lounge/plant2.png", 13.3, 17.5, 2, 49, 76)
        
        #globe
        furniture("../data/images/lounge/side_table.png", 8.2, 18, 2, int(55*0.9), int(64*0.9))
        furniture("../data/images/lounge/globe.png", 8.4, 17.3, 2, 40, 57)
        
        # ---------  OTHER  ------------
        #chairs
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_531.png", 18, 16, 280, 40, 40)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_531.png", 20, 14.3, 160, 40, 40)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_531.png", 21, 16, 80, 40, 40)
        # #kitchen table
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_506.png", 19, 15, 90, 90, 90)
        
        #separators
        #bedroom
        furniture("../data/images/walls/Mytile_1.png", 15, 1, 0, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 15, 2, 0, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 15, 4, 0, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 15, 6, 0, 10, 70)
        
        furniture("../data/images/walls/Mytile_1.png", 15, 10, -90, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 17, 10, -90, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 19, 10, -90, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 21.2, 10, -90, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 23, 10, -90, 10, 90)
        #bathroom
        furniture("../data/images/walls/Mytile_1.png", 15, 13, 0, 10, 70)
        furniture("../data/images/walls/Mytile_1.png", 15, 15, 0, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 15, 16.2, 0, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 15, 18, 0, 10, 90)
        
        furniture("../data/images/walls/Mytile_1.png", 15, 13, -90, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 17, 13, -90, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 19.2, 13, -90, 10, 90)
        # furniture("../data/topdown-shooter/PNG/Tiles/Mytile_1.png", 21.2, 10, -90, 10, 90)
        
        
        # ---------  BEDROOM  ------------
        #bed
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_106.png", 20, 1, 180, 60, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_107.png", 19, 1, 180,60, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_79.png", 20, 2, 180, 60, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_80.png", 19, 2, 180, 60, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_52.png", 20, 3, 180, 60, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_53.png", 19, 3, 180, 60, 60)
        furniture("../data/images/bedroom/bed.png", 19, 0.5, 0, 60, 100)
        #bedside tables
        furniture("../data/images/bedroom/bedside_table.png", 21, 0.5, 0, 50, 40)
        furniture("../data/images/bedroom/bedside_table.png", 17.2, 0.5, 0, 50, 40)
        #window
        furniture("../data/images/bedroom/bedroom_curtains.png", 15.5, 0.1, 0, 45, 35)
        #desk and chair 
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_505.png", 20.9, 7.8, 160, 50, 50)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_205.png", 18.75, 9.2, 0, 120, 40)
        furniture("../data/images/bedroom/desk.png", 15.5, 4, 0, 55, 85)
        #computer
        # furniture("../data/tiles2/PNG/colored/genericItem_color_049.png", 19.4, 9.2, 0, 25, 25)
        furniture("../data/images/bedroom/computer.png", 22.8, 0.3, 0, 40, 65)
        #Bedroom Rug
        furniture("../data/images/bedroom/bedroom_rug.png", 19, 5, 0, 130, 130)
        # furniture("../data/images/walls/Mytile_1.png", 15, 21, 0, 10, 70)
        #lamp
        furniture("../data/images/bedroom/lamp.png", 23.8, 7, 0, 33, 75)
        
        
        # ---------  BATHROOM  ------------
        #toilet
        furniture("../data/images/bathroom/toilet.png", 20, 13.2, 0, 23, 52)
        #sink
        furniture("../data/images/bathroom/sink.png", 15.5, 13.2, 0, 62, 54)
        #bathmat
        furniture("../data/images/bathroom/bathmat.png", 20.8, 16.7, 0, 35, 50)
        #mirror
        furniture("../data/images/bathroom/bathroom_mirror.png", 18.2, 13.3, 0, 34, 54)
        #harp
        furniture("../data/images/bathroom/harp.png", 15.5, 16, 0, int(52*0.8), int(72*0.8))
        #plant
        furniture("../data/images/lounge/plant3.png", 15.7, 18, 0, int(33*1.15), int(59*1.15))
        #vases
        furniture("../data/images/bathroom/vases.png", 23.1, 18.4, 0, int(61*1), int(53*1))
        
        
        
        # ---------  KITCHEN  ------------
        #ISLAND
        furniture("../data/images/kitchen/kitchen_island.png", -0.08, 13.6, 180, 60, 96)
        #side
        furniture("../data/images/kitchen/kitchen_side.png", 0, 16.5, 0, 27, 90)
        furniture("../data/images/kitchen/kitchen_side.png", 0, 19.2, 90, 26, 90)

        #chairs
        furniture("../data/images/kitchen/chair_left.png", 3.5, 14.2, 0, 36, 57)
        furniture("../data/images/kitchen/chair_left.png", 3.5, 15.2, 0, 36, 57)
        furniture("../data/images/kitchen/chair_right.png", 5.9, 14.2, 0, 32, 53)
        furniture("../data/images/kitchen/chair_right.png", 6, 15.2, 0, 32, 53)
        #table 3, 11, 0, int(72*1.2), int(87*1.2))
        furniture("../data/images/kitchen/table.png", 4, 14, 0, int(72*1.2), int(87*1.2))
        furniture("../data/images/kitchen/doughnuts.png", 5, 14.3, 0, int(30*1), int(34*1))
        furniture("../data/images/kitchen/fruit.png", 4.6, 15.7, 0, int(44*1), int(24*1))
        #pool table
        furniture("../data/images/kitchen/pool_table.png", 10, 15.2, 0, 117, 92)
        furniture("../data/images/kitchen/balls.png", 11, 15.9, 0, 32, 28)
        #cueues
        furniture("../data/images/kitchen/cueues.png", 14, 13.5, 0, 24, 65)
        
        # ---------  Corridor  ------------
        #door
        furniture("../data/images/corridor/door.png", 24.8, 11, 0, 8, 50)
        #doormat
        furniture("../data/images/corridor/doormat.png", 23.8, 11.1, 0, int(87/2.8), int(128/2.8))
        #plants by stairs
        furniture("../data/images/lounge/plant.png", -0.1,4.5, 0, 51, 81)
        #stairs
        furniture("../data/images/corridor/stairs.png", -0.6, 6, 0, int(80/1.5), int(96/1.5))
        furniture("../data/images/lounge/plant.png", -0.1,7, 0, 51, 81)
        #vase
        furniture("../data/images/corridor/vase.png", 0,11, 0, 30, 30)
        
        
        
        
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_153.png", 18.5, 9,     180, 60, 30)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_177.png", 19.5, 9,     90,  30, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_152.png", 20.5, 9,     180, 60, 30)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_152.png", 18.5, 9.55,  0,   60, 30)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_177.png", 19.5, 9.55,  -90, 30, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_153.png", 20.5, 9.55,  0,   60, 30)
        
        print(x,y)
        hero.render(gameDisplay)
        my_group.update()
        my_group.draw(gameDisplay)
        hero.update_position((x, y))
        
        
        
        pygame.display.update()
        clock.tick(50)
        

pygame.QUIT
game_intro()
# if __name__ == "__main__":
    # main(100)