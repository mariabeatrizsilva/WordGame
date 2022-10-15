import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Player(pygame.sprite.Sprite):
    """
   Player class, subclass of Sprite
    """

    def __init__(self):
        # Call the super constructor
        super().__init__()

        self.image = pygame.image.load("knight_walking.gif").convert()
        self.image = pygame.transform.scale(self.image, (90, 90))

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, 400)


class Background:
    """
    Background class, loops background infinitely
    """
    # load bg image and set coordinates
    def __init__(self):
        self.image = pygame.image.load("bgtester.png").convert()
        self.rect = self.image.get_rect()

        self.x1 = 0
        self.y1 = 0

        self.x2 = self.rect.width
        self.y2 = 0

        self.speed = 1

    # update coordinates as bg moves
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 <= -self.rect.width:
            self.x1 = self.rect.width

        if self.x2 <= self.rect.width:
            self.x2 = self.rect.width

    # display overlayed bg image
    def render(self):
        screen.blit(self.image, (self.x1, self.y1))
        screen.blit(self.image, (self.x2, self.y2))

# pygame init
pygame.init()

# Set the height and width of the screen
width = 700
height = 600
screen = pygame.display.set_mode([width, height])

# every block BUT player
block_list = pygame.sprite.Group()

# every block including player
sprites_list = pygame.sprite.Group()

# create player, add to sprite list
player = Player()
sprites_list.add(player)

# create background
bg = Background()

# on/off button
on = True


# -------- PROGRAM HERE -----------
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    # background image
    bg.update()
    bg.render()

    # draw sprites
    sprites_list.draw(screen)

    # display screen
    pygame.display.flip()

pygame.quit()
