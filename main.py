import pygame

from Enemy import Enemy
from EventListener import EventListener
from Player import Player
from RenderObject import RenderObject
from Shield import Shield

fps = 60


class Game:
    screen_size = (1250, 750)

    def __init__(self):
        self.event_listeners: list[EventListener] = []
        self.render_objects: list[RenderObject] = []

        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.screen_size)

        # Init objects
        self.player = Player(self)
        self.shields = [Shield(self, (x, 550)) for x in range(125, self.screen_size[0] + 1, 300)]

        enemy_y = 100
        self.enemies = []
        for score in (30, 20, 20, 10, 10):
            self.enemies.extend([Enemy(self, (x, enemy_y), score) for x in range(200, self.screen_size[0] - 200, 100)])
            enemy_y += 60

        while True:
            self.tick()

            pygame.display.update()
            self.clock.tick(fps)

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            for event_listener in self.event_listeners:
                event_listener.on_event(event)

        self.surface.fill((0, 0, 0))

        for render_object in self.render_objects:
            render_object.tick(self.surface)


if __name__ == '__main__':
    Game()

