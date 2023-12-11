import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load(r"src\robot.png")

x = 0
x_2 = 0
y = 0
velocity = 1
velocity_2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x_2, y + 100))
    pygame.display.flip()

    x += velocity
    x_2 += velocity_2
    
    # For the top robot (x):
    if velocity > 0 and x + robot.get_width() >= 640:
        velocity = -velocity
    elif velocity < 0 and x <= 0:
        velocity = -velocity

    # For the bottom robot (x_2):
    if velocity_2 > 0 and x_2 + robot.get_width() >= 640:
        velocity_2 = -velocity_2
    elif velocity_2 < 0 and x_2 <= 0:
        velocity_2 = -velocity_2

    clock.tick(60)

