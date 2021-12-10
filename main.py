import os
import sys
import random

import pygame


# Изображение не получится загрузить
# без предварительной инициализации pygame
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Creature(pygame.sprite.Sprite):
    creature = load_image("E:/PytonProject/data/creature.png")
    creature2 = load_image("E:/PytonProject/data/creature2.png")

    def __init__(self, width, height, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Creature.creature
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.image = Creature.creature2
                self.rect.x -= 10
                # если была нажата стрелка вправо
            if event.key == pygame.K_RIGHT:
                self.image = Creature.creature
                self.rect.x += 10
                # если была нажата стрелка вниз
            if event.key == pygame.K_DOWN:
                self.rect.y += 10
                # если была нажата стрелка вверх
            if event.key == pygame.K_UP:
                self.rect.y -= 10


def main():
    pygame.init()
    width = 500
    height = 500
    size = (width, height)
    screen = pygame.display.set_mode(size)
    running = True
    pygame.display.set_caption("СУЩЕСТВО")
    all_sprites = pygame.sprite.Group()
    Creature(width, height, all_sprites)
    while running:
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        for event in pygame.event.get():
            all_sprites.update(event)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
