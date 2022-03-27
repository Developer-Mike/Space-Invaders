import pygame

from Player import Player
from RenderObject import RenderObject
from Shield import Shield


class EnemyLaser(RenderObject):
    speed = 5
    size = (4, 10)

    def __init__(self, game, pos):
        self.game = game
        game.render_objects.append(self)

        self.sprite = pygame.transform.scale(pygame.image.load("assets/missle_white.png"), self.size)
        self.rect = self.sprite.get_rect()
        self.rect = self.rect.move(pos)
        self.rect.move_ip(-self.size[0] / 2, -self.size[1])

    def tick(self, surface):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > self.game.screen_size[1]:
            self.game.render_objects.remove(self)

        self.check_collision()
        surface.blit(self.sprite, self.rect)

    def check_collision(self):
        for render_object in self.game.render_objects:
            if type(render_object) is Player or type(render_object) is Shield:
                if self.rect.colliderect(render_object.rect):
                    self.game.render_objects.remove(self)
                    render_object.damage(self.rect)
