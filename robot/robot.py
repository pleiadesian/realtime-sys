import sys
import pygame
from pygame.locals import *
bif = "background.png"
mif = "robot.png"
WIDTH, HEIGHT = 640, 360


pygame.init()
pygame.display.set_caption("Robot")

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
background = pygame.image.load(bif).convert()
robot = pygame.image.load(mif).convert_alpha()

robot_normal = robot
robot_right = pygame.transform.rotate(robot, -90)
robot_down = pygame.transform.rotate(robot_right, -90)
robot_left = pygame.transform.rotate(robot_down, -90)

x, y = 0, 0
movex, movey = 0, 0
# print(robot.get_width(), robot.get_height())
while True:
    step = 0.2
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -step
                robot = robot_left
            if event.key == K_RIGHT:
                movex = +step
                robot = robot_right
            elif event.key == K_UP:
                movey = -step
                robot = robot_normal
            elif event.key == K_DOWN:
                movey = +step
                robot = robot_down
        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex = 0
            if event.key == K_RIGHT:
                movex = 0
            elif event.key == K_UP:
                movey = 0
            elif event.key == K_DOWN:
                movey = 0
    nx, ny = x + movex, y + movey
    x = nx if 0 <= nx and nx <= (WIDTH - robot.get_width()) else x
    y = ny if 0 <= ny and ny <= (HEIGHT - robot.get_height()) else y
    screen.blit(background, (0, 0))
    screen.blit(robot, (x, y))
    pygame.display.update()
