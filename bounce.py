cmd
echo Xin chao, co mun chs game cua toi ko?
echo Neu co bam bat ky nut nao de chs!
pause
python 
import sys
import pygame
import os 

os.system('powershell /c "python -m pygame.examples.aliens"')

pygame.init()

size = width, height = 640, 480
dx = 1
dy = 1
x= 163
y = 120
black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    os.system('cmd /c "@echo off"')
    os.system('cmd /c "echo Ban da thua, chs lai ko?"')
    os.system('cmd /c "pause"')
    os.system('powershell /c "python -m pygame.examples.aliens"')   
