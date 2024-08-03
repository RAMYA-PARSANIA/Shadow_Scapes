import pygame
import spritesheet

width = 720
height = 480
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)


fireball1=pygame.image.load('pygameAssests\Fire_bullet.png')
fireball2=pygame.image.load('pygameAssests\Fire_bullet.png')

BG = pygame.image.load("pygameAssests\menubg1.png")
opBg = pygame.image.load("pygameAssests\optionbg.png")

cloudBg1 = pygame.image.load("pygameAssests\cloud1.png")
mountBg1 = pygame.image.load("pygameAssests\mountV1.png")

battle1 = pygame.image.load("pygameAssests\cloud1.png")
ferntree = pygame.image.load("pygameAssests\Fern_tree1.png")
smFern = pygame.image.load("pygameAssests\Fern_tree2.png")
w2rock = pygame.image.load("pygameAssests\w2rock.png")

interm_screen = pygame.image.load("pygameAssests\game_background_4.png")
battle2 = pygame.image.load("pygameAssests\game_background_1.png")
ruinb2_1 = pygame.image.load("pygameAssests\Brown_ruins1.png")
jumprock1 = pygame.image.load("pygameAssests\canyon_rock3.png")
bigrock1 = pygame.image.load("pygameAssests\canyon_rock1.png")

battle3 = pygame.image.load("pygameAssests\Battleground1.png")
ruin1 = pygame.image.load("pygameAssests\White_ruins1.png")
ruin2 = pygame.image.load("pygameAssests\White_ruins2.png")

battle4 = pygame.image.load("pygameAssests\game_background_3.png")
sruin1 = pygame.image.load("pygameAssests\Sand_ruins1.png")
battle5 = pygame.image.load("pygameAssests\game_background_2.png")
battle6 = pygame.image.load("pygameAssests\castleBridge.png")
castle = pygame.image.load("pygameAssests\castle.png")
castleCorr = pygame.image.load("pygameAssests\Battleground2.png")
shadow_world = pygame.image.load("pygameAssests\shadow_world.png")

FinalBridge = pygame.image.load("pygameAssests\skyBridge.png")
FinalBridge_M = pygame.image.load("pygameAssests\skyBridge_n.png")
creditsPage = pygame.image.load("pygameAssests\credits.png")

gameover = pygame.image.load("pygameAssests\gameover.png")
