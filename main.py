import random
import pygame


pygame.init()
SIZE = WIDTH, HEIGHT = 1200, 300
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


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


class TRex(pygame.sprite.Sprite):  # player class
    def __init__(self, pos, group):
        super().__init__(group)
        self.x_coord, self.y_coord = pos
        self.width = 88
        self.height = 94
        self.current_animation = rex_run
        self.animation_counter = 0
        self.image = self.current_animation[self.animation_counter]
        self.rect = self.current_animation[self.animation_counter].get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.x_coord
        self.rect.y = self.y_coord
        self.timer = 0
        self.is_jump = False
        self.jump_vel = 0

    def update(self):
        if self.is_jump:
            if self.jump_vel <= 18:
                self.y_coord += self.jump_vel
                self.rect.y += self.jump_vel
                self.jump_vel += 1
            else:
                self.is_jump = False
                self.current_animation = rex_run
                self.animation_counter = 0
                self.image = self.current_animation[self.animation_counter]
        else:
            self.timer += 1  # delay between animations
            if self.timer >= 5:
                self.animation_counter += 1
                if self.animation_counter >= 2:
                    self.animation_counter = 0
                self.timer = 0
                self.image = self.current_animation[self.animation_counter]

    def is_collided_with(self, sprite):
        if pygame.sprite.collide_mask(self, sprite):
            return True
        return False

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.jump_vel = -18
            self.current_animation = pygame.image.load("sprites/rex_jump.png")
            self.image = self.current_animation
            self.rect = self.current_animation.get_rect()
            self.rect.x = self.x_coord
            self.rect.y = self.y_coord

    def jump_status(self):
        return self.is_jump


class Barrier(pygame.sprite.Sprite):  # bush class
    def __init__(self, x_coord, velocity, group):
        super().__init__(group)
        image_number = random.randint(1, 6)  # choosing random bush
        self.barrier_image = pygame.image.load(f'sprites/barriers/{image_number}.png')
        self.image = self.barrier_image
        self.rect = self.barrier_image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        if image_number == 1 or image_number == 2 or image_number == 3:  # different bushes - different sizes
            self.y_coord = 200
        else:
            self.y_coord = 170
        if image_number == 1:
            self.width = 102
            self.height = 70
        elif image_number == 2:
            self.width = 68
            self.height = 70
        elif image_number == 3:
            self.width = 34
            self.height = 70
        elif image_number == 4:
            self.width = 150
            self.height = 100
        elif image_number == 5:
            self.width = 100
            self.height = 100
        elif image_number == 6:
            self.width = 50
            self.height = 100
        self.x_coord = x_coord
        self.velocity = velocity
        self.rect.x = self.x_coord
        self.rect.y = self.y_coord

    def update(self):
        self.x_coord += self.velocity
        self.rect.x = self.x_coord

    def get_x(self):
        return self.x_coord

    def get_rect(self):
        return [self.x_coord, self.y_coord, self.width, self.height]

    def change_velocity(self, velocity):
        self.velocity = velocity


class Floor(pygame.sprite.Sprite):  # road class
    def __init__(self, pos, velocity, group):
        super().__init__(group)
        self.image = pygame.image.load("sprites/floor.png")
        self.x_coord, self.y_coord = pos
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x_coord, self.y_coord
        self.velocity = velocity

    def update(self):
        self.x_coord += self.velocity
        self.rect.x += self.velocity

    def get_x(self):
        return self.x_coord

    def change_velocity(self, velocity):
        self.velocity = velocity


class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, group):
        super().__init__(group)
        self.image = pygame.image.load("sprites/cloud.png")
        self.x_coord, self.y_coord = pos
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x_coord, self.y_coord
        self.velocity = velocity

    def update(self):
        self.x_coord += self.velocity
        self.rect.x += self.velocity

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


def start_screen():
    # Sprites
    # ------------------------------------------------------------------------------------------------------------------
    floor = pygame.image.load("sprites/floor.png")
    current_animation = rex_run
    rex = rex_jump
    # ------------------------------------------------------------------------------------------------------------------
    # Variables
    # ------------------------------------------------------------------------------------------------------------------
    running = True
    is_exit = False
    timer = 0
    animation_counter = 0
    rect_x = 100
    rect_vel = 0
    rex_x = 0
    rex_y = 176
    rex_vel = 0
    open_space = False
    is_jump = False
    jump_var = -18
    # ------------------------------------------------------------------------------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                is_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == 273 or event.key == 32:
                    is_jump = True
                    jump_var = -18
        if is_jump:
            if jump_var <= 18:
                rex_y += jump_var
                jump_var += 1
            else:
                is_jump = False
                open_space = True
        if open_space:
            rex_vel = 1
            rect_vel = 20
        # Animation
        # --------------------------------------------------------------------------------------------------------------
        timer += 1
        if timer >= 5:
            animation_counter += 1
            if animation_counter >= 2:
                animation_counter = 0
            timer = 0
        # --------------------------------------------------------------------------------------------------------------
        # Drawing
        # --------------------------------------------------------------------------------------------------------------
        screen.fill((255, 255, 255))
        screen.blit(floor, (0, 250))
        pygame.draw.rect(screen, (255, 255, 255), (rect_x, 200, 1200, 200))
        if not open_space:
            screen.blit(rex, (rex_x, rex_y))
        else:
            screen.blit(current_animation[animation_counter], (rex_x, rex_y))
        # --------------------------------------------------------------------------------------------------------------
        # Moving TRex
        # --------------------------------------------------------------------------------------------------------------
        if rex_x < 50:
            rex_x += rex_vel
        else:
            running = False
        # --------------------------------------------------------------------------------------------------------------
        # Moving map
        # --------------------------------------------------------------------------------------------------------------
        rect_x += rect_vel
        # --------------------------------------------------------------------------------------------------------------
        pygame.display.flip()
        clock.tick(FPS)
    if is_exit:
        pygame.quit()


# Sprites
# ----------------------------------------------------------------------------------------------------------------------
FPS = 60
HI = [pygame.image.load("sprites/highscore/letter_h.png"), pygame.image.load("sprites/highscore/letter_i.png")]
rex_run = [pygame.image.load("sprites/rex_run_1.png"), pygame.image.load("sprites/rex_run_2.png")]
rex_down = [pygame.image.load("sprites/rex_down_1.png"), pygame.image.load("sprites/rex_down_2.png")]
rex_jump = pygame.image.load("sprites/rex_jump.png")
game_over = pygame.image.load("sprites/gameover.png")
restart_button = pygame.image.load("sprites/restart_button.png")
highscore_numbers = init_highscore_numbers()
numbers = init_numbers()
# ----------------------------------------------------------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------------------------------------------------------
with open('highscore.txt', 'r') as f:
    highscore = int(f.read())

main_velocity = -8  # the whole map velocity
score = 0
timer = 0
cloud_speed = -1
running = True
# ----------------------------------------------------------------------------------------------------------------------
# Class objects
# ----------------------------------------------------------------------------------------------------------------------
foreground = pygame.sprite.Group()
background = pygame.sprite.Group()

player = TRex((50, 176), foreground)
bush1 = Barrier(1300, main_velocity, foreground)
bush2 = Barrier(2000, main_velocity, foreground)  # initializing 2 bushes to avoid free spaces
main_floor = Floor((0, 250), main_velocity, background)
reserve_floor = Floor((2400, 250), main_velocity, background)  # same
cloud1 = Cloud((random.randint(100, 1000), random.randint(30, 80)), cloud_speed, background)
cloud2 = Cloud((random.randint(600, 1600), random.randint(30, 80)), cloud_speed, background)
cloud3 = Cloud((random.randint(1000, 2000), random.randint(30, 80)), cloud_speed, background)
cloud4 = Cloud((random.randint(1500, 2500), random.randint(30, 80)), cloud_speed, background)
# ----------------------------------------------------------------------------------------------------------------------
start_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32 or event.key == 273:
                player.jump()

    # Updating score
    # ------------------------------------------------------------------------------------------------------------------
    timer += 1
    if timer >= 5:
        score += 1
        if score > highscore:
            highscore = score
        timer = 0

        # Updating velocity
        # ---------------------------------------------------------------------------------------------------------------
        if score % 100 == 0 and score <= 500:
            main_velocity -= 1
            bush1.change_velocity(main_velocity)
            bush2.change_velocity(main_velocity)
            main_floor.change_velocity(main_velocity)
            reserve_floor.change_velocity(main_velocity)
        # --------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # Spawning clouds
    # ------------------------------------------------------------------------------------------------------------------
    if cloud1.get_x() < -92:
        foreground.remove(cloud1)
        cloud1 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), cloud_speed, foreground)
    if cloud2.get_x() < -92:
        foreground.remove(cloud2)
        cloud2 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), cloud_speed, foreground)
    if cloud3.get_x() < -92:
        foreground.remove(cloud3)
        cloud3 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), cloud_speed, foreground)
    if cloud4.get_x() < -92:
        foreground.remove(cloud4)
        cloud4 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), cloud_speed, foreground)
    # ------------------------------------------------------------------------------------------------------------------
    # Spawning bushes
    # ------------------------------------------------------------------------------------------------------------------
    if bush1.get_x() < -150:
        foreground.remove(bush1)
        bush1 = Barrier(random.randint(1200, 1400), main_velocity, foreground)
    if bush2.get_x() < -150:
        foreground.remove(bush2)
        bush2 = Barrier(random.randint(1200, 1400), main_velocity, foreground)
    # ------------------------------------------------------------------------------------------------------------------
    # Spawning floor
    # ------------------------------------------------------------------------------------------------------------------
    if main_floor.get_x() < -2400:
        background.remove(main_floor)
        main_floor = Floor((2400, 250), main_velocity, background)
    if reserve_floor.get_x() < -2400:
        background.remove(reserve_floor)
        reserve_floor = Floor((2400, 250), main_velocity, background)
    # ------------------------------------------------------------------------------------------------------------------
    # Checking collision
    # ------------------------------------------------------------------------------------------------------------------
    if player.is_collided_with(bush1) or player.is_collided_with(bush2):
        # Updating highscore
        # --------------------------------------------------------------------------------------------------------------
        if score >= highscore:
            set_highscore(score)
        # --------------------------------------------------------------------------------------------------------------
        is_showing = True
        while is_showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    is_showing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_showing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == 32 or event.key == 273 or event.key == 274:
                        is_showing = False
            # Drawing
            # ----------------------------------------------------------------------------------------------------------
            background.draw(screen)
            foreground.draw(screen)
            screen.blit(game_over, (410, 79))
            screen.blit(restart_button, (564, 136))
            # ----------------------------------------------------------------------------------------------------------
            pygame.display.flip()
        # Updating variables
        # --------------------------------------------------------------------------------------------------------------
        main_velocity = -8  # the whole map velocity
        score = 0
        timer = 0
        # --------------------------------------------------------------------------------------------------------------
        # Removing objects from groups
        # --------------------------------------------------------------------------------------------------------------
        foreground.remove(player)
        foreground.remove(bush1)
        foreground.remove(bush2)
        # --------------------------------------------------------------------------------------------------------------
        # Initializing new objects
        # --------------------------------------------------------------------------------------------------------------
        player = TRex((50, 176), foreground)
        bush1 = Barrier(1300, main_velocity, foreground)
        bush2 = Barrier(2000, main_velocity, foreground)
        background.remove(main_floor)
        background.remove(reserve_floor)
        main_floor = Floor((0, 250), main_velocity, background)
        reserve_floor = Floor((2400, 250), main_velocity, background)
        # --------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # Updating positions
    # ------------------------------------------------------------------------------------------------------------------
    cloud1.update()
    cloud2.update()
    cloud3.update()
    cloud4.update()
    main_floor.update()
    reserve_floor.update()
    bush1.update()
    bush2.update()
    player.update()
    # ------------------------------------------------------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------------------------------------------------------
    screen.fill((255, 255, 255))
    show_score(score)
    background.draw(screen)
    foreground.draw(screen)
    # ------------------------------------------------------------------------------------------------------------------
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()