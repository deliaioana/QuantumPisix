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

    def move_in_circuit(self):
        self.rect.center = (self.rect.center[0] + 5, self.rect.center[1])

    def is_next_to_camera(self, pos_x):
        return self.rect.center[0] + 100 >= pos_x

    def change_state(self, gate_name):
        if gate_name == 'SPAWNED_catnip_gate':
            self.state = 'super'
            self.speed = 1

        elif gate_name == 'SPAWNED_milk_gate':
            if self.state == 'asleep':
                self.state = 'idle'
                self.speed = 0.02

            elif self.state == 'idle':
                self.state = 'asleep'
                self.speed = 0.02

        elif gate_name == 'SPAWNED_mouse_gate':
            if self.state == 'asleep':
                self.state = 'idle'
                self.speed = 0.02
            elif self.state == 'idle':
                self.state = 'asleep'
                self.speed = 0.02

    def is_next_to_element(self, element):
        pos_x = element.rect.center[0]
        return abs(pos_x - self.rect.center[0]) < 20

    def collapse_state(self, state):
        if state == 1:
            self.state = 'idle'
        else:
            self.state = 'asleep'
        self.update()
