# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width() # 50
height = robot.get_height() # 86


for j in range(1000):
    window.blit(robot, (random.randint(0, 640), random.randint(0, 480)))

"""
for i in range(1000):
    x = randint(0,width-robot.get_width())
    y = randint(0,height-robot.get_height())
    screen.blit(robot, (x,y))
"""




pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

