import pygame
import spritesheet

width = 720
height = 480
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)
black=000
sprite_sheet_image=pygame.image.load('pygameAssests\player_run.png').convert_alpha() 
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
sprite_sheet_image1=pygame.image.load('pygameAssests\player_jump.png').convert_alpha()
sprite_sheet1=spritesheet.sprite_sheet(sprite_sheet_image1)
sprite_sheet_image2=pygame.image.load('pygameAssests\player_attack.png').convert_alpha()
sprite_sheet2=spritesheet.sprite_sheet(sprite_sheet_image2)
sprite_sheet_image3=pygame.image.load('pygameAssests\player_attack1.png').convert_alpha()
sprite_sheet3=spritesheet.sprite_sheet(sprite_sheet_image3)
sprite_sheet_image4=pygame.image.load('pygameAssests\player_idle.png').convert_alpha()
sprite_sheet4=spritesheet.sprite_sheet(sprite_sheet_image4)
sprite_sheet_image5=pygame.image.load('pygameAssests\player_kick.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(sprite_sheet_image5)
sprite_sheet_image6=pygame.image.load('pygameAssests\player_shield.png').convert_alpha()
sprite_sheet6=spritesheet.sprite_sheet(sprite_sheet_image6)
sprite_sheet_image7=pygame.image.load('pygameAssests\player_dead.png').convert_alpha()
sprite_sheet7=spritesheet.sprite_sheet(sprite_sheet_image7)
sprite_sheet_image8=pygame.image.load('pygameAssests\enemy_run1.png').convert_alpha()
sprite_sheet8=spritesheet.sprite_sheet(sprite_sheet_image8)
erun=[sprite_sheet8.image(0.4,90,150,2,black),sprite_sheet8.image(2.05,90,150,2,black),sprite_sheet8.image(3.8,90,150,2,black),sprite_sheet8.image(5.55,90,150,2,black),sprite_sheet8.image(7.1,90,150,2,black),sprite_sheet8.image(8.85,90,150,2,black),sprite_sheet8.image(10.4,90,150,2,black),sprite_sheet8.image(12.2,90,150,2,black)]
sprite_sheet_image9=pygame.image.load('pygameAssests\enemy_attack.png').convert_alpha()
sprite_sheet9=spritesheet.sprite_sheet(sprite_sheet_image9)
eattack=[sprite_sheet9.image(0,100,160,2,black),sprite_sheet9.image(1.7,100,160,2,black),sprite_sheet9.image(4,90,160,2,black),sprite_sheet9.image(5.8,90,160,2,black)]
sprite_sheet_image11=pygame.image.load('pygameAssests\enemy_flamejet.png').convert_alpha()
sprite_sheet11=spritesheet.sprite_sheet(sprite_sheet_image11)
flamejet=[sprite_sheet11.image(0.05,139,160,2,black),sprite_sheet11.image(1.2,139,160,2,black),sprite_sheet11.image(2.3,139,160,2,black),sprite_sheet11.image(3.45,139,160,2,black),sprite_sheet11.image(4.6,139,160,2,black),sprite_sheet11.image(5.75,139,160,2,black),sprite_sheet11.image(6.9,139,160,2,black),sprite_sheet11.image(8.05,139,160,2,black),sprite_sheet11.image(9.2,139,160,2,black),sprite_sheet11.image(10.4,139,160,2,black),sprite_sheet11.image(11.8,139,160,2,black),sprite_sheet11.image(13,139,160,2,black),sprite_sheet11.image(14,139,160,2,black),sprite_sheet11.image(15.3,139,160,2,black)]
sprite_sheet_image12=pygame.image.load('pygameAssests\enemy_dead.png').convert_alpha()
sprite_sheet12=spritesheet.sprite_sheet(sprite_sheet_image12)
sprite_sheet_image13=pygame.image.load('pygameAssests\e1_run.png').convert_alpha()
sprite_sheet13=spritesheet.sprite_sheet(sprite_sheet_image13)
e1run=[sprite_sheet13.image(0.2,90,130,2,black),sprite_sheet13.image(1.5,90,130,2,black),sprite_sheet13.image(3,90,130,2,black),sprite_sheet13.image(4.4,90,130,2,black),sprite_sheet13.image(5.8,90,130,2,black),sprite_sheet13.image(7.3,90,130,2,black)]
sprite_sheet_image14=pygame.image.load('pygameAssests\e1_attack.png').convert_alpha()
sprite_sheet14=spritesheet.sprite_sheet(sprite_sheet_image14)
y0=[sprite_sheet14.image(0.2,90,130,2,black),sprite_sheet14.image(1.5,90,130,2,black),sprite_sheet14.image(3,90,130,2,black),sprite_sheet14.image(4.4,90,130,2,black),sprite_sheet14.image(5.8,90,130,2,black)]
enemy1_attack=y0[::-1]
sprite_sheet_image15=pygame.image.load('pygameAssests\e1_dead.png').convert_alpha()
sprite_sheet15=spritesheet.sprite_sheet(sprite_sheet_image15)
y0=[sprite_sheet15.image(0.2,90,130,2,black),sprite_sheet15.image(1.7,90,130,2,black),sprite_sheet15.image(3.2,90,130,2,black),sprite_sheet15.image(4.6,90,130,2,black)]
enemy1_dead=y0[::-1]
bg=(100,100,100)
black=(0,0,0)
run=[sprite_sheet.image(0.2,90,130,2,black),sprite_sheet.image(1.6,90,130,2,black),sprite_sheet.image(3,90,130,2,black),sprite_sheet.image(4.48,90,130,2,black),sprite_sheet.image(5.9,90,130,2,black),sprite_sheet.image(7.3,90,130,2,black),sprite_sheet.image(8.7,90,130,2,black),sprite_sheet.image(10.1,90,130,2,black)]
jump=[sprite_sheet1.image(0.2,90,130,2,black),sprite_sheet1.image(1.6,90,130,2,black),sprite_sheet1.image(3,90,130,2,black),sprite_sheet1.image(4.48,90,130,2,black),sprite_sheet1.image(5.9,90,130,2,black),sprite_sheet1.image(7.3,90,130,2,black),sprite_sheet1.image(8.7,90,130,2,black),sprite_sheet1.image(10.1,90,130,2,black)]
attack=[sprite_sheet2.image(0.2,90,130,2,black),sprite_sheet2.image(1.6,75,130,2,black),sprite_sheet2.image(3,90,130,2,black),sprite_sheet2.image(4.48,90,130,2,black),sprite_sheet3.image(0.15,90,130,2,black),sprite_sheet3.image(1.5,90,130,2,black),sprite_sheet3.image(2.95,90,130,2,black)]
idle=[sprite_sheet4.image(0.15,90,130,2,black)]
kick=[sprite_sheet5.image(0.2,90,130,2,black),sprite_sheet5.image(1.6,90,130,2,black),sprite_sheet5.image(3,90,130,2,black),sprite_sheet5.image(4.48,90,130,2,black)]
shield=[sprite_sheet6.image(0.2,90,130,2,black),sprite_sheet6.image(1.6,90,130,2,black)]
dead=[sprite_sheet7.image(0.2,90,130,2,black),sprite_sheet7.image(1.6,90,130,2,black),sprite_sheet7.image(3,90,130,2,black)]


sprite_sheet_image76=pygame.image.load('pygameAssests\player_rund.png').convert_alpha()  #player run left
sprite_sheet76=spritesheet.sprite_sheet(sprite_sheet_image76)
left_run=[sprite_sheet76.image(0.2,90,130,2,black),sprite_sheet76.image(1.6,90,130,2,black),sprite_sheet76.image(3,90,130,2,black),sprite_sheet76.image(4.48,90,130,2,black),sprite_sheet76.image(5.9,90,130,2,black),sprite_sheet76.image(7.3,90,130,2,black),sprite_sheet76.image(8.7,90,130,2,black),sprite_sheet76.image(10.1,90,130,2,black)]

sprite_sheet_image77=pygame.image.load('pygameAssests\player_attackd.png').convert_alpha() #player left
sprite_sheet77=spritesheet.sprite_sheet(sprite_sheet_image77)


sprite_sheet_image78=pygame.image.load('pygameAssests\player_attack1.png').convert_alpha()   #player left
sprite_sheet78=spritesheet.sprite_sheet(sprite_sheet_image78)
left_attack=[sprite_sheet77.image(0.2,90,130,2,black),sprite_sheet77.image(1.6,90,130,2,black),sprite_sheet77.image(3,90,130,2,black),sprite_sheet77.image(4.48,90,130,2,black),sprite_sheet78.image(0.15,90,130,2,black),sprite_sheet78.image(1.5,90,130,2,black),sprite_sheet78.image(2.95,90,130,2,black)]

sprite_sheet_image79=pygame.image.load('pygameAssests\player_kick.png').convert_alpha()   #player left
sprite_sheet79=spritesheet.sprite_sheet(sprite_sheet_image79)
left_kick=[sprite_sheet79.image(0.2,90,130,2,black),sprite_sheet79.image(1.6,90,130,2,black),sprite_sheet79.image(3,90,130,2,black),sprite_sheet79.image(4.48,90,130,2,black)]

sprite_sheet_imagep = pygame.image.load("pygameAssests\princess_run.png").convert_alpha()
sprite_sheetp=spritesheet.sprite_sheet(sprite_sheet_imagep)
prun=[sprite_sheetp.image(0.2,90,130,2,black),sprite_sheetp.image(1.6,90,130,2,black),sprite_sheetp.image(3,90,130,2,black),sprite_sheetp.image(4.48,90,130,2,black),sprite_sheetp.image(5.9,90,130,2,black),sprite_sheetp.image(7.3,90,130,2,black),sprite_sheetp.image(8.7,90,130,2,black),sprite_sheetp.image(10.1,90,130,2,black)]

