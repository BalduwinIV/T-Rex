import os
import sys
import pygame


pygame.init()
SIZE = WIDTH, HEIGHT = 1200, 300
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
FPS = 10
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


def update_highscore():
    global highscore
    with open('highscore.txt', 'r') as f:
        highscore = int(f.read())


def set_highscore(score):
    with open('highscore.txt', 'w') as f:
        f.write(str(score))


highscore_numbers = init_highscore_numbers()
numbers = init_numbers()
number = 0
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    show_score(number)
    number += 1
    if number % 100 == 0:
        set_highscore(number)
        update_highscore()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()