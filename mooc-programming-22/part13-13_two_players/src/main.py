import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# positions of robots
positions = [[0, 0],
          [width-robot.get_width(), height-robot.get_height()]]
 
controls = []
# key, which robot moves, horizontal movement, vertical movement
controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, 0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, 0, -2))
controls.append((pygame.K_s, 1, 0, 2))
 
clock = pygame.time.Clock()
 
key_pressed = {}
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True
 
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
 
        if event.type == pygame.QUIT:
            exit()
 

    # controls = (button pressed, robot #, direction right/left, direction up/down)
    for key in controls:
        if key[0] in key_pressed:
            positions[key[1]][0] += key[2]          # positions indicates robot 1 or 0, key[1] stores robot #, then the 2nd indicies positions[robot#][0/1]
            positions[key[1]][1] += key[3]             # the 2nd indicies positions indicates x and y coordinates respectively, note the 2x2 list structure 
                                                            # given the nature of controls tupule, even though it's updating both here, one increments by 0 depending on the key 
    screen.fill((0, 0, 0))
    for i in range(2):
        screen.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
 
    clock.tick(60)
    
# WRITE YOUR SOLUTION HERE:


"""# WRITE YOUR SOLUTION HERE:
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 


# ROBOT ONE
robot = pygame.image.load("robot.png")

x = (width / 2) - (robot.get_width() / 2)
y = (height / 4)- (robot.get_height() / 4)
 
to_right = False
to_left = False
to_up = False
to_down = False

# ROBOT TWO
robot_two = pygame.image.load("robot.png")

a = (width / 8) - (robot.get_width() / 8)
b = (height / 4)- (robot.get_height() / 4)

to_d = False
to_a = False
to_w = False
to_s = False

 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # player one
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True


            # player two
            if event.key == pygame.K_d:
                to_d = True
            if event.key == pygame.K_a:
                to_a = True
            if event.key == pygame.K_w:
                to_w = True
            if event.key == pygame.K_s:
                to_s = True


 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
 

            if event.key == pygame.K_d:
                to_d = False
            if event.key == pygame.K_a:
                to_a = False
            if event.key == pygame.K_w:
                to_w = False
            if event.key == pygame.K_s:
                to_s = False


        if event.type == pygame.QUIT:
            exit()
 
    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2

    if to_d:
        a += 2
    if to_a:
        a -= 2
    if to_w:
        b -= 2
    if to_s:
        b += 2
 
    # sets boundaries 
    x = max(x,0)
    x = min(x,width-robot.get_width())
    y = max(y,0)
    y = min(y,height-robot.get_height())
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    screen.blit(robot_two, (a, b))
    pygame.display.flip()
 
    clock.tick(60)
"""

