import pygame
from EventListener import EventListener
from Laser import Laser
from RenderObject import RenderObject


class Player(EventListener, RenderObject):
    move_speed = 5
    size = (100, 75)
    y = 650
    x_bounds = (100, 1150)

    def __init__(self, game):
        self.game = game
        game.render_objects.append(self)
        game.event_listeners.append(self)

        self.sprite = pygame.transform.scale(pygame.image.load("assets/laser.webp"), self.size)
        self.rect = self.sprite.get_rect()
        self.rect.x = (self.x_bounds[0] + self.x_bounds[1]) / 2 - self.size[0] / 2
        self.rect.y = self.y

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Laser(self.game, (self.rect.x + self.size[0] / 2, self.rect.y))

    def tick(self, surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.move_speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.move_speed, 0)

        if self.rect.x < self.x_bounds[0]:
            self.rect.x = self.x_bounds[0]
        elif self.rect.x > self.x_bounds[1] + self.size[0] / 2:
            self.rect.x = self.x_bounds[1] + self.size[0] / 2

        surface.blit(self.sprite, self.rect)
