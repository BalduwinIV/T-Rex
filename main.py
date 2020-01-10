import os
import sys
import random
import pygame


pygame.init()
SIZE = WIDTH, HEIGHT = 1200, 300
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
FPS = 60
HI = [pygame.image.load("sprites/highscore/letter_h.png"), pygame.image.load("sprites/highscore/letter_i.png")]
with open('highscore.txt', 'r') as f:
    highscore = int(f.read())


def init_numbers():
    zero = pygame.image.load("sprites/numbers/number_0.png")
    one = pygame.image.load("sprites/numbers/number_1.png")
    two = pygame.image.load("sprites/numbers/number_2.png")
    three = pygame.image.load("sprites/numbers/number_3.png")
    four = pygame.image.load("sprites/numbers/number_4.png")
    five = pygame.image.load("sprites/numbers/number_5.png")
    six = pygame.image.load("sprites/numbers/number_6.png")
    seven = pygame.image.load("sprites/numbers/number_7.png")
    eight = pygame.image.load("sprites/numbers/number_8.png")
    nine = pygame.image.load("sprites/numbers/number_9.png")
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def init_highscore_numbers():
    zero = pygame.image.load("sprites/highscore/hi_0.png")
    one = pygame.image.load("sprites/highscore/hi_1.png")
    two = pygame.image.load("sprites/highscore/hi_2.png")
    three = pygame.image.load("sprites/highscore/hi_3.png")
    four = pygame.image.load("sprites/highscore/hi_4.png")
    five = pygame.image.load("sprites/highscore/hi_5.png")
    six = pygame.image.load("sprites/highscore/hi_6.png")
    seven = pygame.image.load("sprites/highscore/hi_7.png")
    eight = pygame.image.load("sprites/highscore/hi_8.png")
    nine = pygame.image.load("sprites/highscore/hi_9.png")
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def show_score(score):
    first = score // 10000
    second = (score // 1000) % 10
    third = (score // 100) % 10
    forth = (score // 10) % 10
    fifth = score % 10
    screen.blit(numbers[first], (WIDTH - 100, 10))
    screen.blit(numbers[second], (WIDTH - 80, 10))
    screen.blit(numbers[third], (WIDTH - 60, 10))
    screen.blit(numbers[forth], (WIDTH - 40, 10))
    screen.blit(numbers[fifth], (WIDTH - 20, 10))

    first = highscore // 10000
    second = (highscore // 1000) % 10
    third = (highscore // 100) % 10
    forth = (highscore // 10) % 10
    fifth = highscore % 10
    screen.blit(HI[0], (WIDTH - 270, 10))
    screen.blit(HI[1], (WIDTH - 250, 10))
    screen.blit(highscore_numbers[first], (WIDTH - 220, 10))
    screen.blit(highscore_numbers[second], (WIDTH - 200, 10))
    screen.blit(highscore_numbers[third], (WIDTH - 180, 10))
    screen.blit(highscore_numbers[forth], (WIDTH - 160, 10))
    screen.blit(highscore_numbers[fifth], (WIDTH - 140, 10))


class TRex:  # player class
    def __init__(self, pos):
        self.x_coord, self.y_coord = pos
        self.current_animation = rex_run
        self.animation_counter = 0
        self.timer = 0
        self.is_jump = False  # TODO

    def update(self):
        screen.blit(self.current_animation[self.animation_counter], (self.x_coord, self.y_coord))
        self.timer += 1  # delay between animations
        if self.timer >= 5:
            self.animation_counter += 1
            if self.animation_counter >= 2:
                self.animation_counter = 0
            self.timer = 0

    def jump(self):
        self.is_jump = True


class Barrier:  # bush class
    def __init__(self, x_coord, velocity):
        image_number = random.randint(1, 6)  # choosing random bush
        self.barrier_image = pygame.image.load(f'sprites/barriers/{image_number}.png')
        if image_number == 1 or image_number == 2 or image_number == 3:  # different bushes - different sizes
            self.y_coord = 200
        else:
            self.y_coord = 170
        self.x_coord = x_coord
        self.velocity = velocity

    def update(self):
        self.x_coord += self.velocity
        screen.blit(self.barrier_image, (self.x_coord, self.y_coord))

    def get_x(self):
        return self.x_coord


class Floor:  # road class
    def __init__(self, pos, velocity):
        self.image = pygame.image.load("sprites/floor.png")
        self.x_coord, self.y_coord = pos
        self.velocity = velocity

    def update(self):
        self.x_coord += self.velocity
        screen.blit(self.image, (self.x_coord, self.y_coord))

    def get_x(self):
        return self.x_coord


def update_highscore():
    '''getting highscore from file'''
    global highscore
    with open('highscore.txt', 'r') as f:
        highscore = int(f.read())


def set_highscore(score):
    '''changing highscore in file'''
    with open('highscore.txt', 'w') as f:
        f.write(str(score))


rex_startscreen = pygame.image.load("sprites/rex_startscreen.png")
rex_run = [pygame.image.load("sprites/rex_run_1.png"), pygame.image.load("sprites/rex_run_2.png")]
main_velocity = -10  # the whole map velocity
player = TRex((50, 176))
bush1 = Barrier(1300, main_velocity)
bush2 = Barrier(2000, main_velocity)  # initializing 2 bushes to avoid free spaces
main_floor = Floor((0, 250), main_velocity)
reserve_floor = Floor((2400, 250), main_velocity)
highscore_numbers = init_highscore_numbers()
numbers = init_numbers()
score = 0
timer = 0
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    timer += 1
    if timer >= 5:
        score += 1
        show_score(score)
        timer = 0

    main_floor.update()
    reserve_floor.update()
    bush1.update()
    bush2.update()
    if bush1.get_x() < -50:
        bush1 = Barrier(random.randint(1200, 1800), main_velocity)
    if bush2.get_x() < -50:
        bush2 = Barrier(random.randint(1200, 1800), main_velocity)
    if main_floor.get_x() < -2400:
        main_floor = Floor((2400, 250), main_velocity)
    if reserve_floor.get_x() < -2400:
        reserve_floor = Floor((2400, 250), main_velocity)

    player.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()