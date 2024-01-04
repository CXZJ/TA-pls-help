import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
game_active = False

sky_surface = pygame.image.load('../graphics/Environment/sky.png').convert_alpha()
font = pygame.font.Font("../font/Pixeltype.ttf", 50)
font_title = pygame.font.Font("../font/Pixeltype.ttf", 100)

title_text = font_title.render("Singing Runner", True, 'white')
title_rect = title_text.get_rect(center=(screen_width // 2, 150))

lobby_text = font.render("Click to Play", True, 'white')
lobby_rect = lobby_text.get_rect(center=(screen_width // 2, screen_height // 2))

music = pygame.mixer.Sound('../audio/music.mp3')
music.set_volume(0.5)
music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            level = Level(level_map,screen)
            game_active = True

    screen.blit(sky_surface, (0, 0))

    if game_active:
        level.run()
        player = level.player.sprite
        # Check if the player falls out of the world using the new method
        if player.check_fall():
            game_active = False

    else:
        screen.blit(lobby_text, lobby_rect)
        screen.blit(title_text, title_rect)

    pygame.display.update()
    clock.tick(60)