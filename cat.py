import pygame


class Cat(pygame.sprite.Sprite):
    def __init__(self, idle_frames, asleep_frames, super_frames, state, x, y):
        super().__init__()
        self.sprites = {'idle': idle_frames, 'asleep': asleep_frames, 'super': super_frames}
        self.state = state
        self.current_sprite = 0
        self.image = self.sprites[self.state][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 0.02
        if self.state == 'super':
            self.speed = 1

    def update(self):
        self.current_sprite += self.speed
        if int(self.current_sprite) >= len(self.sprites[self.state]):
            self.current_sprite = 0

        self.image = self.sprites[self.state][int(self.current_sprite)]
