import pygame
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

direction = "RIGHT"
x = 10
y = 10

clock = pygame.time.Clock()

colorSnake = (255,255,255)

tamanho = 10

def desenha(screen, color, x,y,l,a):
    pygame.draw.rect(screen, colorSnake, (x,y, l, a))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: direction = "UP"
    if pressed[pygame.K_DOWN]: direction = "DOWN"
    if pressed[pygame.K_LEFT]: direction = "LEFT"
    if pressed[pygame.K_RIGHT]: direction = "RIGHT"

    if direction=="UP": y -= 10
    if direction=="DOWN": y += 10
    if direction=="LEFT": x -= 10
    if direction=="RIGHT": x += 10

    tamanho += 10

    screen.fill((0, 0, 0))   

    desenha(screen, colorSnake, x, y, 10, 10)  

    clock.tick(45)
    pygame.display.update()
