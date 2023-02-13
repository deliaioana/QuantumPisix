import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, frames, x, y, speed):
        super().__init__()
        self.sprites = []
        self.sprites.extend(frames)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprite += self.speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
