import pygame
from allLoadedAssets import *
finScreen = pygame.transform.scale(BG, (width,height))
cloudBg1T = pygame.transform.scale(cloudBg1, (width,height))
mountBg1T = pygame.transform.scale(mountBg1, (width,height))

interm_screenT = pygame.transform.scale(interm_screen, (720,480))
#scaled images of ruins for battle1T:

battle2T = pygame.transform.scale(battle2, (width,height))
battle2T_1 = pygame.transform.scale(battle2, (width,height))
battle2T_j1 = pygame.transform.scale(battle2, (width,height))
battle2T_j2 = pygame.transform.scale(battle2, (width,height))
battle2T_b1 = pygame.transform.scale(battle2, (width,height))
jumprock1_T = pygame.transform.scale(jumprock1, (67,53))

w1b1 = pygame.Vector2(2880, -200)
# battle2T_j1 = pygame.transform.scale(battle2, (width,height))
b2 = pygame.Vector2(battle2T.get_width(),battle2T.get_height())
ruinb2_1T = pygame.transform.scale(ruinb2_1, (133,143)) #at (327,104) on map
ruinb2_1T_mask = pygame.mask.from_surface(ruinb2_1T).outline()
ruinb2_1T_mask = [(x+327, y+104) for x,y in ruinb2_1T_mask]
world1 = 0
sworld1 = 0
sw1z = 0

battle1T = pygame.transform.scale(battle1,(width,height))
battle1T_1 = pygame.transform.scale(battle1, (width,height))
battle1T_j1 = pygame.transform.scale(battle1, (width,height))
battle1T_j2 = pygame.transform.scale(battle1, (width,height))
battle1T_j3 = pygame.transform.scale(battle1, (width,height))
b1 = pygame.Vector2(battle1T.get_width(),battle1T.get_height())
w2rock_T = pygame.transform.scale(w2rock, (74,55))

fernT = pygame.transform.scale(ferntree, (212,210)) #at (205,111) on map
fernT_mask = pygame.mask.from_surface(fernT).outline()
fernT_mask = [(x+205, y+130) for x, y in fernT_mask]
smFernT = pygame.transform.scale(smFern, (101,91)) #at (347,176) on map
smFernT_mask = pygame.mask.from_surface(smFernT).outline()
smFernT_mask = [(x+347,y+176) for x, y in smFernT_mask]
world2 = 0
sworld2 = 0
sw2z = 0


battle3T = pygame.transform.scale(battle3, (width,height)) #obstacle at x=204
b3 = pygame.Vector2(battle3T.get_width(),battle3T.get_height())
battle3T_1 = pygame.transform.scale(battle3, (width, height))
ruin2_1 = pygame.transform.scale(ruin2, (160,155)) #at (404,203) on map
ruin2_1_mask = pygame.mask.from_surface(ruin2_1).outline()
ruin2_1_mask = [(x+404, y+203) for x, y in ruin2_1_mask]
ruin1_1 = pygame.transform.scale(ruin1, (172,162)) #at (42,188) on map
ruin1_1_mask = pygame.mask.from_surface(ruin1_1).outline()
ruin1_1_mask = [(x+42, y+188) for x, y in ruin1_1_mask] 
world3 = 0
sworld3 = 0
sw3z = 0

battle4T = pygame.transform.scale(battle4, (width,height))
b4 = pygame.Vector2(battle4T.get_width(),battle4T.get_height())
battle4T_1 = pygame.transform.scale(battle4, (width,height))
sruin1_T = pygame.transform.scale(sruin1, (150,160)) #at (403,100)
sruin1_T_mask = pygame.mask.from_surface(sruin1_T).outline()
sruin1_T_mask = [(x+403, y+100) for x, y in sruin1_T_mask]
world4 = 0
sworld4 = 0
sw4z = 0

battle5T = pygame.transform.scale(battle5, (width, height))
b5 = pygame.Vector2(battle5T.get_width(),battle5T.get_height())

battle6T = pygame.transform.scale(battle6, (width,height))
b6 = pygame.Vector2(battle6T.get_width(),battle6T.get_height())

castleT = pygame.transform.scale(castle, (width,height))
cT = pygame.Vector2(castleT.get_width(),castleT.get_height())
castleCorrT = pygame.transform.scale(castleCorr, (width,height))
cCT = pygame.Vector2(castleCorrT.get_width(),castleCorrT.get_height())
shadow_worldT = pygame.transform.scale(shadow_world, (width,height))
swT = pygame.Vector2(shadow_worldT.get_width(),shadow_worldT.get_height())
finalT = pygame.transform.scale(FinalBridge, (width,height))
fT = pygame.Vector2(finalT.get_width(),finalT.get_height())
finalMT = pygame.transform.scale(FinalBridge_M, (width,height))
fMT = pygame.Vector2(finalMT.get_width(),finalMT.get_height())

creditsT = pygame.transform.scale(creditsPage, (width,height))

gameoverT = pygame.transform.scale(gameover, (width,height))