import math
import pygame


class Pendulum:
    def __init__(self, pivotx=0, pivoty=0, m=1, l=200, a=math.pi/2, g=1, color='blue'):
        self.pivot = (pivotx, pivoty)
        self.m = m
        self.l = l
        self.a = a
        self.g = g
        self.clr = color

        self.x = 0
        self.y = 0

        self.av = 0
        self.traj = []

    def step(self):
        acc = (- self.g / self.l) * math.sin(self.a)
        self.av += acc
        self.av *= 0.995  # friction

        self.a += self.av
        self.x = self.pivot[0] + self.l * math.sin(self.a)
        self.y = self.pivot[1] + self.l * math.cos(self.a)

    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 255),
                         self.pivot, (self.x, self.y))
        pygame.draw.circle(surface, self.clr, (self.x, self.y), 15)


def init_surface(size, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    surface = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    return surface, clock


def run():
    width, height = 800, 800
    fps = 60
    surface, clock = init_surface((width, height), 'Pendulum')

    length = [200 + 20 * i for i in range(10)]
    colors = ["Turquoise", "White", "Red", "Green", "Blue",
              "Yellow", "Cyan", "Magenta", "Orange", "Purple"]

    pendulums = [Pendulum(pivotx=width // 2, pivoty=height //
                          2, l=l, color=c) for l, c in zip(length, colors)]

    stop = False
    while not stop:
        clock.tick(fps)
        surface.fill((0, 0, 0))  # black

        for event in pygame.event.get():
            stop = event.type == pygame.QUIT

        for i in range(len(pendulums)):
            pendulums[i].step()
            pendulums[i].draw(surface=surface)
        pygame.display.flip()

    pygame.quit()


run()
