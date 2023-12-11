# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width() # 50
height = robot.get_height() # 86
# x is left to right 
# y is up to down 
space = width
for i in range(10):
    window.blit(robot, (50 + width * i, 100))





pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()