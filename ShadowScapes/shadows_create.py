import pygame
import math
from allLoadedAssets import *
from allTransformed import *

sun_pos = pygame.Vector2(100,0)

#Shadow for world2
target_pos_w1 = pygame.Vector2(349,300)
sun_angle_w1 = math.atan2((sun_pos.y - target_pos_w1.y), (sun_pos.x - target_pos_w1.x))
shadows_w1 = []
for x, y in fernT_mask:
    shadow_height = (300 - y ) * 1.5
    shadow_width = shadow_height * math.tan(sun_angle_w1)
    shadow_point = (x + shadow_width, y + shadow_height)
    shadows_w1.append(shadow_point)

#shadow for world1
sun_pos1 = pygame.Vector2(150,0)
target_pos_w2 = pygame.Vector2(392,230)
sun_angle_w2 = math.atan2((sun_pos1.y - target_pos_w2.y), (sun_pos1.x - target_pos_w2.x))
shadows_w2 = []
for x, y in ruinb2_1T_mask:
    shadow_height1 = (230 - y ) * 2
    shadow_width1 = shadow_height1 * math.tan(sun_angle_w2)
    shadow_point1 = (x + shadow_width1, y + shadow_height1)
    shadows_w2.append(shadow_point1)

#shadow for world3_r2
sun_pos2 = pygame.Vector2(720,0)
target_pos_w3_r2 = pygame.Vector2(330,330)
sun_angle_w3_r2 = math.atan2((sun_pos2.y - target_pos_w3_r2.y), (sun_pos2.x - target_pos_w3_r2.x))
shadows_w3_r2 = []
for x, y in ruin2_1_mask:
    shadow_height2 = (330 - y ) * 1.5
    shadow_width2 = shadow_height2 * math.tan(sun_angle_w3_r2)
    shadow_point2 = (x + shadow_width2, y + shadow_height2)
    shadows_w3_r2.append(shadow_point2)

#shadow for world3_r1
sun_pos3 = pygame.Vector2(720,0)
target_pos_w3_r1 = pygame.Vector2(100,350)
sun_angle_w3_r1 = math.atan2((sun_pos3.y - target_pos_w3_r1.y), (sun_pos3.x - target_pos_w3_r1.x))
shadows_w3_r1 = []
for x, y in ruin1_1_mask:
    shadow_height3 = (350 - y ) * 1.4
    shadow_width3 = shadow_height3 * math.tan(sun_angle_w3_r1)
    shadow_point3 = (x + shadow_width3, y + shadow_height3)
    shadows_w3_r1.append(shadow_point3)

#shadow for world4
sun_pos4 = pygame.Vector2(507,18)
target_pos_w4 = pygame.Vector2(0,265)
sun_angle_w4 = math.atan2((sun_pos4.y - target_pos_w4.y), (sun_pos4.x - target_pos_w4.x))
shadows_w4 = []
for x, y in sruin1_T_mask:
    shadow_height4 = (265 - y ) * 1.8
    shadow_width4 = shadow_height4 * math.tan(sun_angle_w4)
    shadow_point4 = (x + shadow_width4, y + shadow_height4)
    shadows_w4.append(shadow_point4)

