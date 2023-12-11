# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0

target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION: 
            target_x = event.pos[0] - (robot.get_width() / 2)
            target_y = event.pos[1] - (robot.get_height() / 2)

        if event.type == pygame.QUIT:
            exit()

        # robot will follow mouse position


    window.fill((0, 0, 0))
    window.blit(robot, (target_x, target_y))
    pygame.display.flip()

    clock.tick(60)



"""
# Follows the mouse, kinda
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0

target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION: 
            target_x = event.pos[0] - (robot.get_width() / 2)
            target_y = event.pos[1] - (robot.get_height() / 2)

        if event.type == pygame.QUIT:
            exit()

        # robot will follow mouse position
        if robot_x > target_x:
            robot_x -= 1
        if robot_x < target_x:
            robot_x += 1
        if robot_y > target_y:
            robot_y -= 1
        if robot_y < target_y:
            robot_y += 1

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
"""

### Following code teleports robot to mouse position

"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]-robot.get_width()/2
            y = event.pos[1]-robot.get_height()/2

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()
"""