import pygame

# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pygame
from random import *

pygame.init()
x = 400
y = 300
screen = pygame.display.set_mode((x, y))
done = False

direction = "RIGHT"
x = 10
y = 10
colorSnake = (255, 255, 255)
snakeBody = [(10, 10), (10, 20), (10, 30)]
snake = pygame.Surface((x, y))
snake.fill(colorSnake)

xEnemy = randrange(0, 400, 10)
yEnemy = randrange(0, 300, 10)
colorEnemy = (255, 0, 0)
enemy = pygame.Surface((10, 10))
enemy.fill(colorEnemy)

font = pygame.font.Font("freesansbold.ttf", 14)
points = 0

clock = pygame.time.Clock()


def updateEnemy():
    global xEnemy, yEnemy
    xEnemy = randrange(0, 400, 10)
    yEnemy = randrange(0, 300, 10)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        direction = "UP"
    if pressed[pygame.K_DOWN]:
        direction = "DOWN"
    if pressed[pygame.K_LEFT]:
        direction = "LEFT"
    if pressed[pygame.K_RIGHT]:
        direction = "RIGHT"

    if direction == "UP":
        snakeBody[0] = (snakeBody[0][0], snakeBody[0][1] - 10)
    if direction == "DOWN":
        snakeBody[0] = (snakeBody[0][0], snakeBody[0][1] + 10)
    if direction == "LEFT":
        snakeBody[0] = (snakeBody[0][0] - 10, snakeBody[0][1])
    if direction == "RIGHT":
        snakeBody[0] = (snakeBody[0][0] + 10, snakeBody[0][1])

    for i in range(len(snakeBody) - 1, 0, -1):
        snakeBody[i] = snakeBody[i - 1]

    screen.fill((0, 0, 0))

    if (snakeBody[0][0], snakeBody[0][1]) == (xEnemy, yEnemy):
        points += 10
        updateEnemy()
        newPeace = (
            snakeBody[len(snakeBody) - 1][0],
            snakeBody[len(snakeBody) - 1][1] + 10,
        )
        snakeBody.append(newPeace)

    if snakeBody[0][0] == 390 or snakeBody[0][0] == 0:
        done = True
    if snakeBody[0][1] == 290 or snakeBody[0][1] == 0:
        done = True

    for pos in snakeBody:
        screen.blit(snake, pos)

    screen.blit(enemy, (xEnemy, yEnemy))
    screen.blit(font.render(str(points), True, (0, 255, 0)), (375, 7))

    clock.tick(15)
    pygame.display.update()
    pygame.display.set_caption("Snake")
