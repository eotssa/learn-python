## *Robot Invasion*
```python
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_img = pygame.image.load(r"src\robot.png")

# Define a Robot class to hold properties for each robot
class Robot:
    def __init__(self):
        self.x = random.randint(0, 640 - robot_img.get_width())
        self.y = 0
        self.y_velocity = 1
        self.x_velocity = 0

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        # Check if the robot has hit the ground
        if self.y + robot_img.get_height() >= 480 and self.y_velocity > 0:
            self.y_velocity = 0  # Stop vertical movement
            self.x_velocity = random.choice([-1, 1])  # Choose a random direction: left (-1) or right (1)

    def off_screen(self):
        return self.x + robot_img.get_width() < 0 or self.x >= 640

robots = []
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    for robot in robots:
        robot.move()
        window.blit(robot_img, (robot.x, robot.y))
    
    # Remove robots that have moved off-screen
    robots = [robot for robot in robots if not robot.off_screen()]
    
    # Occasionally add a new robot
    if random.random() < 0.05:
        robots.append(Robot())

    pygame.display.flip()
    clock.tick(60)

```

# *Robot Invasion Model Version w/ comments*
```python
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# number of robots (the same robots are reused)
number = 20
 
robots = []
for i in range(number):
    # causes the new random start position to be drawn immediately
    robots.append([-1000,height])  # -1000 sets robot's to the far left of the screen out of view 
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    for i in range(number):
        if robots[i][1]+robot.get_height() < height:   # checks if robot above the bottom of the screen, if it is, then increment by 1 until reaches the floor 
            # the robot falls downwards
            robots[i][1] += 1
        else:                                         # once on the floor... 
            if robots[i][0] < -robot.get_width() or robots[i][0] > width:     # checks if robot is off the screen to the left or off the screen to the right 
                # new random start point
                robots[i][0] = randint(0,width-robot.get_width())              
                robots[i][1] = -randint(100,1000)                              # reason for negative val ensures robot is above the screen (in height), 100-1000 ensures randomness 
            elif robots[i][0]+robot.get_width()/2 < width/2:     # if robot is on the left half, move left
                # the robot moves to the left
                robots[i][0] -= 1
            else:
                # the robot moves to the right
                robots[i][0] += 1
 
    screen.fill((0, 0, 0))
    for i in range(number):
        screen.blit(robot, (robots[i][0], robots[i][1]))
    pygame.display.flip()
 
    clock.tick(60)

```