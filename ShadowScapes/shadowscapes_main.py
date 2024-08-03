from sysconfig import get_makefile_filename
import pygame
import spritesheet
import os
import math
import sys
from button import Button
from HealthBar import healthbar
from allVars import *
from allSprites import *
from allLoadedAssets import *
from allTransformed import *
from shadows_create import *


pygame.init()

width=720
height=480
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)
clock=pygame.time.Clock()
running=True

pygame.display.set_caption('Shadow Scapes')

health_bar=healthbar(22,38,187,36,player_health)

gamestate = -1


music=pygame.mixer.music.load("pygameAssests\main.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-2)


def get_title_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("pygameAssests\TitleFont.ttf", size)

def get_body_font(size):
    return pygame.font.Font("pygameAssests\FontBody1.otf", size)
MENU_MOUSE_POS = pygame.mouse.get_pos()
PLAY_MOUSE_POS = pygame.mouse.get_pos()
PLAY_BUTTON = Button(image=pygame.image.load("pygameAssests\Box1P.png"), pos=(360,160), 
                    text_input="PLAY", font=get_body_font(60), base_color="black", hovering_color="dark blue")
CREDITS_BUTTON = Button(image=pygame.image.load("pygameAssests\Box1.png"), pos=(360,310), 
                    text_input="CREDITS", font=get_body_font(36), base_color="black", hovering_color="dark blue")
QUIT_BUTTON = Button(image=pygame.image.load("pygameAssests\Box2.png"), pos=(360,420), 
                    text_input="QUIT", font=get_body_font(36), base_color="black", hovering_color="dark blue")

iworld = 0
worldtrans = get_title_font(60).render("NEXT WORLD!", True, "White")
wttext_rect = worldtrans.get_rect()
wttext_rect.center = (width//2,100)
w2r1 = pygame.Vector2(450,289)
w2r2 = pygame.Vector2(720+480, 289)
w2r3 = pygame.Vector2(1440+200, 289)
w1r1 = pygame.Vector2(600,283)
w1r2 = pygame.Vector2(2880+360, 283)

while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if (gamestate==-1):
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_title_font(60).render("Shadow Scapes", True, "RED")
        MENU_RECT = MENU_TEXT.get_rect(center=(360,40))
        #size of rect (362,158)
        PLAY_BUTTON = Button(image=pygame.image.load("pygameAssests\Box1P.png"), pos=(360,160), 
                            text_input="PLAY", font=get_body_font(60), base_color="black", hovering_color="dark blue")
        CREDITS_BUTTON = Button(image=pygame.image.load("pygameAssests\Box1.png"), pos=(360,310), 
                            text_input="CREDITS", font=get_body_font(36), base_color="black", hovering_color="dark blue")
        QUIT_BUTTON = Button(image=pygame.image.load("pygameAssests\Box2.png"), pos=(360,420), 
                            text_input="QUIT", font=get_body_font(36), base_color="black", hovering_color="dark blue")
                
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gamestate = -0.25
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gamestate = -0.5
                if (QUIT_BUTTON.checkForInput(MENU_MOUSE_POS)):
                    pygame.quit()
                    sys.exit()
    if (gamestate == -0.25):
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(opBg,(0,0))

        PLAY_TEXT = get_title_font(48).render("Choose Difficulty", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(360,40))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        EASY_BUTTON = Button(image=pygame.image.load("pygameAssests\levelbutton.png"), pos=(360,115), 
                            text_input="EASY", font=get_title_font(36), base_color="White", hovering_color="Black")
        NORMAL_BUTTON = Button(image=pygame.image.load("pygameAssests\levelbutton.png"), pos=(360,225), 
                            text_input="NORMAL", font=get_title_font(36), base_color="White", hovering_color="Black")
        HARD_BUTTON = Button(image=pygame.image.load("pygameAssests\levelbutton.png"), pos=(360,335), 
                            text_input="HARD", font=get_title_font(36), base_color="White", hovering_color="Black")
        PLAY_BACK = Button(image=pygame.image.load("pygameAssests\Box2.png"), pos=(360,420), 
                            text_input="BACK", font=get_title_font(36), base_color="White", hovering_color="Green")
        EASY_BUTTON.changeColor(PLAY_MOUSE_POS)
        EASY_BUTTON.update(screen)
        NORMAL_BUTTON.changeColor(PLAY_MOUSE_POS)
        NORMAL_BUTTON.update(screen)
        HARD_BUTTON.changeColor(PLAY_MOUSE_POS)
        HARD_BUTTON.update(screen)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    gamestate = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    diff = 3
                    gamestate = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NORMAL_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    diff = 2
                    gamestate = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    diff = 1
                    gamestate = 0
    if (gamestate == -0.5):
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(opBg, (0,0))
        CREDITS_TEXT = get_title_font(60).render("CREDITS", True, "White")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(360,50))
        CREDITS_DETAILS1 = get_body_font(20).render("craftpix.net",True,"White")
        CREDITS_DETAILS1_RECT = CREDITS_DETAILS1.get_rect(center=(360,155))
        CREDITS_DETAILS2 = get_body_font(20).render("Open Source Assets:",True,"White")
        CREDITS_DETAILS2_RECT = CREDITS_DETAILS2.get_rect(center=(360,130))
        CREDITS_DETAILS3 = get_body_font(35).render("Developers:",True,"White")
        CREDITS_DETAILS3_RECT = CREDITS_DETAILS3.get_rect(center=(360,210))
        CREDITS_DETAILS4 = get_body_font(25).render("Areen   Ramesh   Patil",True,"White")
        CREDITS_DETAILS4_RECT = CREDITS_DETAILS4.get_rect(center=(360,240))
        CREDITS_DETAILS5 = get_body_font(25).render("Ramya   Parsania",True,"White")
        CREDITS_DETAILS5_RECT = CREDITS_DETAILS5.get_rect(center=(360,270))
        CREDITS_DETAILS6 = get_body_font(25).render("Krishna   Sai",True,"White")
        CREDITS_DETAILS6_RECT = CREDITS_DETAILS6.get_rect(center=(360,300))
        CREDITS_DETAILS7 = get_body_font(40).render("Special  Thanks:  ZENSE",True,"White")
        CREDITS_DETAILS7_RECT = CREDITS_DETAILS7.get_rect(center=(360,330))
        screen.blit(CREDITS_TEXT, CREDITS_RECT)
        screen.blit(CREDITS_DETAILS1, CREDITS_DETAILS1_RECT)
        screen.blit(CREDITS_DETAILS2, CREDITS_DETAILS2_RECT)
        screen.blit(CREDITS_DETAILS3, CREDITS_DETAILS3_RECT)
        screen.blit(CREDITS_DETAILS4, CREDITS_DETAILS4_RECT)
        screen.blit(CREDITS_DETAILS5, CREDITS_DETAILS5_RECT)
        screen.blit(CREDITS_DETAILS6, CREDITS_DETAILS6_RECT)
        screen.blit(CREDITS_DETAILS7, CREDITS_DETAILS7_RECT)
        CREDITS_BACK = Button(image=pygame.image.load("pygameAssests\Box2.png"), pos=(360,420), 
                            text_input="BACK", font=get_title_font(36), base_color="White", hovering_color="Green")
        CREDITS_BACK.changeColor(OPTIONS_MOUSE_POS)
        CREDITS_BACK.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    gamestate = -1
    z=0
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if (gamestate==0):
        pygame.display.set_caption('World-1')
        screen.blit(battle2T_j1, (world1,0)) #jumping 1
        screen.blit(battle2T, (width+world1,0)) #enemy num 1
        screen.blit(battle2T, ((width*2)+world1, 0)) #enemy num 2
        screen.blit(battle2T_1, ((width*3)+world1, 0)) #shadow
        screen.blit(battle2T_b1, ((width*4)+world1, 0)) #big rock
        screen.blit(battle2T_j2, ((width*5)+world1, 0)) #jumping 2
        screen.blit(battle2T, ((width*6)+world1, 0)) #enemy num 3
        screen.blit(battle2T, ((width*7)+world1, 0))
        battle2T.blit(ruinb2_1T, (327,104))
        battle2T_1.blit(ruinb2_1T, (327,104))
        pygame.draw.polygon(battle2T_1, (0,0,0), shadows_w2) #459
        screen.blit(jumprock1_T, (w1r1.x, w1r1.y))
        screen.blit(jumprock1_T, (w1r2.x, w1r2.y))
        screen.blit(bigrock1, (w1b1.x, w1b1.y))
        #co-ords for enemies: 1130,240 ; 3960,240 ; 4520,240 : : for big rock: (3080,-300)
        if ((shadows_w2[0][0] + world1 > -2421) and (shadows_w2[0][0] + world1 < -1701) and (keys[pygame.K_DOWN])):
            sw1z = 1
            gamestate+=0.5
        if (world1==-4680):
            gamestate+=0.75
    if ((gamestate==0.5) or (sw1z==1)):
        pygame.display.set_caption('Shadow World')
        enemy3_alive = False
        variable= 4 
        checker = 1
        screen.blit(shadow_worldT, (sworld1,0))
        screen.blit(shadow_worldT, (width+sworld1,0))
        
        if (sworld1==-width):
            sw1z = 0
            gamestate = 0
    if (gamestate==0.75):
        pygame.display.set_caption('Next World!')
        screen.blit(interm_screenT, (iworld,0))
        screen.blit(interm_screenT, (width+iworld,0))
        screen.blit(worldtrans, wttext_rect)
        iworld-=15
        if (iworld==-width*0.75):
            iworld = 0
            gamestate = 1
    if (gamestate==1):
        pygame.display.set_caption('World-2')
        screen.blit(battle1T, (world2,0))
        screen.blit(battle1T, (width+world2,0))
        screen.blit(battle1T, ((width*2)+world2,0))
        screen.blit(battle1T_1, ((width*3)+world2,0))
        screen.blit(battle1T, ((width*4)+world2,0))
        screen.blit(battle1T, ((width*5)+world2,0))
        screen.blit(battle1T, ((width*6)+world2,0))
        screen.blit(battle1T, ((width*7)+world2,0))
        battle1T_1.blit(fernT, (205,130))
        pygame.draw.polygon(battle1T_1, (0,0,0), shadows_w1)
        battle1T_1.blit(smFernT, (347,176))
        screen.blit(w2rock_T, (w2r1.x, w2r1.y))
        screen.blit(w2rock_T, (w2r2.x, w2r2.y))
        screen.blit(w2rock_T, (w2r3.x, w2r3.y))
        if ((shadows_w1[0][0] + world2 > -2316) and (shadows_w1[0][0] + world2 < -1596) and (keys[pygame.K_DOWN])):
            sw2z = 1
            gamestate+=0.5
        if (world2<-5040):
            gamestate = 1.75
            
    if ((gamestate==1.5) or (sw2z==1)):
        pygame.display.set_caption('Shadow World')
        enemy5_alive=False
        variable = 6
        checker = 1
        screen.blit(shadow_worldT, (sworld2,0))
        screen.blit(shadow_worldT, (width+sworld2,0))
        
        if (sworld2 in range (-width-100,-width+100)):
            sw2z = 0
            gamestate = 1
    
    if (gamestate==1.75):
        pygame.display.set_caption('Next World!')
        screen.blit(interm_screenT, (iworld,0))
        screen.blit(interm_screenT, (width+iworld,0))
        screen.blit(worldtrans, wttext_rect)
        iworld-=15
        if (iworld==-width*0.75):
            iworld = 0
            gamestate = 2
    if (gamestate==2):
        pygame.display.set_caption('World-3')
        screen.blit(battle3T, (world3,0))
        screen.blit(battle3T, (width+world3,0))
        screen.blit(battle3T, ((width*2)+world3, 0))
        screen.blit(battle3T_1, ((width*3)+world3, 0))
        screen.blit(battle3T, ((width*4)+world3, 0))
        screen.blit(battle3T, ((width*5)+world3, 0))
        screen.blit(battle3T, ((width*6)+world3, 0))
        screen.blit(battle3T, ((width*7)+world3, 0))
        battle3T_1.blit(ruin2_1, (404,203))
        battle3T_1.blit(ruin1_1, (42,188))
        pygame.draw.polygon(battle3T_1, (0,0,0), shadows_w3_r2)
        pygame.draw.polygon(battle3T_1, (0,0,0), shadows_w3_r1)
        if (((shadows_w3_r1[0][0] + world3 > -2310)and(shadows_w3_r1[0][0] + world3 < -1590)) and ((shadows_w3_r2[0][0] + world3 > -2352)and(shadows_w3_r1[0][0] + world3 < -1632)) and (keys[pygame.K_DOWN])): 
            sw3z = 1
            gamestate+=0.5
        if (world3<-4320):
            gamestate = 2.75

    if ((gamestate==2.5) or (sw3z==1)):
        pygame.display.set_caption('Shadow World')
        enemy10_alive = False
        enemy11_alive = False
        variable = 12
        checker = 1
        screen.blit(shadow_worldT, (sworld3,0))
        screen.blit(shadow_worldT, (width+sworld3,0))
        
        if (sworld3==-width):
            sw3z = 0
            gamestate = 2

    if (gamestate==2.75):
        pygame.display.set_caption('Next World!')
        screen.blit(interm_screenT, (iworld,0))
        screen.blit(interm_screenT, (width+iworld,0))
        screen.blit(worldtrans, wttext_rect)
        iworld-=15
        if (iworld==-width*0.75):
            iworld = 0
            gamestate = 3

    if (gamestate==3):
        pygame.display.set_caption('World-4')
        screen.blit(battle4T, (world4,0))
        screen.blit(battle4T, (width+world4,0))
        screen.blit(battle4T, ((width*2)+world4, 0))
        screen.blit(battle4T_1, ((width*3)+world4, 0))
        screen.blit(battle4T, ((width*4)+world4, 0))
        screen.blit(battle4T, ((width*5)+world4, 0))
        screen.blit(battle4T, ((width*6)+world4, 0))
        screen.blit(battle4T, ((width*7)+world4, 0))
        battle4T_1.blit(sruin1_T, (404,150))
        pygame.draw.polygon(battle4T_1, (0,0,0), shadows_w4)
        if ((shadows_w4[0][0] + world4 > -2542) and (shadows_w4[0][0] + world4 < -1822) and (keys[pygame.K_DOWN])):
            sw4z = 1
            gamestate+=0.5
        if (world4<=-4680):
            gamestate = 3.75
    
    if ((gamestate==3.5) or (sw4z==1)):
        pygame.display.set_caption('Shadow World')
        enemy15_alive = False
        variable = 16
        checker = 1
        screen.blit(shadow_worldT, (sworld4,0))
        screen.blit(shadow_worldT, (width+sworld4,0))
        
        if (sworld4==-width):
            sw4z = 0
            gamestate = 3
    
    if (gamestate==3.75):
        pygame.display.set_caption('Off To the Final Battle!')
        screen.blit(interm_screenT, (iworld,0))
        screen.blit(interm_screenT, (width+iworld,0))
        screen.blit(worldtrans, wttext_rect)
        iworld-=15
        if (iworld==-width*0.75):
            iworld = 0
            gamestate = 4
    

    clock.tick(900)
    dt=clock.tick(25)
    time=time+clock.tick(120)


    if (keys[pygame.K_RIGHT]):
        if ((gamestate==0)):
            
            if ((w1r1.x-player_x!=70) and (w1r2.x-player_x!=70)):
                world1-=10
                w1r1.x-=10
                w1r2.x-=10
            if (((w1r1.x-player_x==70) or (w1r2.x-player_x==70)) and (player_y<210)):
                world1-=10
                w1r1.x-=10
                w1r2.x-=10
            if (((w1r1.x-player_x==70) or (w1r2.x-player_x==70))):
                player_health-=2//diff
        if (gamestate==0.5):
            sworld1-=10
            world1-=15
        if ((gamestate==1)):
            if ((w2r1.x-player_x!=40) and (w2r2.x-player_x!=50) and (w2r3.x-player_x!=70)):
                world2-=10
                w2r1.x-=10
                w2r2.x-=10
                w2r3.x-=10
            if (((w2r1.x-player_x==40) or (w2r2.x-player_x==50) or (w2r3.x-player_x==70)) and (player_y<210)):
                world2-=10
                w2r1.x-=10
                w2r2.x-=10
                w2r3.x-=10
            if ((w2r1.x-player_x==70) or (w2r2.x-player_x==70) or (w2r3.x-player_x==70)):
                player_health-=2//diff
        if (gamestate==1.5):
            enemy5_alive = False
            sworld2-=10
            world2-=15
        if (gamestate==2):
            if (world3 not in [-100,-(720+100),-(1440+100),-(2160+100),-(2880+100),-(3600+100),-(4320+100)]):
                world3-=10
            if ((world3 in [-100,-(720+100),-(1440+100),-(2160+100),-(2880+100),-(3600+100),-(4320+100)]) and (player_y<210)):
                world3-=10
            if ((world3 in [-100,-(720+100),-(1440+100),-(2160+100),-(2880+100),-(3600+100),-(4320+100)])):
                player_health-=2//diff
        if (gamestate==2.5):
            sworld3-=10
            world3-=15
        if (gamestate==3):
            if (world4 not in [-120,-(720+120),-(1440+120),-(2160+120),-(2880+120),-(3600+120),-(4320+120)]):
                world4-=10
            if ((world4 in [-120,-(720+120),-(1440+120),-(2160+120),-(2880+120),-(3600+120),-(4320+120)]) and (player_y<210)):
                world4-=10
            if (world4 in [-120,-(720+120),-(1440+120),-(2160+120),-(2880+120),-(3600+120),-(4320+120)]):
                player_health-=2//diff
        if (gamestate==3.5):
            sworld4-=10
            world4-=15

    if(gamestate<4) and (gamestate>=0):
        if player_y < 210:
            z=1
            screen.blit(jump[1],(player_x,player_y))  # You can adjust this value to control gravity strength
            player_y_velocity += 2
        else:
            player_y_velocity = 0  # Reset velocity when on the ground
            player_y = 210 
    
    if keys[pygame.K_UP] and player_y == 210 and gamestate<4 and (gamestate>=0):  # Check if player is on the ground
        screen.blit(jump[0], (player_x, player_y))
        player_y_velocity = -18
    
    elif keys[pygame.K_RIGHT] and z==0 and gamestate<4 and (gamestate>=0): 
        index = (index + 1) % len(run)
        time = 0
        screen.blit(run[index], (player_x, player_y))

    
    elif (player_y<210) and gamestate<4 and (gamestate>=0):
        player_y+=z
    
    elif keys[pygame.K_x] and z==0 and gamestate<4 and (gamestate>=0):
        ##dt=clock.tick(50)
        index = (index+1) % len(attack)
        time=0
        screen.blit(attack[index],(player_x,player_y))
        if(enemy1_alive==True and enemy1_x in range(player_x,player_x+63)):
            enemy1_health-=10
        if(enemy2_alive==True and  enemy2_x in range(player_x,player_x+63)):
            enemy2_health-=10
        if(enemy3_alive==True and  enemy3_x in range(player_x,player_x+63)):
            enemy3_health-=10
        if(enemy4_alive==True and  enemy4_x in range(player_x,player_x+63)):
            enemy4_health-=10
        if(enemy5_alive==True and  enemy5_x in range(player_x,player_x+63)):
            enemy5_health-=10
        if(enemy6_alive==True and  enemy6_x in range(player_x,player_x+63)):
            enemy6_health-=10
        if(enemy7_alive==True and  enemy7_x in range(player_x,player_x+63)):
            enemy7_health-=10
        if(enemy8_alive==True and  enemy8_x in range(player_x,player_x+63)):
            enemy8_health-=10
        if(enemy9_alive==True and  enemy9_x in range(player_x,player_x+63)):
            enemy9_health-=10
        if(enemy10_alive==True and  enemy10_x in range(player_x,player_x+63)):
            enemy10_health-=10
        if(enemy11_alive==True and  enemy11_x in range(player_x,player_x+63)):
            enemy11_health-=10
        if(enemy12_alive==True and  enemy12_x in range(player_x,player_x+63)):
            enemy12_health-=10
        if(enemy13_alive==True and  enemy13_x in range(player_x,player_x+63)):
            enemy13_health-=10
        if(enemy14_alive==True and  enemy14_x in range(player_x,player_x+63)):
            enemy14_health-=10
        if(enemy15_alive==True and  enemy15_x in range(player_x,player_x+63)):
            enemy15_health-=10
        if(enemy16_alive==True and  enemy16_x in range(player_x,player_x+63)):
            enemy16_health-=10

    elif  keys[pygame.K_k] and z==0 and gamestate<4 and (gamestate>=0): 
        #dt=clock.tick(50)
        index = (index+1) % len(kick)
        time=0
        screen.blit(kick[index],(player_x,player_y))
        if(enemy1_alive==True and enemy1_x in range(player_x,player_x+63)):
            enemy1_health-=10
        if(enemy2_alive==True and  enemy2_x in range(player_x,player_x+63)):
            enemy2_health-=10
        if(enemy3_alive==True and  enemy3_x in range(player_x,player_x+63)):
            enemy3_health-=10
        if(enemy4_alive==True and  enemy4_x in range(player_x,player_x+63)):
            enemy4_health-=10
        if(enemy5_alive==True and  enemy5_x in range(player_x,player_x+63)):
            enemy5_health-=10
        if(enemy6_alive==True and  enemy6_x in range(player_x,player_x+63)):
            enemy6_health-=10
        if(enemy7_alive==True and  enemy7_x in range(player_x,player_x+63)):
            enemy7_health-=10
        if(enemy8_alive==True and  enemy8_x in range(player_x,player_x+63)):
            enemy8_health-=10
        if(enemy9_alive==True and  enemy9_x in range(player_x,player_x+63)):
            enemy9_health-=10
        if(enemy10_alive==True and  enemy10_x in range(player_x,player_x+63)):
            enemy10_health-=10
        if(enemy11_alive==True and  enemy11_x in range(player_x,player_x+63)):
            enemy11_health-=10
        if(enemy12_alive==True and  enemy12_x in range(player_x,player_x+63)):
            enemy12_health-=10
        if(enemy13_alive==True and  enemy13_x in range(player_x,player_x+63)):
            enemy13_health-=10
        if(enemy14_alive==True and  enemy14_x in range(player_x,player_x+63)):
            enemy14_health-=10
        if(enemy15_alive==True and  enemy15_x in range(player_x,player_x+63)):
            enemy15_health-=10
        if(enemy16_alive==True and  enemy16_x in range(player_x,player_x+63)):
            enemy16_health-=10
        
    elif keys[pygame.K_d] and z==0 and gamestate<4 and (gamestate>=0):
        screen.blit(shield[1],(player_x,player_y))
    elif(z==0 and not(keys[pygame.K_k]) and not(keys[pygame.K_x]) and not(keys[pygame.K_RIGHT]) and not(keys[pygame.K_UP]) and gamestate!=4 and (gamestate>=0)):                       
        screen.blit(idle[0],(player_x,player_y))
    player_y += player_y_velocity
    
    
   
    if ((variable==1 and checker==1) and (gamestate==0)):
        enemy1_x=720+500 #orc
        enemy1_y=210
        checker=0
        enemy1_alive=True
        enemy1_health=250
    if ((variable==2 and checker==1) and (gamestate==0)):
        enemy2_x=720+500 #orc
        enemy2_y=210
        checker=0
        enemy2_alive=True
        enemy2_health=250
    if ((variable==3 and checker==1) and (gamestate==0)):
        enemy3_x=2880+600 #sword running
        enemy3_y=180
        checker=0
        enemy3_alive=True
        enemy3_health=250
    if ((variable==4 and checker==1) and (gamestate==1)):
        enemy4_x=2880+550 #orc
        enemy4_y=210
        checker=0
        enemy4_alive=True 
        enemy4_health=250
    if ((variable==5 and checker==1) and (gamestate==1)):
        enemy5_x=770+750
        enemy5_y=190 #mage
        checker=0
        enemy5_alive=True
        enemy5_health=250
    if ((variable==6 and checker==1) and (gamestate==1)):
        enemy6_x=1200
        enemy6_y=180 #running sword
        checker=0
        enemy6_alive=True
        enemy6_health=250
    if ((variable==7 and checker==1) and (gamestate==1)):
        enemy7_x=1200
        enemy7_y=210 #orc
        checker=0
        enemy7_alive=True
        enemy7_health=250
    if ((variable==8 and checker==1) and (gamestate==2)):
        enemy8_x=600
        enemy8_y=210 #orc
        checker=0
        enemy8_alive=True
        enemy8_health=250
    if ((variable==9 and checker==1) and (gamestate==2)):
        enemy9_x=770+600
        enemy9_y=180 #running sword
        checker=0
        enemy9_alive=True
        enemy9_health=250
    if ((variable==10 and checker==1) and (gamestate==2)):
        enemy10_x=2880
        enemy10_y=190 #mage
        checker=0
        enemy10_alive=True
        enemy10_health=250
    if ((variable==11 and checker==1) and (gamestate==2)):
        enemy11_x=1800
        enemy11_y=180 #running sword
        checker=0
        enemy11_alive=True
        enemy11_health=250
    if ((variable==12 and checker==1) and (gamestate==2)):
        enemy12_x=800
        enemy12_y=190 #mage
        checker=0
        enemy12_alive=True
        enemy12_health=250
    if ((variable==13 and checker==1) and (gamestate==3)):
        enemy13_x=1200
        enemy13_y=210 #orc
        checker=0
        enemy13_alive=True
        enemy13_health=250
    if ((variable==14 and checker==1) and (gamestate==3)):
        enemy14_x=2160
        enemy14_y=180 #running sword
        checker=0
        enemy14_alive=True
        enemy14_health=250
    if ((variable==15 and checker==1) and (gamestate==3)):
        enemy15_x=900
        enemy15_y=190 #mage
        checker=0
        enemy15_alive=True
        enemy15_health=250
    if ((variable==16 and checker==1) and (gamestate==3)):
        enemy16_x=1200
        enemy16_y=190 #mage
        checker=0
        enemy16_alive=True
        enemy16_health=250


    if ((variable==1 and checker==0) and (gamestate==0)):
        if(enemy1_x>player_x+55):
           
            #dt=clock.tick(50)
            index1=(index1+1)%len(e1run)
            time=0
            if(enemy1_alive==True):
                screen.blit(e1run[index1],(enemy1_x,enemy1_y))
                enemy1_x-=20
        else:
            #dt=clock.tick(50)
            index1=(index1+1)%len(enemy1_attack)
            time=0
            if(enemy1_alive==True):
                screen.blit(enemy1_attack[index1],(enemy1_x,enemy1_y))
                if(enemy1_x>player_x+55):
                    enemy1_x-=20
            if(enemy1_x in range(player_x, player_x+55)):
                player_health-=5//diff
            if(enemy1_health<=0):
                enemy1_alive=False
                variable=2
                checker=1
    if ((variable==2 and checker==0) and (gamestate==0)):
        if(enemy2_x>player_x+55):
            
            #dt=clock.tick(50)
            index1=(index1+1)%len(e1run)
            time=0
            if(enemy2_alive==True):
                screen.blit(e1run[index1],(enemy2_x,enemy2_y))
                enemy2_x-=20
        else:
            #dt=clock.tick(50)
            index1=(index1+1)%len(enemy1_attack)
            time=0
            if(enemy2_alive==True):
                screen.blit(enemy1_attack[index1],(enemy2_x,enemy2_y))
                if(enemy2_x>33+player_x):
                    enemy2_x-=20
            if(enemy2_x in range(player_x, player_x+60)):
                player_health-=5//diff
            if(enemy2_health<=0):
                enemy2_alive=False
                variable=3
                checker=1
    if ((variable==3 and checker==0) and (gamestate==0)):
        if(enemy3_x>player_x+55):
           
            index2_run=(index2_run+1)%len(erun)
            time=0
            if(enemy3_alive==True):
                screen.blit(erun[index2_run],(enemy3_x,enemy3_y))
                enemy3_x-=20
                
        else:
            #dt=clock.tick(50)
            index2_attack= (index2_attack+1)%len(eattack)
            time=0
            if(enemy3_alive==True):
                screen.blit(eattack[index2_attack],(enemy3_x,enemy3_y))
                if(enemy3_x>33+player_x):
                    enemy3_x-=20
            
            if(enemy3_x in range(player_x, player_x+55)):
                player_health-=5//diff
            if(enemy3_health<=0):
                enemy3_alive=False
                variable=4
                checker=1
    if ((variable==4 and checker==0) and (gamestate==1)):
        if(enemy4_x>player_x+55):
            
            #dt=clock.tick(50)
            index1=(index1+1)%len(e1run)
            time=0
            if(enemy4_alive==True):
                screen.blit(e1run[index1],(enemy4_x,enemy4_y))
                enemy4_x-=20
        else:
            #dt=clock.tick(50)
            index1=(index1+1)%len(enemy1_attack)
            time=0
            if(enemy4_alive==True):
                screen.blit(enemy1_attack[index1],(enemy4_x,enemy4_y))
                if(enemy4_x>33+player_x):
                    enemy4_x-=20
            if(enemy4_x in range(player_x,player_x+55)):
                player_health-=5//diff
            if(enemy4_health<=0):
                enemy4_alive=False
                variable=5
                checker=1
    if ((variable==5 and checker==0) and (gamestate==1)):
       
        if(enemy5_x>player_x+30):
            
            if(enemy5_alive==True):
                if(enemy5_x==720):
                    bullet1_state=True 
                    bullet1_x=enemy5_x
                    bullet1_y=enemy5_y+75
                if(enemy5_x==360):
                    bullet2_state=True 
                    bullet2_x=enemy5_x
                    bullet2_y=enemy5_y+75
                if(bullet1_state==True):
                    screen.blit(fireball1,(bullet1_x,bullet1_y))
                    bullet1_x-=30
                    if(bullet1_x in range(player_x ,player_x+20)  and (player_y==210)):
                        player_health-=10//diff
                        bullet1_state=False
                if(bullet2_state==True):
                    screen.blit(fireball2,(bullet2_x,bullet2_y))
                    bullet2_x-=30
                    if(bullet2_x in range(player_x-10,player_x+10)  and (player_y==210)):
                        player_health-=10//diff
                        bullet2_state=False 
                if(enemy5_x>=player_x+80 and enemy5_x<=player_x+105):
                    #dt=clock.tick(50)
                    index3=(index3+1)%len(erun)
                    time=0
                    screen.blit(erun[index3],(enemy5_x,enemy5_y))
                elif(enemy5_x>=player_x+50 and enemy5_x<=player_x+75):
                    #dt=clock.tick(50)
                    index_firethrow1=(index_firethrow1+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow1],(enemy5_x,enemy5_y))
                else:
                    #dt=clock.tick(50)
                    index_firethrow2=(index_firethrow2+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow2],(enemy5_x,enemy5_y))
                enemy5_x-=25
        if(enemy5_x<=player_x+55):
            #dt=clock.tick(50)
            index3=(index3+1)%len(flamejet)
            time=0
            if(enemy5_alive==True):
                screen.blit(flamejet[index3],(enemy5_x,enemy5_y))
            if(enemy5_x in range(player_x-50,player_x+50)):
                player_health-=5//diff
        
        if(enemy5_x<50):
            e3_flame_state=True
        if(enemy5_health<=0):
            enemy5_alive=False
            variable=6
            checker=1

    if ((variable==6 and checker==0) and (gamestate==1)):
        if(enemy6_x>player_x+60):
            
            index2_run=(index2_run+1)%len(erun)
            time=0
            if(enemy6_alive==True):
                screen.blit(erun[index2_run],(enemy6_x,enemy6_y))
                enemy6_x-=20
                
        else:
            #dt=clock.tick(50)
            index2_attack= (index2_attack+1)%len(eattack)
            time=0
            if(enemy6_alive==True):
                screen.blit(eattack[index2_attack],(enemy6_x,enemy6_y))
                if(enemy6_x>player_x+50):
                    enemy6_x-=20
            if(enemy6_x in range(player_x-50, player_x+50)):
                player_health-=5//diff
            if(enemy6_health<=0):
                enemy6_alive=False
                variable=7
                checker=1
    if ((variable==7 and checker==0) and (gamestate==1)):
        if(enemy7_x>player_x+50):
           
            #dt=clock.tick(50)
            index1=(index1+1)%len(e1run)
            time=0
            if(enemy7_alive==True):
                screen.blit(e1run[index1],(enemy7_x,enemy7_y))
                enemy7_x-=20
        else:
            #dt=clock.tick(50)
            index1=(index1+1)%len(enemy1_attack)
            time=0
            if(enemy7_alive==True):
                screen.blit(enemy1_attack[index1],(enemy7_x,enemy7_y))
                if(enemy7_x>33+player_x):
                    enemy7_x-=20
            if(enemy7_x in range(player_x-50,player_x+50)):
                player_health-=5//diff
            if(enemy7_health<=0):
                enemy7_alive=False
                variable=8
                checker=1
    if((variable==8 and checker==0) and (gamestate==2)):
        if(enemy8_x>player_x+60):
            
            #dt=clock.tick(50)
            index1=(index1+1)%len(e1run)
            time=0
            if(enemy8_alive==True):
                screen.blit(e1run[index1],(enemy8_x,enemy8_y))
                enemy8_x-=20
        else:
            #dt=clock.tick(50)
            index1=(index1+1)%len(enemy1_attack)
            time=0
            if(enemy8_alive==True):
                screen.blit(enemy1_attack[index1],(enemy8_x,enemy8_y))
                if(enemy8_x>50+player_x):
                    enemy8_x-=20
            if(enemy8_x in range(player_x,player_x+60)):
                player_health-=5//diff
            if(enemy8_health<=0):
                enemy8_alive=False
                variable=9
                checker=1
    if ((variable==9 and checker==0) and (gamestate==2)):
        if(enemy9_x>player_x+60):
            
            index2_run=(index2_run+1)%len(erun)
            time=0
            if(enemy9_alive==True):
                screen.blit(erun[index2_run],(enemy9_x,enemy9_y))
                enemy9_x-=20
                
        else:
            #dt=clock.tick(50)
            index2_attack= (index2_attack+1)%len(eattack)
            time=0
            if(enemy9_alive==True):
                screen.blit(eattack[index2_attack],(enemy9_x,enemy9_y))
                if(enemy9_x>player_x+50):
                    enemy9_x-=20
            
            if(enemy9_x in range(player_x, player_x+60)):
                player_health-=5//diff
            if(enemy9_health<=0):
                enemy9_alive=False
                variable=10
                checker=1
    if ((variable==10 and checker==0) and  (gamestate==2)):
        
        if(enemy10_x>player_x+30):
            
            if(enemy10_alive==True):
                if(enemy10_x==720):
                    bullet1_state=True 
                    bullet1_x=enemy10_x
                    bullet1_y=enemy10_y+75
                if(enemy10_x==360):
                    bullet2_state=True 
                    bullet2_x=enemy10_x
                    bullet2_y=enemy10_y+75
                if(bullet1_state==True):
                    screen.blit(fireball1,(bullet1_x,bullet1_y))
                    bullet1_x-=30
                    if(bullet1_x in range(player_x , player_x+60)  and (player_y==210)):
                        player_health-=10//diff
                        bullet1_state=False
                if(bullet2_state==True):
                    screen.blit(fireball2,(bullet2_x,bullet2_y))
                    bullet2_x-=30
                    if(bullet2_x in range(player_x,player_x+60)  and (player_y==210)):
                        player_health-=10//diff
                        bullet2_state=False 
                if(enemy10_x>=player_x+100 and enemy10_x<=player_x+125):
                    #dt=clock.tick(50)
                    index3=(index3+1)%len(erun)
                    time=0
                    screen.blit(erun[index3],(enemy10_x,enemy10_y))
                elif(enemy10_x>=player_x+70 and enemy10_x<=player_x+100):
                    #dt=clock.tick(50)
                    index_firethrow1=(index_firethrow1+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow1],(enemy10_x,enemy10_y))
                else:
                    #dt=clock.tick(50)
                    index_firethrow2=(index_firethrow2+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow2],(enemy10_x,enemy10_y))
                enemy10_x-=25
        if(enemy10_x<=player_x+60):
            #dt=clock.tick(50)
            index3=(index3+1)%len(flamejet)
            time=0
            if(enemy10_alive==True):
                screen.blit(flamejet[index3],(enemy10_x,enemy10_y))
            if(enemy10_x in range(player_x, player_x+60)):
                player_health-=5//diff
        
        if(enemy10_x<60):
            e3_flame_state=True
        if(enemy10_health<=0):
            enemy10_alive=False
            variable=11
            checker=1

    if ((variable==11 and checker==0) and (gamestate==2)):
        if(enemy11_x>player_x+60):
           
            index2_run=(index2_run+1)%len(erun)
            time=0
            if(enemy11_alive==True):
                screen.blit(erun[index2_run],(enemy11_x,enemy11_y))
                enemy11_x-=20
                
        else:
            #dt=clock.tick(50)
            index2_attack= (index2_attack+1)%len(eattack)
            time=0
            if(enemy11_alive==True):
                screen.blit(eattack[index2_attack],(enemy11_x,enemy11_y))
                if(enemy11_x>player_x+50):
                    enemy11_x-=20
            
            if(enemy11_x in range(player_x, player_x+60)):
                player_health-=5//diff
            if(enemy11_health<=0):
                enemy11_alive=False
                variable=12
                checker=1
    if ((variable==12 and checker==0) and (gamestate==2)):
        
        if(enemy12_x>player_x+60):
            
            if(enemy12_alive==True):
                if(enemy12_x==720):
                    bullet1_state=True 
                    bullet1_x=enemy12_x
                    bullet1_y=enemy12_y+75
                if(enemy12_x==360):
                    bullet2_state=True 
                    bullet2_x=enemy12_x
                    bullet2_y=enemy12_y+75
                if(bullet1_state==True):
                    screen.blit(fireball1,(bullet1_x,bullet1_y))
                    bullet1_x-=30
                    if(bullet1_x in range(player_x, player_x+60)  and (player_y==210)):
                        player_health-=10//diff
                        bullet1_state=False
                if(bullet2_state==True):
                    screen.blit(fireball2,(bullet2_x,bullet2_y))
                    bullet2_x-=30
                    if(bullet2_x in range(player_x, player_x+30)  and (player_y==210)):
                        player_health-=10//diff
                        bullet2_state=False 
                if(enemy12_x>=player_x+100 and enemy12_x<=player_x+125):
                    #dt=clock.tick(50)
                    index3=(index3+1)%len(erun)
                    time=0
                    screen.blit(erun[index3],(enemy12_x,enemy12_y))
                elif(enemy12_x>=player_x+70 and enemy12_x<=player_x+100):
                    #dt=clock.tick(50)
                    index_firethrow1=(index_firethrow1+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow1],(enemy12_x,enemy12_y))
                else:
                    #dt=clock.tick(50)
                    index_firethrow2=(index_firethrow2+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow2],(enemy12_x,enemy12_y))
                enemy12_x-=25
        if(enemy12_x<=player_x+60):
            #dt=clock.tick(50)
            index3=(index3+1)%len(flamejet)
            time=0
            if(enemy12_alive==True):
                screen.blit(flamejet[index3],(enemy12_x,enemy12_y))
            if(enemy12_x in range(player_x, player_x+60)):
                player_health-=5//diff
        
        if(enemy12_x<60):
            e3_flame_state=True
        if(enemy12_health<=0):
            enemy12_alive=False
            variable=13
            checker=1

    if((variable==13 and checker==0) and (gamestate==3)):
        if(enemy13_x>player_x+60):
           
            #dt=clock.tick(50)
            index1=(index1+1)%len(e1run)
            time=0
            if(enemy13_alive==True):
                screen.blit(e1run[index1],(enemy13_x,enemy13_y))
                enemy13_x-=30
        else:
            #dt=clock.tick(50)
            index1=(index1+1)%len(enemy1_attack)
            time=0
            if(enemy13_alive==True):
                screen.blit(enemy1_attack[index1],(enemy13_x,enemy13_y))
                if(enemy13_x>50+player_x):
                    enemy13_x-=20
            if(enemy13_x in range(player_x, player_x+60)):
                player_health-=5//diff
            if(enemy13_health<=0):
                enemy13_alive=False
                variable=14
                checker=1
    if ((variable==14 and checker==0) and (gamestate==3)):
        
        if(enemy14_x>player_x+60):
            
            index2_run=(index2_run+1)%len(erun)
            time=0
            if(enemy14_alive==True):
                screen.blit(erun[index2_run],(enemy14_x,enemy14_y))
                enemy14_x-=20
                
        else:
            #dt=clock.tick(50)
            index2_attack= (index2_attack+1)%len(eattack)
            time=0
            if(enemy14_alive==True):
                screen.blit(eattack[index2_attack],(enemy14_x,enemy14_y))
                if(enemy14_x>player_x+50):
                    enemy14_x-=20
            
            if(enemy14_x in range(player_x , player_x+60)):
                player_health-=5//diff
            if(enemy14_health<=0):
                enemy14_alive=False
                variable=15
                checker=1
    if ((variable==15 and checker==0) and (gamestate==3)):
       
        if(enemy15_x>player_x+60):
            
            if(enemy15_alive==True):
                if(enemy15_x==720):
                    bullet1_state=True 
                    bullet1_x=enemy15_x
                    bullet1_y=enemy15_y+75
                if(enemy15_x==360):
                    bullet2_state=True 
                    bullet2_x=enemy15_x
                    bullet2_y=enemy15_y+75
                if(bullet1_state==True):
                    screen.blit(fireball1,(bullet1_x,bullet1_y))
                    bullet1_x-=30
                    if(bullet1_x in range(player_x, player_x+60)  and (player_y==210)):
                        player_health-=10//diff
                        bullet1_state=False
                if(bullet2_state==True):
                    screen.blit(fireball2,(bullet2_x,bullet2_y))
                    bullet2_x-=30
                    if(bullet2_x in range(player_x, player_x+30)  and (player_y==210)):
                        player_health-=10//diff
                        bullet2_state=False 
                if(enemy15_x>=player_x+100 and enemy15_x<=player_x+125):
                    #dt=clock.tick(50)
                    index3=(index3+1)%len(erun)
                    time=0
                    screen.blit(erun[index3],(enemy15_x,enemy15_y))
                elif(enemy15_x>=player_x+70 and enemy15_x<=player_x+100):
                    #dt=clock.tick(50)
                    index_firethrow1=(index_firethrow1+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow1],(enemy15_x,enemy15_y))
                else:
                    #dt=clock.tick(50)
                    index_firethrow2=(index_firethrow2+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow2],(enemy15_x,enemy15_y))
                enemy15_x-=25
        if(enemy15_x<=player_x+60):
            #dt=clock.tick(50)
            index3=(index3+1)%len(flamejet)
            time=0
            if(enemy15_alive==True):
                screen.blit(flamejet[index3],(enemy15_x,enemy15_y))
            if(enemy15_x in range(player_x-50,player_x+50)):
                player_health-=5//diff
        
        if(enemy15_x<50):
            e3_flame_state=True
        if(enemy15_health<=0):
            enemy15_alive=False
            variable=16
            checker=1
            
    if ((variable==16 and checker==0) and (gamestate==3)):
        
        if(enemy16_x>player_x+60):
           
            if(enemy16_alive==True):
                if(enemy16_x==720):
                    bullet1_state=True 
                    bullet1_x=enemy16_x
                    bullet1_y=enemy16_y+75
                if(enemy16_x==360):
                    bullet2_state=True 
                    bullet2_x=enemy16_x
                    bullet2_y=enemy16_y+75
                if(bullet1_state==True):
                    screen.blit(fireball1,(bullet1_x,bullet1_y))
                    bullet1_x-=30
                    if(bullet1_x in range(player_x, player_x+60)  and (player_y==210)):
                        player_health-=10//diff
                        bullet1_state=False
                if(bullet2_state==True):
                    screen.blit(fireball2,(bullet2_x,bullet2_y))
                    bullet2_x-=30
                    if(bullet2_x in range(player_x, player_x+30)  and (player_y==210)):
                        player_health-=10//diff
                        bullet2_state=False 
                if(enemy16_x>=player_x+100 and enemy16_x<=player_x+125):
                    #dt=clock.tick(50)
                    index3=(index3+1)%len(erun)
                    time=0
                    screen.blit(erun[index3],(enemy16_x,enemy16_y))
                elif(enemy16_x>=player_x+70 and enemy16_x<=player_x+100):
                    #dt=clock.tick(50)
                    index_firethrow1=(index_firethrow1+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow1],(enemy16_x,enemy16_y))
                else:
                    #dt=clock.tick(50)
                    index_firethrow2=(index_firethrow2+1)%len(erun)
                    time=0
                    screen.blit(erun[index_firethrow2],(enemy16_x,enemy16_y))
                enemy16_x-=25
        if(enemy16_x<=player_x+60):
            #dt=clock.tick(50)
            index3=(index3+1)%len(flamejet)
            time=0
            if(enemy16_alive==True):
                screen.blit(flamejet[index3],(enemy16_x,enemy16_y))
            if(enemy16_x in range(player_x-50,player_x+50)):
                player_health-=5//diff
        
        if(enemy16_x<50):
            e3_flame_state=True
        if(enemy16_health<=0):
            enemy16_alive=False
            variable=17
            checker=1
    
    if(gamestate==4):
        pygame.display.set_caption('FINAL BATTLE!')
        clock.tick(900)
        #dt=clock.tick(50)
        
        checkmate=0
    
        screen.blit(FinalBridge, (0,0))
        if player_y < 210:
            z=1
            player_y_velocity += 2
            screen.blit(jump[1],(player_x,player_y))  # You can adjust this value to control gravity strength
        else:
            player_y_velocity = 0  # Reset velocity when on the ground
            player_y = 210 
        if keys[pygame.K_UP] and player_y == 210:  # Check if player is on the ground
            screen.blit(jump[1], (player_x, player_y))
            player_y_velocity = -18
        
        if keys[pygame.K_RIGHT] and z==0: 
            index = (index + 1) % len(run)
            time = 0
            player_x+=5
            screen.blit(run[index], (player_x, player_y))
        elif keys[pygame.K_LEFT] and z==0: 
            index = (index + 1) % len(left_run)
            time = 0
            player_x-=5
            screen.blit(left_run[index], (player_x, player_y))
        elif (player_y<210):
            player_y+=z
        elif keys[pygame.K_x] and z==0:
            #dt=clock.tick(50)
            index = (index+1) % len(attack)
            time=0
            screen.blit(attack[index],(player_x,player_y))
            if(enemy17_alive==True and enemy17_x in range(player_x,player_x+63)):
                enemy17_health-=10
            
        elif  keys[pygame.K_k] and z==0: 
            #dt=clock.tick(50)
            index = (index+1) % len(kick)
            time=0
            screen.blit(kick[index],(player_x,player_y))
            if(enemy17_alive==True and enemy17_x in range(player_x,player_x+63)):
                enemy17_health-=10
            
        elif(z==0 and not(keys[pygame.K_k]) and not(keys[pygame.K_l]) and not(keys[pygame.K_x]) and not(keys[pygame.K_z]) and not(keys[pygame.K_RIGHT] ) and not(keys[pygame.K_LEFT]) and not(keys[pygame.K_UP])):                       
            screen.blit(idle[0],(player_x,player_y))
        player_y += player_y_velocity
        if (enemy17_alive==True):
            if(enemy17_x>player_x+60):
            
                if(enemy17_alive==True):
                    if(enemy17_x==800):
                        bullet1_state=True 
                        bullet1_x=enemy17_x
                        bullet1_y=enemy17_y+75
                    if(enemy17_x==600):
                        bullet2_state=True 
                        bullet2_x=enemy17_x
                        bullet2_y=enemy17_y+75
                    if(bullet1_state==True):
                        screen.blit(fireball1,(bullet1_x,bullet1_y))
                        bullet1_x-=20
                        if(bullet1_x in range(player_x, player_x+60) and (player_y==210)):
                            player_health-=10//diff
                            bullet1_state=False
                    if(bullet2_state==True):
                        screen.blit(fireball2,(bullet2_x,bullet2_y))
                        bullet2_x-=20
                        if(bullet2_x in range(player_x, player_x+30) and (player_y==210)):
                            player_health-=10//diff
                            bullet2_state=False 
                    if(enemy17_x>=player_x+100 and enemy17_x<=player_x+125):
                        #dt=clock.tick(50)
                        index3=(index3+1)%len(erun)
                        time=0
                        screen.blit(erun[index3],(enemy17_x,enemy17_y))
                    elif(enemy17_x>=player_x+70 and enemy17_x<=player_x+100):
                        #dt=clock.tick(50)
                        index_firethrow1=(index_firethrow1+1)%len(erun)
                        time=0
                        screen.blit(erun[index_firethrow1],(enemy17_x,enemy17_y))
                    else:
                        #dt=clock.tick(50)
                        index_firethrow2=(index_firethrow2+1)%len(erun)
                        time=0
                        screen.blit(erun[index_firethrow2],(enemy17_x,enemy17_y))
                    enemy17_x-=10
            if(enemy17_x<=player_x+60):
                #dt=clock.tick(50)
                index3=(index3+1)%len(flamejet)
                time=0
                if(enemy17_alive==True):
                    screen.blit(flamejet[index3],(enemy17_x,enemy17_y))
                if(enemy17_x in range(player_x-50,player_x+50)):
                    player_health-=30//diff
            
            if(enemy17_x<50):
                e3_flame_state=True
            if(enemy17_health<=0):
                enemy17_alive=False
        if ((enemy17_alive==False) and (player_x>=550)):
            gamestate = 4.5
    if (gamestate==4.5):
        pygame.display.set_caption('Mission Accomplished!')
        screen.blit(battle6T, (0,0))
        #dt=clock.tick(10)
        indexp = (indexp+1) % (len(prun)-2)
        index = (index+1) % len(run)
        screen.blit(run[index], (player_f_x,player_f_y))
        screen.blit(prun[indexp], (princess_x,princess_y))
        player_f_x+=10
        princess_x+=10
        if (player_f_x>=670):
            screen.blit(finScreen, (fscreen,0))
            screen.blit(finScreen, (width+fscreen,0))
            fscreen-=30
            if (fscreen==-width):
                gamestate = -1
      

    if (gamestate>=0) and (gamestate!=4.5):
        health_bar.bdraw(player_health,screen)
        if(player_health<=0):
            screen.blit(gameoverT, (gameO,0))
            screen.blit(gameover, (width+gameO,0))
            gameO-=10
            if (gameO==-100):
                running = False
            
        

    pygame.display.flip()
pygame.quit()
sys.exit()


