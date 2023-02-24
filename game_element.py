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

        self.is_attached_to_free_space = False
        self.free_space = None

        self.free_space_area_size = 100
        self.attached_gate = None
        self.is_visible = True

    def update(self):
        self.current_sprite += self.speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        if self.is_moving:
            self.rect.center = pygame.mouse.get_pos()

    def is_position_inside(self, position):
        x, y = position
        center_x, center_y = self.rect.center
        clickable_area = self.clickable_area_size / 2

        return (center_x - clickable_area <= x <= center_x + clickable_area) and \
               (center_y - clickable_area <= y <= center_y + clickable_area)

    def is_inside_free_space(self, free_space):
        x, y = free_space.rect.center
        center_x, center_y = self.rect.center

        free_space_area = self.free_space_area_size / 2

        return (x - free_space_area <= center_x <= x + free_space_area) and \
               (y - free_space_area <= center_y <= y + free_space_area)

    def attach_gate(self, gate):
        self.attached_gate = gate
        self.is_visible = False

        gate.is_attached_to_free_space = True
        gate.free_space = self
        gate.center_here(self.rect.center)

    def center_here(self, position):
        self.rect.center = position
