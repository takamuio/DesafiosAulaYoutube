import pygame
pygame.init()

tela = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Tocando musica com pygame')
branco = (255, 255, 255)

musica = pygame.mixer.Sound('teste21.mp3')
musica.play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tela.fill(branco)
    pygame.display.update()
