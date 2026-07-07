import pygame, sys, time, random
pygame.init()
screen = pygame.display.set_mode([1200, 800])
screen.fill([255,255,255])
pygame.display.flip()



class Star:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 800)
        self.sx = random.randint(3, 8)
        self.sy = random.randint(3, 8)
        self.t = 0.0001
        self.imagepath = "./2b50_color.png"
    def move1(self):
        if (screen.get_width() + 10 < self.x):
            self.x = -17
        if (screen.get_height() + 10 < self.y):
            self.y = -17
        photo = pygame.image.load(self.imagepath)
        # pygame.draw.rect(screen, [255, 255, 255], [self.x - self.sx, self.y - self.sy, 17, 17], 0)
        screen.blit(photo, [self.x, self.y])
        # pygame.display.flip()
        self.x += self.sx
        self.y += self.sy
    def move2(self):
        if (screen.get_width() < self.x or self.x < 0):
            self.sx = - self.sx
        if (screen.get_height() < self.y or self.y < 0):
            self.sy = - self.sy
        photo = pygame.image.load(self.imagepath)
        # pygame.draw.rect(screen, [255, 255, 255], [self.x - self.sx, self.y - self.sy, 17, 17], 0)
        screen.blit(photo, [self.x, self.y])
        # pygame.display.flip()
        self.x += self.sx
        self.y += self.sy

# randomlist = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]


for i in range(1, 65):
    globals()[f'star{i}'] = Star()
while 1:
    for i in range(1, 65):
        globals()[f'star{i}'].move1()
    pygame.display.flip()
    screen.fill([255, 255, 255])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if running == False:
                pygame.quit()
