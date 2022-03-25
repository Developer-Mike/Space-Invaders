import pygame

import Enemy
from EventListener import EventListener
from RenderObject import RenderObject
from Shield import Shield


class Laser(RenderObject):
    speed = 10
    size = (4, 10)

    def __init__(self, game, pos):
        self.game = game
        game.render_objects.append(self)

        self.sprite = pygame.transform.scale(pygame.image.load("assets/shield.png"), self.size)
        self.rect = self.sprite.get_rect()
        self.rect = self.rect.move(pos)
        self.rect.x -= self.size[0] / 2

    def tick(self, surface):
        self.rect.move_ip(0, -self.speed)
        if self.rect.y + self.size[1] < 0:
            self.game.render_objects.remove(self)

        self.check_collision()
        surface.blit(self.sprite, self.rect)

    def check_collision(self):
        for render_object in self.game.render_objects:
            if type(render_object) is Enemy or type(render_object) is Shield:
                if self.rect.colliderect(render_object.rect):
                    self.game.render_objects.remove(self)
                    render_object.damage(self.rect)
