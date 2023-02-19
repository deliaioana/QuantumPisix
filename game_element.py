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
        self.is_moving = False
        self.clickable_area_size = 100

    def update(self):
        self.current_sprite += self.speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        if self.is_moving:
            self.rect.center = pygame.mouse.get_pos()

    def is_inside(self, position):
        x, y = position
        center_x, center_y = self.rect.center
        clickable_area = self.clickable_area_size / 2

        return center_x - clickable_area <= x <= center_x + clickable_area \
            and center_y - clickable_area <= y <= center_y + clickable_area
