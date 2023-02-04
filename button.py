import pygame


# button class
class Button:
    def __init__(self, x, y, image, hover_image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale)))
        self.active_image = image
        self.hovering = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.hovering = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        else:
            self.hovering = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        self.update_image()
        surface.blit(self.active_image, (self.rect.x, self.rect.y))

        return action

    def update_image(self):
        if self.hovering:
            self.active_image = self.hover_image
        else:
            self.active_image = self.image


