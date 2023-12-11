import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load(r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part13-09_bouncing_ball\src\ball.png")

x = 0
y = 0
x_velocity = 1
y_velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()
    
    x += x_velocity
    y += y_velocity

    # Check x boundaries
    if (x_velocity > 0 and x + ball.get_width() >= 640) or (x_velocity < 0 and x <= 0):
        x_velocity = -x_velocity
    
    # Check y boundaries
    if (y_velocity > 0 and y + ball.get_height() >= 480) or (y_velocity < 0 and y <= 0):
        y_velocity = -y_velocity

    clock.tick(1000)  # I've reduced the tick value to make it smoother. Adjust as needed.

"""
import pygame
import math
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
ball = pygame.image.load("ball.png")
 
x = 0
y = 0
ball_x = 2
ball_y = 2
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    x += ball_x
    y += ball_y
 
    if x == 0 or x+ball.get_width() == width:
        ball_x = -ball_x
    if y == 0 or y+ball.get_height() == height:
        ball_y = -ball_y
 
    screen.fill((0, 0, 0))
    screen.blit(ball, (x, y))
    pygame.display.flip()
 
    clock.tick(60)
"""