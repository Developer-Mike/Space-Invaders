import pygame
from EventListener import EventListener
from Player import Player
from RenderObject import RenderObject
from Shield import Shield

fps = 60
screen_size = (1250, 750)


class Game:
    def __init__(self):
        self.event_listeners: list[EventListener] = []
        self.render_objects: list[RenderObject] = []

        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(screen_size)

        # Init objects
        self.player = Player(self)
        self.shields = [Shield(self, (x, 550)) for x in range(125, screen_size[0] + 1, 300)]

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

