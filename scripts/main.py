""" Creating a room that I can move around in. Also needs files CONFIG"""
try:
    import sys
    import random
    import math
    import os
    import random
    import getopt
    import pygame
    import time
    import CONFIG
    import itertools
    import math
    import numpy as np
    from socket import *
    from pygame.locals import *
except ImportError:
    print("couldn't load module. %s" % (err))
    sys.exit(2)
    
pygame.init()
#print(pygame.font.get_fonts())
pygame.mixer.music.load("../data/jazz.mp3")
# display_width = 640 
# display_height = 480   
display_width = 800 
display_height = 640   
gameDisplay=pygame.display.set_mode((display_width, display_height))  
pygame.display.set_caption('Explore the house to discover some science')
map = []
camera=[0,0]
map_tile_image = {
    "G" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_97.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "L" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_376.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "R" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_378.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "T" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_350.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "B" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_404.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "C" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_349.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "D" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_351.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "E" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_403.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    "F" : pygame.transform.scale(pygame.image.load("../data/flooring/tile_405.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    #bathroom floor
    "X" : pygame.transform.scale(pygame.image.load("../data/flooring/bathroom_floor.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    #bedroom floor
    "K" : pygame.transform.scale(pygame.image.load("../data/flooring/bedroom_floor.png"), ((CONFIG.SCALE, CONFIG.SCALE))),
    #lounge floor
    "Z" : pygame.transform.scale(pygame.image.load("../data/flooring/lounge_floor.png"), ((CONFIG.SCALE, CONFIG.SCALE)))
}


#resources------ Here we place static game components, imagery etc.

def text_objects(text, font):
    textSurface=font.render(text, True, CONFIG.Black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,inactive, active, action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 0:
                main()
            elif action == 1:
                pygame.quit()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, w, h))
            
    smallText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2), y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    
def game_intro():
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
        # background = pygame.transform.scale(image, (display_width, display_height))
        # background = background.convert()
        # gameDisplay.blit(background, (0, 0))
        #gameDisplay.fill("../data/topdown-shooter/PNG/Tiles/tile73.png")
        largeText=pygame.font.Font('../data/fonts/Eight-Bit_Madness.ttf', 80)
        largeText2=pygame.font.SysFont ("bitstreamverasans", 30)
        text2=largeText2.render("Lockdown Edition", True, CONFIG.Yellow)
        text3=largeText2.render("A programme completely compiled in BASH", True, CONFIG.White)
        
        text2 = pygame.transform.rotate(text2, -30)
        TextSurf, TextRect = text_objects("The Advanced ", largeText)
        TextSurf2, TextRect2 = text_objects("Scripting Workshop", largeText)
        TextRect.center = (display_width/2, display_height/3)
        TextRect2.center = (display_width/2, display_height/3+40)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(text2, (display_width*0.7, display_height/7))
        gameDisplay.blit(text3, (display_width*0.1, display_height/1.2))
        
        button("Enter!", display_width/2-150, 300, 200, 100, CONFIG.Brown, CONFIG.Bright_green, 0)
        button("Quit!", display_width/2, 400, 200, 100, CONFIG.Brown, CONFIG.Bright_red, 1)
        
        pygame.display.update()
        clock.tick(15)

def render_map(screen, hero):
        # determine_camera(hero)
        y_pos = 0
        for line in map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos*CONFIG.SCALE, y_pos*CONFIG.SCALE, CONFIG.SCALE,CONFIG.SCALE)
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
            
# def determine_camera(hero):
#         max_y_position = len(map) - display_height/ CONFIG.SCALE
#         y_position = (hero.position[1]/ CONFIG.SCALE) - math.ceil(round((display_height/ CONFIG.SCALE) / 2))
#         if y_position <= max_y_position and y_position >= 0:
#             camera[1] = hero.position[1]/ CONFIG.SCALE
#         elif y_position < 0:
#             camera[1] = 0
#         else:
#             camera[1] = max_y_position
       
#         print('Camera is '+str(camera[1]))
#         print('hero is '+str(hero.position[1]/CONFIG.SCALE))
        
class Hero:
    def __init__(self, x_pos, y_pos):
        self.position = [x_pos, y_pos]
        self.image = pygame.image.load("../data/images/player.png")
        self.image = pygame.transform.scale(self.image, (CONFIG.SCALE, CONFIG.SCALE))
        self.rect = pygame.Rect(self.position[0], self.position[1], CONFIG.SCALE, CONFIG.SCALE)
    
    
    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]


    def render(self, screen, camera):
        #self.rect = pygame.Rect(self.position[0]*CONFIG.SCALE, self.position[1]*CONFIG.SCALE-(camera[1]*CONFIG.SCALE),CONFIG.SCALE, CONFIG.SCALE)
        self.rect = pygame.Rect((self.position[0]), (self.position[1]),CONFIG.SCALE, CONFIG.SCALE)
        screen.blit(self.image, self.rect)
        print(self.rect)
        
        
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
        self.rect = pygame.Rect(17*CONFIG.SCALE, 15*CONFIG.SCALE, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        timescale=10
        self.index += 1
        if int(self.index/timescale) >= len(self.images):
            self.index = 0
        print(int(self.index/timescale))
        self.image = self.images[int(self.index/timescale)]
        
        
def furniture(file, tilex, tiley, rotation, scalea, scaleb):
    """load furniture into a specific area"""
    image = pygame.image.load("../data/"+str(file))
    x=tilex*CONFIG.SCALE
    y=tiley*CONFIG.SCALE
    image = pygame.transform.scale(image, (scalea, scaleb))
    image = pygame.transform.rotate(image, rotation)
    rect = pygame.Rect(x, y, scalea, scaleb)
    gameDisplay.blit(image, rect)
           

clock = pygame.time.Clock()
def main():
    camera=[0,0]
    #where to place car
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0 
    y_change = 0
    load_map("myfile")
    gameExit = False
    hero = Hero(100, 100)
    # print(len(map))
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)
    
    
    
    while not gameExit: #GAME LOOP
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:

                
                keys=pygame.key.get_pressed()    
                if keys[pygame.K_LEFT]:
                    x_change=-5
                elif keys[pygame.K_RIGHT]:
                    x_change=5
                elif keys[pygame.K_UP]:
                    y_change=-5
                elif keys[pygame.K_DOWN]:
                    y_change=5
                else:
                    x_change=0 
                    y_change=0
        
        # print(int((x+x_change)/CONFIG.SCALE))
        # print(int((y+y_change)/CONFIG.SCALE))
        if int((x+x_change)) < 0 or int((x+x_change)) > (display_width -1-CONFIG.SCALE):
            x_change=0
    

        if int((y+y_change)) < 0 or int((y+y_change)) > (display_height -5-CONFIG.SCALE):
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
        gameDisplay.fill(CONFIG.Black)
        render_map(gameDisplay, hero)
        
        
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
        furniture("../data/images/lounge/chair.png", 12.2, 3, 2, 33, 30)
        
        
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
        #bathroom
        furniture("../data/images/walls/Mytile_1.png", 15, 13, 0, 10, 70)
        furniture("../data/images/walls/Mytile_1.png", 15, 15, 0, 10, 90)
        furniture("../data/images/walls/Mytile_1.png", 15, 16.2, 0, 10, 90)
        
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
        
        furniture("../data/images/walls/Mytile_1.png", 15, 21, 0, 10, 70)
        
        # ---------  BATHROOM  ------------
        #toilet
        furniture("../data/images/bathroom/toilet.png", 20, 13.2, 0, 23, 52)
        #sink
        furniture("../data/images/bathroom/sink.png", 15.5, 13.2, 0, 62, 54)
        #bathmat
        furniture("../data/images/bathroom/bathmat.png", 18.3, 16.7, 0, 35, 50)
        #mirror
        furniture("../data/images/bathroom/bathroom_mirror.png", 18.2, 13.3, 0, 34, 54)
        
        
        # ---------  KITCHEN  ------------
        #ISLAND
        furniture("../data/images/kitchen/kitchen_island.png", 4, 15.5, 0, 65, 96)
        #side
        furniture("../data/images/kitchen/kitchen_side.png", 1, 15.5, 0, 26, 90)
        furniture("../data/images/kitchen/kitchen_side.png", 1, 18.2, 90, 26, 90)
        #pool table
        furniture("../data/images/kitchen/pool_table.png", 10, 14.2, 0, 117, 92)
        #balls
        furniture("../data/images/kitchen/balls.png", 11, 14.9, 0, 40, 35)
        #cueues
        furniture("../data/images/kitchen/cueues.png", 13.5, 12.5, 0, 24, 65)
        
        
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_153.png", 18.5, 9,     180, 60, 30)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_177.png", 19.5, 9,     90,  30, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_152.png", 20.5, 9,     180, 60, 30)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_152.png", 18.5, 9.55,  0,   60, 30)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_177.png", 19.5, 9.55,  -90, 30, 60)
        # furniture("../data/topdown-shooter/PNG/Tiles/tile_153.png", 20.5, 9.55,  0,   60, 30)
        
        
        
        hero.render(gameDisplay, camera)
        my_group.update()
        my_group.draw(gameDisplay)
        hero.update_position((x, y))
        
        
        
        pygame.display.update()
        clock.tick(50)
        

pygame.QUIT
game_intro()
if __name__ == "__main__":
    main()