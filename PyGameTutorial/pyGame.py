import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Car Game')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.PNG')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


x = (display_width * 0.45)
y = (display_height * 0.80)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.QUIT()
quit()
