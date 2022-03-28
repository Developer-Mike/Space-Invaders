import pygame

from EventListener import EventListener
from Laser import Laser
from RenderObject import RenderObject


class Player(EventListener, RenderObject):
    move_speed = 5
    shoot_delay = 15  # 0.25s
    size = (100, 75)
    y = 650
    x_bounds = (100, 1150)

    life_size = (66, 50)
    life_distance = 75
    life_pos = (25, 25)

    def __init__(self, game):
        self.game = game
        self.shoot_timer = 0

        game.render_objects.append(self)
        game.event_listeners.append(self)

        self.lives = 3
        self.life_sprite = pygame.transform.scale(pygame.image.load("assets/laser.webp"), self.life_size)
        self.life_rect = self.life_sprite.get_rect()

        self.sprite = pygame.transform.scale(pygame.image.load("assets/laser.webp"), self.size)
        self.rect = self.sprite.get_rect()
        self.rect.x = (self.x_bounds[0] + self.x_bounds[1]) / 2 - self.size[0] / 2
        self.rect.y = self.y

    def on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.shoot_timer <= 0:
                self.shoot_timer = self.shoot_delay
                Laser(self.game, (self.rect.x + self.size[0] / 2, self.rect.y))

    def tick(self, surface):
        self.shoot_timer -= 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.move_speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.move_speed, 0)

        if self.rect.centerx < self.x_bounds[0]:
            self.rect.centerx = self.x_bounds[0]
        elif self.rect.centerx > self.x_bounds[1]:
            self.rect.centerx = self.x_bounds[1]

        surface.blit(self.sprite, self.rect)

        self.render_lives(surface)

    def render_lives(self, surface):
        current_life_rect = self.life_rect.copy().move(self.life_pos)

        for _ in range(self.lives):
            surface.blit(self.life_sprite, current_life_rect)
            current_life_rect.move_ip(self.life_distance, 0)

    def damage(self, damage_pos):
        self.lives -= 1

        if self.lives == 0:
            self.game.restart()
