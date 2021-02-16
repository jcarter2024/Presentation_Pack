""" Creating a room that I can move around in. Also needs files CONFIG"""
try:
    import sys
    # import random
    # import os
    # import getopt
    import pygame
    # import time
    # import numpy as np
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
            print(action)
            if action <1:
                main(a,b)
            elif 0.9 < action < 2:
                pygame.quit()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, w, h))
            
    smallText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2), y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    
def nextpage(msg,x,y,w,h,inactive, active, a, b, string):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active, (x, y, w, h))
        if click[0] == 1 and string != None:
            if string == 0:
                print("yes")
                game_intro(2)
            elif string == 1:
                pygame.quit()
            elif string == 2:
                window(a, b, 2)
            elif string ==3:    
                globe(a,b,2)
            elif string ==4:    
                pool(a,b,2)
            elif string ==5:    
                book(a,b,2)
            elif string ==6:    
                computer(a,b,2)
            elif string ==7:    
                desk(a,b,2)
            elif string ==8:    
                bath(a,b,2)
            elif string ==9:    
                mirror(a,b,2)
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, w, h))
            
    smallText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 15)
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

def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        # don't pause for spaces
        if letter != ' ':
            yield tmp
            
class DynamicText(object): #credit to stack overflow 
    def __init__(self, font, text, pos, color, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.pos = pos
        self.color=color
        self.autoreset = autoreset
        self.update()

    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, self.color) #color
            except StopIteration: 
                self.done = True
                if self.autoreset: self.reset()

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)
    
def game_intro(page):
    """ Essential for a good start"""
    pygame.mixer.music.play(-1)
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
        #p1
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        largeText2=pygame.font.SysFont ("bitstreamverasans", 30)
        smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
        
        if page==1:
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
            nextpage("Enter!", display_width/2-150, 300, 200, 100, Brown, Bright_green, 764, 360, 0)
            button("Quit!", display_width/2, 400, 200, 100, Brown, Bright_red, 100, 100, 1)
        elif page==2:
            TextSurf, TextRect = text_objects("This program was coded using pygame,", smalltext)
            TextSurf2, TextRect2 = text_objects("built on ARCHER2,  ", smalltext)
            TextSurf3, TextRect3 = text_objects("and developed via github.", smalltext)
            TextSurf4, TextRect4 = text_objects("Credit to gathertown for inspiring this presentation format. .", smalltext)
            TextSurf5, TextRect5 = text_objects("Visit the lounge window to begin...", smalltext)
            
            TextRect.center = (display_width/2, 100)
            TextRect2.center = (display_width/2, 200)
            TextRect3.center = (display_width/2, 300)
            TextRect4.center = (display_width/2, 400)
            TextRect5.center = (display_width/2, 600)
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)
            gameDisplay.blit(TextSurf3, TextRect3)
            gameDisplay.blit(TextSurf4, TextRect4)
            gameDisplay.blit(TextSurf5, TextRect5)
            button("Enter!", 650, 550, 100, 50, Brown, Bright_green, 764, 360, 0)

        else:
            pass
        
        pygame.display.update()
        clock.tick(15)
    
        
def computer(initial_x, initial_y, page):
    """ interaction with a computer """
    load_map("computer")
    background = pygame.image.load("../data/images/screens/computer/terminal.png")
    background=background.convert()
    background=pygame.transform.scale(background, (display_width, display_height))
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    intro = True
    #Page 1
    p1line1 = DynamicText(smalltext,"Running WRF simulations is an intensive process. With", (75, 98), Green, autoreset = False)
    p1line2 = DynamicText(smalltext,"supercomputer access a single two-day simulation can be", (75, 128), Green, autoreset = False)
    p1line3 = DynamicText(smalltext, "conducted within 24 hours at high resolution.", (75, 158),Green, autoreset = False)
    p1line4 = DynamicText(smalltext,"Currently, this research is limited by the Manchester", (75, 218),Green, autoreset = False)
    p1line5 = DynamicText(smalltext, " CSF-HPC which is extremely busy and often undergoes", (75, 248),Green, autoreset = False,)
    p1line6 = DynamicText(smalltext," periods of downtime.", (75, 278),Green, autoreset = False)
    p1line7 = DynamicText(smalltext, "With the use of Archer2, simulations can be carried out ", (75, 338),Green, autoreset = False)
    p1line8 = DynamicText(smalltext, "at higher resolutions without a large time penalty. This" ,(75, 368),Green, autoreset = False)
    p1line9 = DynamicText(smalltext, "will directly impact ISHMAEL simulations by increasing" ,(75, 398), Green,autoreset = False)
    p1line10 = DynamicText(smalltext, "the amount of ice-spheroids available, creating more" ,(75, 428), Green,autoreset = False)
    p1line11 = DynamicText(smalltext, "localised feedback to the riming process..." ,(75, 458), Green,autoreset = False)
    
    #page 2
    p2line1 = DynamicText(smalltext, "...Archer will provide a crucial second platform to " ,(75, 98), Green,autoreset = False)
    p2line2 = DynamicText(smalltext, "conduct simulations,not only broadening the availability of  " ,(75, 128),Green, autoreset = False)
    p2line3 = DynamicText(smalltext, "simulation time, but also providing an important safety net" ,(75, 158),Green, autoreset = False)
    p2line4 = DynamicText(smalltext, "to combat HPC downtime  ", (75, 188), Green, autoreset = False)
    p2line5 = DynamicText(smalltext, "Go to the desk to hear more about BASH " ,(75, 438),Green, autoreset = False)

    #Page 2
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (0, 0))
        
        if page ==1:            
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
            p1line11.draw(gameDisplay)
            p1line11.update()
            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 6)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
   
        pygame.display.update()
        clock.tick(50)

def window(initial_x, initial_y, page):
    """ interaction with a computer """
    load_map("window")
    pygame.time.set_timer(pygame.USEREVENT, 200)
    clock.tick(2)
    #clouds
    cloud1 = pygame.image.load("../data/images/screens/window/cloud4.png").convert_alpha()
    cloud2 = pygame.image.load("../data/images/screens/window/cloud5.png").convert_alpha()
    cloud3 = pygame.image.load("../data/images/screens/window/cloud7.png").convert_alpha()
    #trees
    tree1 = pygame.image.load("../data/images/screens/window/tree1.png").convert_alpha()
    tree2 = pygame.image.load("../data/images/screens/window/tree2.png").convert_alpha()
    #castle
    castle = pygame.image.load("../data/images/screens/window/castle.png").convert_alpha()
    #crystal
    crystal = pygame.image.load("../data/images/screens/window/crystal.png").convert_alpha()
    
    cloud1=pygame.transform.scale(cloud1, (int(228/2.5), int(124/2.5)))
    cloud2=pygame.transform.scale(cloud2, (int(238/1.5), int(135/1.5)))
    cloud3=pygame.transform.scale(cloud3, (int(234/3), int(118/3)))
    cloud4=pygame.transform.scale(cloud3, (int(238/1.5), int(135/1.5)))
    cloud5=pygame.transform.scale(cloud2, (int(234/3), int(118/3)))
    tree1=pygame.transform.scale(tree1, (int(129/4), int(230/4)))
    tree2=pygame.transform.scale(tree2, (int(106/4), int(241/4)))
    castle=pygame.transform.scale(castle, (int(204/4), int(182/4)))
    crystal=pygame.transform.scale(crystal, (int(726/6), int(1018/6)))
    
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    verysmalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 18)
    
    box=pygame.image.load("../data/flooring/white_transparent.png").convert_alpha()
    box1=pygame.transform.scale(box, (353, 255))
    box2=pygame.transform.scale(box, (353, 290))
    largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
    #Page 1
    p1line1 = DynamicText(smalltext, "Though clouds can exist on the kilometre scale, they consist ", (40, 68), Black, autoreset=False)
    p1line2 = DynamicText(smalltext, "entirely of small particles that occupy the microscale, typically", (40,98),Black, autoreset=False)
    p1line3 = DynamicText(smalltext, "growing no larger than a few millimetres. These particles each ",(40, 128),Black, autoreset=False)
    p1line4 = DynamicText(smalltext, "have unique qualities that are generated during formation and ", (40, 158),Black, autoreset=False)
    p1line5 = DynamicText(smalltext, "are built upon by interactions with their local environment.", (40, 188),Black, autoreset=False)
    p1line6 = DynamicText(smalltext, "Capturing the consequences of those interactions is a key", (40, 328),Black, autoreset=False)
    p1line7 = DynamicText(smalltext, "challenge for weather forecasting, as the accuracy of forecasts ", (40, 358),Black, autoreset=False)
    p1line8 = DynamicText(smalltext, "depends on a computational model’s ability to correctly predict ", (40, 388), Black,autoreset=False)
    p1line9 = DynamicText(smalltext, "the interactions of hundreds of millions of particles.",(40, 418),Black, autoreset=False)
    p1line10 = DynamicText(smalltext, "One important subset of these particles is cloud ice.",(40, 458),Black, autoreset=False)
    p1line11 = DynamicText(verysmalltext, "A single rimed plate-like crystal, Rango et al.,(2003)",(160, 540),Black, autoreset=False)
    #Page2
    p2line1 = DynamicText(smalltext, "Unlike liquid droplets, ice can form in a multitude of shapes, ", (40, 68),Black, autoreset=False)
    p2line2 = DynamicText(smalltext, "from stellar crystals to bullets, and this shape affects the ", (40, 98),Black, autoreset=False)
    p2line3 = DynamicText(smalltext, "crystal’s ability to interact with other crystals. It may become", (40, 128),Black, autoreset=False)
    p2line4 = DynamicText(smalltext, "more likely to fracture, generating reflective ice-shards, or it ", (40, 158),Black, autoreset=False)
    p2line5 = DynamicText(smalltext, "may aggregate to other crystals more readily, creating large flakes.", (40, 188),Black, autoreset=False)
    p2line6 = DynamicText(smalltext, "My research examines how models reproduce the riming process, an", (40, 358),Black, autoreset=False)
    p2line7 = DynamicText(smalltext, "interaction between supercooled liquid water and cloud ice.", (40, 388),Black, autoreset=False)
    p2line8 = DynamicText(smalltext, "Head to the Globe to learn about weather models and simulated ice.", (40, 458),Black, autoreset=False)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            # if event.type == pygame.USEREVENT: message.update()
                
        
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
        gameDisplay.blit(box1, (32,32))
        gameDisplay.blit(box1, (416,32))
        gameDisplay.blit(box2, (32,320))
        gameDisplay.blit(box2, (416,320))
        
        gameDisplay.blit(crystal, (20,478))
        
        
        if page ==1:  
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
            p1line11.draw(gameDisplay)
            p1line11.update()
            
            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 2)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            p2line6.draw(gameDisplay)
            p2line6.update()
            p2line7.draw(gameDisplay)
            p2line7.update()
            p2line8.draw(gameDisplay)
            p2line8.update()
            p1line11.draw(gameDisplay)
            p1line11.update()
     
            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
            
        
        pygame.display.update()
        clock.tick(55)

def book(initial_x, initial_y, page):
    """ interaction with a computer """
    load_map("book")
    background = pygame.image.load("../data/images/screens/book/newspaper.png").convert_alpha()
    background=pygame.transform.scale(background, (int(display_width/1.1),int(display_height/1.1)))
    bl = pygame.image.load("../data/images/screens/book/blizzard.png").convert_alpha()
    bl=pygame.transform.scale(bl, (int(2527/7),int(1687/7)))
    # background=pygame.transform.rotate(background, 4)
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    verysmalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 18)
    intro = True
    p1line1 = DynamicText(smalltext,"To compare ISHMAEL and conventional schemes, a winter ", (60, 168), Black, autoreset = False)
    p1line2 = DynamicText(smalltext,"storm that impacted the north-east United States in", (60, 188), Black, autoreset = False)
    p1line3 = DynamicText(smalltext, "February 2013 was simulated. The storm brought record ,", (60, 208),Black, autoreset = False)
    p1line4 = DynamicText(smalltext, "snowfall to several areas, causing two states to declare ", (60, 228),Black, autoreset = False,)
    p1line5 = DynamicText(smalltext,"a state of emergency. It was particularly devastating to.", (60, 248),Black, autoreset = False)
    p1line6 = DynamicText(smalltext, "infrastructure, aviation and property", (60, 268),Black, autoreset = False)
    p1line7 = DynamicText(smalltext, "This storm was chosen due to its well-defined phases" ,(60, 288),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "of precipitation, which brought snow and rain initially" ,(60, 308), Black,autoreset = False)
    p1line9 = DynamicText(smalltext, "followed by a period of intense riming, and concluded " ,(60, 328), Black,autoreset = False)
    p1line10 = DynamicText(smalltext, "by snowy aggregates ",(60, 348), Black,autoreset = False)
    p1line11 = DynamicText(verysmalltext, "Electricity cut off and Vehicles snowed in! ",(30, 530), Black,autoreset = False)
    p1line12 = DynamicText(verysmalltext, "The 2013 Storm hits Billerica, Massachusetts",(30, 550), Black,autoreset = False)
    #Page 2by snowy aggregates. 
    p2line1 = DynamicText(smalltext,"Radar measurements indicate the cloud particle population aloft, ", (60, 168), Black, autoreset = False)
    p2line2 = DynamicText(smalltext,"whilst on-the-ground recordings of crystal habit took place at", (60, 188), Black, autoreset = False)
    p2line3 = DynamicText(smalltext, "Stony Brook University, Long Island.", (60, 208),Black, autoreset = False)
    p2line4 = DynamicText(smalltext, "The ISHMAEL model was compared to its predecessor and ", (60, 248),Black, autoreset = False,)
    p2line5 = DynamicText(smalltext,"verified with these observational datasets.", (60, 268),Black, autoreset = False)
    p2line6 = DynamicText(smalltext, "Head to the computer to learn how this week's course will", (60, 308),Black, autoreset = False)
    p2line7 = DynamicText(smalltext, "impact my future research" ,(60, 328),Black, autoreset = False)
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (display_width/30, display_height/30))
        gameDisplay.blit(bl, (380,350))
        if page ==1:            
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
            p1line11.draw(gameDisplay)
            p1line11.update()
            p1line12.draw(gameDisplay)
            p1line12.update()
        

            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 5)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            p2line6.draw(gameDisplay)
            p2line6.update()
            p2line7.draw(gameDisplay)
            p2line7.update()
            p1line12.draw(gameDisplay)
            p1line12.update()

            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(55)
        
def pool(initial_x, initial_y, page):
    """ interaction with a computer """
    load_map("pool")
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    intro = True
    #Page 1
    p1line1 = DynamicText(smalltext,"Liquid water can exist at temperatures as low as", (60, 128), Black, autoreset = False)
    p1line2 = DynamicText(smalltext,"-40 degrees Celsius in a stable enough environment.", (50, 158), Black, autoreset = False)
    p1line3 = DynamicText(smalltext, "Often, ice that forms at the top of clouds gains mass", (60, 188),Black, autoreset = False)
    p1line4 = DynamicText(smalltext, "through a field of supercooled droplets. On impact", (120, 218),Black, autoreset = False,)
    p1line5 = DynamicText(smalltext,"droplets accrete to - or rime, the surface of the ice.", (140, 248),Black, autoreset = False)
    p1line6 = DynamicText(smalltext, "immediately freezing and contributing a further mass gain", (160, 278),Black, autoreset = False)
    p1line7 = DynamicText(smalltext, "Riming has several interesting aspects, for" ,(160, 338),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "example, it depletes the cloud’s droplet and ice" ,(160, 368), Black,autoreset = False)
    p1line9 = DynamicText(smalltext, "population, reducing overall cloud lifetime. It also  " ,(160, 398), Black,autoreset = False)
    p1line10 = DynamicText(smalltext, "alters the crystal shape, distorting the aerodynamic",(160, 428), Black,autoreset = False)
    p1line11 = DynamicText(smalltext,"profile of the ice and further increasing fall speed",(160, 458), Black,autoreset = False)
    #Page 2
    p2line1 = DynamicText(smalltext,"A simulation of riming is provided at this link:", (60, 128), Black, autoreset = False)
    p2line2 = DynamicText(smalltext,"https://glowscript.org/ using file:.", (60, 158), Black, autoreset = False)
    p2line3 = DynamicText(smalltext, "It is not possible to capture the exact shapes of crystals", (60, 228),Black, autoreset = False)
    p2line4 = DynamicText(smalltext, "but the ISHMAEL scheme can parametrise them by representing", (120, 258),Black, autoreset = False,)
    p2line5 = DynamicText(smalltext,"geometries with spheroids. This inclusion allows", (140, 288),Black, autoreset = False)
    p2line6 = DynamicText(smalltext, "the riming process to be more closely tied to the size", (160, 318),Black, autoreset = False)
    p2line7 = DynamicText(smalltext, "evolution of the ice field. Examinations of the ISHMAEL" ,(160, 348),Black, autoreset = False)
    p2line8 = DynamicText(smalltext, "model indicate that it more accurately captures the" ,(160, 378), Black,autoreset = False)
    p2line9 = DynamicText(smalltext, "scale of riming than traditional models, and can produce" ,(160, 408), Black,autoreset = False)
    p2line10 = DynamicText(smalltext, "a more spatially accurate precipitation forecast",(160, 438), Black,autoreset = False)
    p2line11 = DynamicText(smalltext,"To read more about the case study, visit the coffee table",(160, 468), Black,autoreset = False)
  
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        11, 14.9, 0, 40, 35
        balls = pygame.image.load("../data/images/kitchen/balls.png").convert_alpha()
        balls=pygame.transform.scale(balls, (int(40*10), int(35*10)))
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(balls, (600, -100))
        
        
        if page ==1: 
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
            p1line11.draw(gameDisplay)
            p1line11.update()

            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 4)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            p2line6.draw(gameDisplay)
            p2line6.update()
            p2line7.draw(gameDisplay)
            p2line7.update()
            p2line8.draw(gameDisplay)
            p2line8.update()
            p2line9.draw(gameDisplay)
            p2line9.update()
            p2line10.draw(gameDisplay)
            p2line10.update()
            p2line11.draw(gameDisplay)
            p2line11.update()
            
            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        pygame.display.update()
        clock.tick(55)
    
def bath(initial_x, initial_y, page):
    """ interaction with a computer """
    load_map("bath")
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    ducky = pygame.image.load("../data/images/screens/bath/duck.png").convert_alpha()
    ducky = pygame.transform.scale(ducky, (int(40*6), int(38*6)))
    bubble = pygame.image.load("../data/images/screens/bath/bubble.png").convert_alpha()
    bubble1 = pygame.transform.scale(bubble, (int(70), int(70)))
    bubble2 = pygame.transform.scale(bubble, (int(40), int(40)))
    
    intro = True
    #page 1
    p1line1 = DynamicText(smalltext,"The GIT component of this course will ", (60, 68), Black, autoreset = False)
    p1line2 = DynamicText(smalltext,"allow for my research tools to be structured,", (50, 98), Black, autoreset = False)
    p1line3 = DynamicText(smalltext, " stored and developed in a cohesive manner.", (60, 128),Black, autoreset = False)
    p1line4 = DynamicText(smalltext, "I often develop lengthy code, but have been unwilling ", (90, 188),Black, autoreset = False)
    p1line5 = DynamicText(smalltext, "to use GIT due to its perceived complexity. Now code", (120, 218),Black, autoreset = False,)
    p1line6 = DynamicText(smalltext,"can be safely backed up, and shared more easily ", (140, 248),Black, autoreset = False)
    p1line7 = DynamicText(smalltext, "for collaboration. ", (160, 278),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "As I work on and develop the ISHMAEL code, it will be" ,(160, 368),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "essential to have records that can be shared with", (160, 398),Black, autoreset = False)
    p1line9 = DynamicText(smalltext, "its authors across the world. Most importantly it will " ,(160, 428), Black,autoreset = False)
    p1line10 = DynamicText(smalltext, "protect against the main source of error, my own edits... " ,(190, 458), Black,autoreset = False)
    #Page 2
    p2line1 = DynamicText(smalltext,"...that break the code in ever more confusing", (90, 128), Black, autoreset = False)
    p2line2 = DynamicText(smalltext," and deceptive ways.", (90, 158), Black, autoreset = False)
    p2line3 = DynamicText(smalltext,"Note: This entire game was developed using Git!", (160, 308), Black, autoreset = False)

    p2line4 = DynamicText(smalltext, "Head to the mirror to 'reflect' on this presentation", (190, 458),Black, autoreset = False)
    
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        
        gameDisplay.blit(ducky, (650, 20))
        gameDisplay.blit(bubble1, (400, 100))
        gameDisplay.blit(bubble1, (600, 200))
        gameDisplay.blit(bubble1, (200, 510))
        gameDisplay.blit(bubble2, (600, 150))
        gameDisplay.blit(bubble1, (700, 500))
        gameDisplay.blit(bubble2, (260, 20))
        
        if page ==1:  
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 8)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()

            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
   
        pygame.display.update()
        clock.tick(55)
        
def mirror(initial_x, initial_y, page):
    """ interaction with bathroom mirror """
    # load_map("mirror")
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    background = pygame.image.load("../data/flooring/mirror_surface.png")
    background=background.convert()
    background=pygame.transform.scale(background, (display_width, display_height))
    
    reflection = pygame.image.load("../data/images/screens/mirror/player_transparent.png").convert_alpha()
    reflection = pygame.transform.scale(reflection, (int(64*10), int(64*10)))
    
    intro = True
    #page 1
    p1line1 = DynamicText(smalltext,"To recap (and reflect), the content delivered on this course", (50, 68), Black, autoreset = False)
    p1line2 = DynamicText(smalltext,"will make for a much more efficient workflow. ", (50, 98), Black, autoreset = False)
    p1line3 = DynamicText(smalltext, "My research seeks to understand how we can improve computational", (50, 158),Black, autoreset = False)
    p1line4 = DynamicText(smalltext, "models of the riming process, by incorporating ice shape ", (50, 188),Black, autoreset = False)
    p1line5 = DynamicText(smalltext, "WRF is used to simulate storm events, during which", (50, 248),Black, autoreset = False,)
    p1line6 = DynamicText(smalltext,"microphysics schemes are compared and assessed to deduce their accuracy", (50, 278),Black, autoreset = False)
    p1line7 = DynamicText(smalltext, "These simulations are impeded by a lack of compute resource ", (50, 308),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "which will be resolved by splitting my research between two..." ,(50, 338),Black, autoreset = False)
    
    #page 2
    p2line1 = DynamicText(smalltext,"...HPC facilities, and by utilising ARCHER2 to conduct the ", (50, 68), Black, autoreset = False)
    p2line2 = DynamicText(smalltext,"most intensive simulations. Access to two facilities is", (50, 98), Black, autoreset = False)
    p2line3 = DynamicText(smalltext,"crucial to accessing resources during downtime.", (50, 128), Black, autoreset = False)
    p2line4 = DynamicText(smalltext, "Compiling and editing this code is difficult, but made easier ", (50, 188),Black, autoreset = False)
    p2line5 = DynamicText(smalltext, "by increased knowledge of command-line tools. ", (50, 208),Black, autoreset = False)
    p2line6 = DynamicText(smalltext, "Documenting edits to the source code is now possible with GIT", (50, 268),Black, autoreset = False,)
    p2line7 = DynamicText(smalltext,"This allows for potentially catastrophic errors to be reverted and", (50, 298),Black, autoreset = False)
    p2line8 = DynamicText(smalltext, "also simplifies international collaboration.", (50, 328),Black, autoreset = False)
    p2line9 = DynamicText(smalltext, "which will be resolved by splitting my research between two" ,(50, 358),Black, autoreset = False)
    
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(reflection, (300, 200))
        if page ==1:   
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()



            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 9)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            p2line6.draw(gameDisplay)
            p2line6.update()
            p2line7.draw(gameDisplay)
            p2line7.update()
            p2line8.draw(gameDisplay)
            p2line8.update()
            p2line9.draw(gameDisplay)
            p2line9.update()

            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
   
 
        pygame.display.update()
        clock.tick(55)
        
def globe(initial_x, initial_y, page):
    """ interaction with bathroom mirror """
    # load_map("mirror")
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    background = pygame.image.load("../data/images/screens/globe/map.png")
    background=background.convert()
    background=pygame.transform.scale(background, (display_width, display_height))
    
    box=pygame.image.load("../data/flooring/white_transparent.png").convert_alpha()
    box1=pygame.transform.scale(box, (650, 460))
    
    intro = True
    #Page 1
    p1line1 = DynamicText(smalltext,"No computer in the world is powerful enough to simulate", (110, 68), Black, autoreset = False)
    p1line2 = DynamicText(smalltext,"even a few cubic metres of cloud particles. To scale ", (110, 98), Black, autoreset = False)
    p1line3 = DynamicText(smalltext, "the cloud, models employ parametrisations that broadly", (110, 158),Black, autoreset = False)
    p1line4 = DynamicText(smalltext, "capture qualities of the particle population and portion ", (110, 188),Black, autoreset = False)
    p1line5 = DynamicText(smalltext, "the particle size distribution into bins. Each size", (110, 218),Black, autoreset = False,)
    p1line6 = DynamicText(smalltext,"range can be operated on as one, with particle", (110, 248),Black, autoreset = False)
    p1line7 = DynamicText(smalltext, "interactions determining the new size distribution at ", (110, 278),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "the end of the time step " ,(110, 308),Black, autoreset = False)
    p1line9 = DynamicText(smalltext, "A weather model employs a microphysics scheme to " ,(110, 368),Black, autoreset = False)
    p1line10 = DynamicText(smalltext,"calculate the changing distribution but these schemes  " ,(110, 398),Black, autoreset = False)
    p1line11= DynamicText(smalltext,"vary in the qualities they record. Ice shape has often" ,(110, 428),Black, autoreset = False)
    p1line12= DynamicText(smalltext, " not been properly accounted for due...", (110, 458),Black, autoreset = False)                  
    #Page 2
    p2line1 = DynamicText(smalltext,"...to its complexity, but advances in computational power ", (110, 128), Black, autoreset = False)
    p2line2 = DynamicText(smalltext,"have provided an opportunity to more efficiently ", (110, 158), Black, autoreset = False)
    p2line3 = DynamicText(smalltext,"represent the shape of ice. Now the ISHMAEL microphysics", (110, 188), Black, autoreset = False)
    p2line4 = DynamicText(smalltext, " scheme  offers a unique opportunity to investigate the ", (110, 218),Black, autoreset = False)
    p2line5 = DynamicText(smalltext, "effects of riming. ", (110, 248),Black, autoreset = False)
    p2line6 = DynamicText(smalltext, "Go to the Pool table to learn more about cloud ", (110, 408),Black, autoreset = False,)
    p2line7 = DynamicText(smalltext, "particle collisions", (110, 438),Black, autoreset = False,)

    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        TextSurf, TextRect = text_objects("I am a computer ", largeText)
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(box1, (100,60))
        
        if page ==1:   
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
            p1line11.draw(gameDisplay)
            p1line11.update()
            p1line12.draw(gameDisplay)
            p1line12.update()

            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 3)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            p2line6.draw(gameDisplay)
            p2line6.update()
            p2line7.draw(gameDisplay)
            p2line7.update()



            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
        
        pygame.display.update()
        clock.tick(55)

def desk(initial_x, initial_y, page):
    """ interaction with desk """
    # load_map("mirror")
    smalltext=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 25)
    background = pygame.image.load("../data/flooring/pool_green2.png")
    background=background.convert()
    background=pygame.transform.scale(background, (display_width, display_height))
    
    book = pygame.image.load("../data/images/screens/desk/books.png").convert_alpha()
    pencil = pygame.image.load("../data/images/screens/desk/pencil.png").convert_alpha()
    book = pygame.transform.scale(book, (int(260*2), int(280*2)))
    pencil = pygame.transform.scale(pencil, (int(260), int(280)))
    pencil=pygame.transform.rotate(pencil,190)
    
    intro = True
    #Page 1
    p1line1 = DynamicText(smalltext,"The BASH component of this course has ", (20, 68), Black, autoreset = False)
    p1line2 = DynamicText(smalltext,"provided new tools for file handling,", (20, 98), Black, autoreset = False)
    p1line3 = DynamicText(smalltext, "that will allow for more efficient", (20, 128),Black, autoreset = False)
    p1line4 = DynamicText(smalltext, "workflows, and increased confidence ", (20, 158),Black, autoreset = False)
    p1line5 = DynamicText(smalltext, "on the command line.  ", (20, 188),Black, autoreset = False,)
    p1line6 = DynamicText(smalltext," Compiling WRF and making amendments to its source", (20, 248),Black, autoreset = False)
    p1line7 = DynamicText(smalltext, "code can be a lengthy and stressful process. ", (20, 278),Black, autoreset = False)
    p1line8 = DynamicText(smalltext, "The addition of new commands, and correct use of " ,(20, 308),Black, autoreset = False)
    p1line9 = DynamicText(smalltext, " environmental variables in particular, will be integral  " ,(20, 368),Black, autoreset = False)
    p1line10 = DynamicText(smalltext, "to resolving virtual...", (20, 398),Black, autoreset = False)
    #Page 2
    p2line1 = DynamicText(smalltext,"...environment issues.  ", (20, 68), Black, autoreset = False)
    p2line2 = DynamicText(smalltext,"Interacting with system files is inefficient in ", (20, 128), Black, autoreset = False)
    p2line3 = DynamicText(smalltext,"my preferred language of python.", (20, 158), Black, autoreset = False)
    p2line4 = DynamicText(smalltext, "BASH naturally lends itself to file", (20, 188),Black, autoreset = False)
    p2line5 = DynamicText(smalltext, "handling, and will reduce the amount of time wasted ", (20, 218),Black, autoreset = False)
    p2line6 = DynamicText(smalltext, "manually  editing text files. ", (20, 248),Black, autoreset = False)
    p2line7 = DynamicText(smalltext,  "Simple scripts utilising for and if loops can be", (20, 308),Black, autoreset = False,)
    p2line8 = DynamicText(smalltext, " built to reduce manual file handling tasks.", (20, 338),Black, autoreset = False)
    p2line9 = DynamicText(smalltext, "Head to the bath for more information on GIT ", (20, 408),Black, autoreset = False)

    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                
        
        gameDisplay.fill(White)
        render_map(gameDisplay)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(book, (570, -100))
        gameDisplay.blit(pencil, (-150, 400))
        if page ==1:
            p1line1.draw(gameDisplay)
            p1line1.update()
            p1line2.draw(gameDisplay)
            p1line2.update()
            p1line3.draw(gameDisplay)
            p1line3.update()
            p1line4.draw(gameDisplay)
            p1line4.update()
            p1line5.draw(gameDisplay)
            p1line5.update()
            p1line6.draw(gameDisplay)
            p1line6.update()
            p1line7.draw(gameDisplay)
            p1line7.update()
            p1line8.draw(gameDisplay)
            p1line8.update()
            p1line9.draw(gameDisplay)
            p1line9.update()
            p1line10.draw(gameDisplay)
            p1line10.update()
    

            nextpage("Next page", display_width/1.2, 550, 100, 50, Brown, Bright_green, initial_x, initial_y, 7)
        elif page==2:
            p2line1.draw(gameDisplay)
            p2line1.update()
            p2line2.draw(gameDisplay)
            p2line2.update()
            p2line3.draw(gameDisplay)
            p2line3.update()
            p2line4.draw(gameDisplay)
            p2line4.update()
            p2line5.draw(gameDisplay)
            p2line5.update()
            p2line6.draw(gameDisplay)
            p2line6.update()
            p2line7.draw(gameDisplay)
            p2line7.update()
            p2line8.draw(gameDisplay)
            p2line8.update()
            p2line9.draw(gameDisplay)
            p2line9.update()

            return_button("Return to game", display_width/1.2, 500, 100, 50, Brown, Bright_green, initial_x, initial_y, 0)
   
        pygame.display.update()
        clock.tick(55)

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
                    window(x,y, 1)
                else:
                    pass
                
             #Book 6.5, 6.7, 0, 50, 50
                if keys[pygame.K_x] and 6.6*SCALE+50 > x > 183 and 6.7*SCALE < y < 6.7*SCALE+50:
                    map.clear()
                    book(x,y, 1)
                else:
                    pass
            
            #Globe
                if keys[pygame.K_x] and 296 > x > 248 and 548 < y < 600:
                    map.clear()
                    globe(x,y, 1)
                else:
                    pass
             
             #KITCHEN ----------
             #Pool  10, 14.2, 0, 117, 92       9, 15.2, 0, 117, 92
                if keys[pygame.K_x] and 425 > x > 9*SCALE and 467 < y < 15.2*SCALE+92:
                    map.clear()
                    pool(x, y, 1)
                else:
                    pass
             
             #BEDROOM ---------- DONE
             #computer  22.8, 0.3, 0, 40, 65
                if keys[pygame.K_x] and x > 22.8*SCALE and y < 0.31*SCALE+65:
                    map.clear()
                    computer(x, y, 1)
                else:
                    pass
            #desk
                if keys[pygame.K_x] and 532 > x > 460 and 99< y < 204:
                    map.clear()
                    desk(x, y, 1)
                else:
                    pass
                
            #BATHROOM ---------- DONE
            #Bath 18.3, 16.7, 0, 35, 50       20.8, 16.7, 0, 35, 50)
                if keys[pygame.K_x] and 765 > x > 20.5*SCALE and 505 < y < 16.5*SCALE+50:
                    map.clear()
                    bath(x,y, 1)
                else:
                    pass
            #Mirror 18.2, 13.3, 0, 34, 54
                if keys[pygame.K_x] and 18.2*SCALE+34 > x > 18.2*SCALE and 13.3*SCALE < y < 13.3*SCALE+54:
                    map.clear()
                    mirror(x,y, 1)
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

        hero.render(gameDisplay)
        my_group.update()
        my_group.draw(gameDisplay)
        hero.update_position((x, y))
        
        
        
        pygame.display.update()
        clock.tick(50)
        

pygame.QUIT
game_intro(1)
# if __name__ == "__main__":
    # main(100)