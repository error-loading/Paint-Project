import pygame
import os

pygame.init()

images = []

folderDir = f"{os.getcwd()}/imgs/tools"

for imgs in os.listdir(folderDir):
    img = pygame.image.load(f"{folderDir}/{imgs}")
    images.append(img)



# toolbar screen 
def toolbarScreen():
    screen = pygame.display.set_mode((1280, 200))
    pygame.display.set_caption("Toolbar Menu")

    running = True

    while running:
        screen.fill((255, 255 , 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for i in range(len(images)):
            if i < len(images) / 2:
                screen.blit(images[i], (60*i, 0))
            else:
                screen.blit(images[i], (60*(i-len(images)/2-1), images[i].get_height()))
    
    pygame.display.flip()
    