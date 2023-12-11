# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width() # 50
height = robot.get_height() # 86


for i in range(10):
    for j in range(10):
        window.blit(robot, (50 + (i * 5) + width * j, (100 + i * 15)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


"""
import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
for i in range(10):
    for j in range(10):
        screen.blit(robot, (20+10*i+40*j, 100+i*20))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
# WRITE YOUR SOLUTION HERE:
 
"""