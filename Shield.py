import pygame
from EventListener import EventListener
from RenderObject import RenderObject


class Shield(RenderObject):
    size = (75, 50)

    def __init__(self, game, pos):
        game.render_objects.append(self)

        self.sprite = pygame.transform.scale(pygame.image.load("assets/shield.png"), self.size)
        self.rect = self.sprite.get_rect()
        self.rect = self.rect.move(pos)

    def tick(self, surface):
        surface.blit(self.sprite, self.rect)

    def damage(self, damage_pos):
        pass
