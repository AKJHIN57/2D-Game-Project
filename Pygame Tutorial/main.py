import pygame, sys
pygame.init()                                                                                   #Obligatory for every pygame project to initialize the window

rozdzielczosc = pygame.display.Info()
WINDOW_WIDTH, WINDOW_HEIGHT = 1800, 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("First Game")
x = 50
y = 5
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    display_surface.fill((0,0,0))
    pygame.draw.rect(display_surface, (255,0,0), (x,y, width, height))
    pygame.display.flip()