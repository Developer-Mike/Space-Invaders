import random
import pygame

from EnemyLaser import EnemyLaser
from RenderObject import RenderObject


class Enemy(RenderObject):
    size = (40, 30)
    shoot_probability = 5
    move_interval = 30  # 0.5sec
    move_distance_x = 20
    move_distance_y = 50
    move_x_bounds = (50, 1200)

    def __init__(self, game, pos, points):
        self.game = game
        self.points = points
        self.move_timer = 0
        self.move_direction = 1
        game.render_objects.append(self)

        self.open_sprite = pygame.transform.scale(pygame.image.load(
            f"assets/{points}_enemy_open.png"
        ), self.size)
        self.closed_sprite = pygame.transform.scale(pygame.image.load(
            f"assets/{points}_enemy_closed.png"
        ), self.size)
        self.open = True
        self.current_sprite = self.open_sprite

        self.rect = self.current_sprite.get_rect()
        self.rect = self.rect.move(pos)

    def tick(self, surface):
        self.move_timer += 1

        if (self.rect.centerx <= self.move_x_bounds[0] and self.move_direction == -1) or \
                (self.rect.centerx >= self.move_x_bounds[1] and self.move_direction == 1):
            for enemy in self.game.enemies:
                enemy.change_y()

        if self.move_timer >= self.move_interval:
            self.move_timer = 0

            self.current_sprite = self.closed_sprite if self.open else self.open_sprite
            self.open = not self.open

            self.rect.move_ip(self.move_distance_x * self.move_direction, 0)

            if random.randint(0, 100) < self.shoot_probability:
                EnemyLaser(self.game, (self.rect.centerx, self.rect.y + self.size[1]))

        surface.blit(self.current_sprite, self.rect)

    def damage(self, collision_pos):
        self.game.render_objects.remove(self)
        self.game.enemies.remove(self)

        self.game.score += self.points

    def change_y(self):
        self.move_direction = self.move_direction * -1
        self.rect.move_ip(0, self.move_distance_y)
