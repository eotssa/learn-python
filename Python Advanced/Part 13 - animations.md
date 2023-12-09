# Creating an animation
The following code creates an animation where a robot moves from left to right in a pygame window:


```
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += 1
    clock.tick(60)
```

# Bouncing off a wall
The previous animation was otherwise excellent, but as the robot reached a wall, it just kept going out of sight. Let's make the robot bounce off the wall.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(60)
```

# Rotation
Let's create one more animation. This time the robot should rotate in a circle around the centre of the window:

```python
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320+math.cos(angle)*100-robot.get_width()/2
    y = 240+math.sin(angle)*100-robot.get_height()/2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
```


```python
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
```


# Vertical 
Please create an animation where the robot moves up and down in an endless loop. 
```python
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x = 0
y = 0
speed = 1
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
 
    y += speed
    if speed > 0 and y+robot.get_height() >= height:
        speed = -speed
    if speed < 0 and y <= 0:
        speed = -speed
 
    clock.tick(60)
    
```

# Round the perimeter
Please create an animation where the robot traces the perimeter of the window.
```python
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x = 0
y = 0
direction = 1 # 1 = to right, 2 = to down, 3 = to left, 4 = to up
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
 
    if direction == 1:
        x += 1
        if x+robot.get_width() == width:
            direction = 2
    elif direction == 2:
        y += 1
        if y+robot.get_height() == height:
            direction = 3
    elif direction == 3:
        x -= 1
        if x == 0:
            direction = 4
    elif direction == 4:
        y -= 1
        if y == 0:
            direction = 1
```


# Two robots
Please create an animation where two robots move back and forth to the left and right. The lower robot should move at double the speed of the upper one. 
```python
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


```

# Robots in a circle
Please create an animation where ten robots go round in a circle. 

```python
# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load(r"src\robot.png")

angle = 0
num_robots = 10
angle_increment = 2 * math.pi / num_robots
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    for i in range(num_robots):
        current_angle = angle + i * angle_increment
        
        x = 320 + math.cos(current_angle) * 100 - robot.get_width() / 2
        y = 240 + math.sin(current_angle) * 100 - robot.get_height() / 2
        
        window.blit(robot, (x, y))
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)


"""
import pygame
import math
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
angle = 0
radius = 150
number = 10
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    for i in range(number):
        x = width/2+math.cos(angle+2*math.pi*i/number)*radius-robot.get_width()/2
        y = height/2+math.sin(angle+2*math.pi*i/number)*radius-robot.get_height()/2
        screen.blit(robot, (x, y))
    pygame.display.flip()
 
    angle += 0.01
    clock.tick(60)
"""
```

# Bouncing ball
Please create an animation where a ball bounces from the edges of the window

```python
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
```
