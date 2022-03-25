import pygame
from EventListener import EventListener
from RenderObject import RenderObject


class Enemy(RenderObject):
    size = (75, 50)

    def __init__(self, game, pos):
        game.render_objects.append(self)

        self.sprite = pygame.transform.scale(pygame.image.load("assets/shield.png"), self.size)
        self.rect = self.sprite.get_rect()
        self.rect = self.rect.move(pos)

    def tick(self, surface):
        new_rect = self.rect.copy()
        new_rect.move_ip(-self.size[0] / 2, -self.size[1] / 2)
        surface.blit(self.sprite, new_rect)

    def damage(self, collision_pos):
        pass
