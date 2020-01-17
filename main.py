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


def show_score(score, surface):
    # Checkpoint effect
    # ------------------------------------------------------------------------------------------------------------------
    if score % 100 <= 20 and score > 20:
        if (score % 100 > 0 and score % 100 <= 5) or (score % 100 > 10 and score % 100 <= 15):
            first = score // 10000
            second = (score // 1000) % 10
            third = (score // 100) % 10
            forth = 0
            fifth = 0
            surface.blit(NUMBERS[first], (WIDTH - 100, 10))
            surface.blit(NUMBERS[second], (WIDTH - 80, 10))
            surface.blit(NUMBERS[third], (WIDTH - 60, 10))
            surface.blit(NUMBERS[forth], (WIDTH - 40, 10))
            surface.blit(NUMBERS[fifth], (WIDTH - 20, 10))

            first = highscore // 10000
            second = (highscore // 1000) % 10
            third = (highscore // 100) % 10
            forth = (highscore // 10) % 10
            fifth = highscore % 10
            surface.blit(HI[0], (WIDTH - 270, 10))
            surface.blit(HI[1], (WIDTH - 250, 10))
            surface.blit(HIGHSCORE_NUMBERS[first], (WIDTH - 220, 10))
            surface.blit(HIGHSCORE_NUMBERS[second], (WIDTH - 200, 10))
            surface.blit(HIGHSCORE_NUMBERS[third], (WIDTH - 180, 10))
            surface.blit(HIGHSCORE_NUMBERS[forth], (WIDTH - 160, 10))
            surface.blit(HIGHSCORE_NUMBERS[fifth], (WIDTH - 140, 10))
        else:
            first = highscore // 10000
            second = (highscore // 1000) % 10
            third = (highscore // 100) % 10
            forth = (highscore // 10) % 10
            fifth = highscore % 10
            surface.blit(HI[0], (WIDTH - 270, 10))
            surface.blit(HI[1], (WIDTH - 250, 10))
            surface.blit(HIGHSCORE_NUMBERS[first], (WIDTH - 220, 10))
            surface.blit(HIGHSCORE_NUMBERS[second], (WIDTH - 200, 10))
            surface.blit(HIGHSCORE_NUMBERS[third], (WIDTH - 180, 10))
            surface.blit(HIGHSCORE_NUMBERS[forth], (WIDTH - 160, 10))
            surface.blit(HIGHSCORE_NUMBERS[fifth], (WIDTH - 140, 10))
    # ------------------------------------------------------------------------------------------------------------------
    else:
        first = score // 10000
        second = (score // 1000) % 10
        third = (score // 100) % 10
        forth = (score // 10) % 10
        fifth = score % 10
        surface.blit(NUMBERS[first], (WIDTH - 100, 10))
        surface.blit(NUMBERS[second], (WIDTH - 80, 10))
        surface.blit(NUMBERS[third], (WIDTH - 60, 10))
        surface.blit(NUMBERS[forth], (WIDTH - 40, 10))
        surface.blit(NUMBERS[fifth], (WIDTH - 20, 10))

        first = highscore // 10000
        second = (highscore // 1000) % 10
        third = (highscore // 100) % 10
        forth = (highscore // 10) % 10
        fifth = highscore % 10
        surface.blit(HI[0], (WIDTH - 270, 10))
        surface.blit(HI[1], (WIDTH - 250, 10))
        surface.blit(HIGHSCORE_NUMBERS[first], (WIDTH - 220, 10))
        surface.blit(HIGHSCORE_NUMBERS[second], (WIDTH - 200, 10))
        surface.blit(HIGHSCORE_NUMBERS[third], (WIDTH - 180, 10))
        surface.blit(HIGHSCORE_NUMBERS[forth], (WIDTH - 160, 10))
        surface.blit(HIGHSCORE_NUMBERS[fifth], (WIDTH - 140, 10))


class TRex(pygame.sprite.Sprite):  # player class
    def __init__(self, pos, group):
        super().__init__(group)
        self.x_coord, self.y_coord = pos
        self.width = 88
        self.height = 94
        self.current_animation = REX_RUN
        self.sit_animation = REX_DOWN
        self.animation_counter = 0
        self.image = self.current_animation[self.animation_counter]
        self.rect = self.current_animation[self.animation_counter].get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.x_coord
        self.rect.y = self.y_coord
        self.is_jump = False
        self.is_sit = False
        self.jump_vel = 0
        self.timer = 0

    def update(self):
        if self.is_jump:
            if self.jump_vel <= 18:  # jump height
                self.y_coord += self.jump_vel
                self.rect.y += self.jump_vel
                self.jump_vel += 1
                if self.jump_vel <= 18 and self.is_sit:  # to fall faster
                    self.y_coord += self.jump_vel
                    self.rect.y += self.jump_vel
                    self.jump_vel += 1
            else:
                self.is_jump = False
                self.current_animation = REX_RUN
                self.animation_counter = 0
                self.image = self.current_animation[self.animation_counter]
        elif self.is_sit:
            self.timer += 1
            if self.timer >= 5:
                self.animation_counter += 1
                if self.animation_counter >= 2:
                    self.animation_counter = 0
                self.timer = 0
                self.image = self.sit_animation[self.animation_counter]
                self.y_coord = 210  # rex_down sprite is lower
                self.rect.y = 210
        else:
            self.timer += 1  # delay between animations
            if self.timer >= 5:
                self.animation_counter += 1
                if self.animation_counter >= 2:
                    self.animation_counter = 0
                self.timer = 0
                self.image = self.current_animation[self.animation_counter]
                self.y_coord = 176
                self.rect.y = 176

    def is_collided_with(self, sprite):
        if pygame.sprite.collide_mask(self, sprite):
            return True
        return False

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.jump_vel = -18  # jump height
            self.current_animation = REX_JUMP
            self.image = self.current_animation
            self.rect = self.current_animation.get_rect()
            self.rect.x = self.x_coord
            self.rect.y = self.y_coord

    def jump_status(self):
        return self.is_jump

    def sit(self, status):
        self.is_sit = status


class Barrier(pygame.sprite.Sprite):  # bush class
    def __init__(self, x_coord, velocity, group):
        super().__init__(group)
        image_number = random.randint(1, 6)  # choosing random bush
        self.barrier_image = BARRIERS[image_number - 1]
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


class FlyEnemy(pygame.sprite.Sprite):
    def __init__(self, x_coord, velocity, group):
        super().__init__(group)
        self.animation = ENEMY
        self.animation_counter = 0
        self.image = self.animation[self.animation_counter]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = random.choice([120, 140, 190])
        self.rect.x = x_coord
        self.velocity = velocity
        self.timer = 1

    def update(self):
        self.timer += 1
        if self.timer >= 10:
            self.animation_counter += 1
            if self.animation_counter >= 2:
                self.animation_counter = 0
            self.image = self.animation[self.animation_counter]
            self.timer = 1
        self.rect.x += self.velocity

    def get_x(self):
        return self.rect.x

    def change_velocity(self, velocity):
        self.velocity = velocity


class Floor(pygame.sprite.Sprite):  # road class
    def __init__(self, pos, velocity, group):
        super().__init__(group)
        self.image = FLOOR
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
        self.image = CLOUD
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
    current_animation = REX_RUN
    rex = REX_JUMP
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
        screen.blit(FLOOR, (0, 250))
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


# Sound effects
# ----------------------------------------------------------------------------------------------------------------------
CHECKPOINT_SOUND = pygame.mixer.Sound("sounds/checkPoint.wav")
DIE_SOUND = pygame.mixer.Sound("sounds/die.wav")
JUMP_SOUND = pygame.mixer.Sound("sounds/jump.wav")
# ----------------------------------------------------------------------------------------------------------------------
# Sprites
# ----------------------------------------------------------------------------------------------------------------------
HI = [pygame.image.load("sprites/highscore/letter_h.png"), pygame.image.load("sprites/highscore/letter_i.png")]
REX_RUN = [pygame.image.load("sprites/rex_run_1.png"), pygame.image.load("sprites/rex_run_2.png")]
REX_DOWN = [pygame.image.load("sprites/rex_down_1.png"), pygame.image.load("sprites/rex_down_2.png")]
REX_JUMP = pygame.image.load("sprites/rex_jump.png")
FLOOR = pygame.image.load("sprites/floor.png")
CLOUD = pygame.image.load("sprites/cloud.png")
BARRIERS = [pygame.image.load('sprites/barriers/1.png'), pygame.image.load('sprites/barriers/2.png'),
            pygame.image.load('sprites/barriers/3.png'), pygame.image.load('sprites/barriers/4.png'),
            pygame.image.load('sprites/barriers/5.png'), pygame.image.load('sprites/barriers/6.png')]
ENEMY = [pygame.image.load('sprites/barriers/enemy_1.png'), pygame.image.load('sprites/barriers/enemy_2.png')]
GAME_OVER = pygame.image.load("sprites/gameover.png")
RESTART_BUTTON = pygame.image.load("sprites/restart_button.png")
HIGHSCORE_NUMBERS = init_highscore_numbers()
NUMBERS = init_numbers()
# ----------------------------------------------------------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------------------------------------------------------
with open('highscore.txt', 'r') as f:
    highscore = int(f.read())

FPS = 60
main_velocity = -12  # the whole map velocity
FLYING_ENEMY_SPAWN_SCORE = 300  # score when FlyEnemy spawns
score = 0
timer = 0
CLOUD_SPEED = -1
running = True
# ----------------------------------------------------------------------------------------------------------------------
# Class objects
# ----------------------------------------------------------------------------------------------------------------------
FOREGROUND = pygame.sprite.Group()
BACKGROUND = pygame.sprite.Group()

player = TRex((50, 176), FOREGROUND)
bush1 = Barrier(2300, main_velocity, FOREGROUND)
bush2 = Barrier(3000, main_velocity, FOREGROUND)  # initializing 2 bushes to avoid free spaces
main_floor = Floor((0, 250), main_velocity, BACKGROUND)
reserve_floor = Floor((2400, 250), main_velocity, BACKGROUND)  # same
cloud1 = Cloud((random.randint(100, 1000), random.randint(30, 80)), CLOUD_SPEED, BACKGROUND)
cloud2 = Cloud((random.randint(600, 1600), random.randint(30, 80)), CLOUD_SPEED, BACKGROUND)
cloud3 = Cloud((random.randint(1000, 2000), random.randint(30, 80)), CLOUD_SPEED, BACKGROUND)
cloud4 = Cloud((random.randint(1500, 2500), random.randint(30, 80)), CLOUD_SPEED, BACKGROUND)
# ----------------------------------------------------------------------------------------------------------------------
start_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32 or event.key == 273:  # SPACE or UP
                JUMP_SOUND.play()
                player.jump()
            if event.key == 274:  # DOWN
                player.sit(True)
        if event.type == pygame.KEYUP:
            if event.key == 274:  # DOWN
                player.sit(False)

    # Updating score
    # ------------------------------------------------------------------------------------------------------------------
    timer += 1
    if timer >= 5:
        score += 1
        if score > highscore:
            highscore = score
        # Play sound
        # --------------------------------------------------------------------------------------------------------------
        if score % 100 == 0 and score > 0:
            CHECKPOINT_SOUND.play()
        # --------------------------------------------------------------------------------------------------------------
        timer = 0

        # Updating velocity
        # --------------------------------------------------------------------------------------------------------------
        if score % 200 == 0 and score <= 1000:
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
        BACKGROUND.remove(cloud1)
        cloud1 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), CLOUD_SPEED, BACKGROUND)
    if cloud2.get_x() < -92:
        BACKGROUND.remove(cloud2)
        cloud2 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), CLOUD_SPEED, BACKGROUND)
    if cloud3.get_x() < -92:
        BACKGROUND.remove(cloud3)
        cloud3 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), CLOUD_SPEED, BACKGROUND)
    if cloud4.get_x() < -92:
        BACKGROUND.remove(cloud4)
        cloud4 = Cloud((random.randint(1200, 1800), random.randint(30, 70)), CLOUD_SPEED, BACKGROUND)
    # ------------------------------------------------------------------------------------------------------------------
    # Spawning bushes
    # ------------------------------------------------------------------------------------------------------------------
    if bush1.get_x() < -150:
        FOREGROUND.remove(bush1)
        if score > FLYING_ENEMY_SPAWN_SCORE:
            random_number = random.randint(1, 10)
            if random_number == 7:  # happy number
                bush1 = FlyEnemy(random.randint(1200, 1400), main_velocity, FOREGROUND)
            else:
                bush1 = Barrier(random.randint(1200, 1400), main_velocity, FOREGROUND)
        else:
            bush1 = Barrier(random.randint(1200, 1400), main_velocity, FOREGROUND)
    if bush2.get_x() < -150:
        FOREGROUND.remove(bush2)
        if score > FLYING_ENEMY_SPAWN_SCORE:
            random_number = random.randint(1, 10)
            if random_number == 7:  # happy number
                bush2 = FlyEnemy(random.randint(1200, 1400), main_velocity, FOREGROUND)
            else:
                bush2 = Barrier(random.randint(1200, 1400), main_velocity, FOREGROUND)
        else:
            bush2 = Barrier(random.randint(1200, 1400), main_velocity, FOREGROUND)
    # ------------------------------------------------------------------------------------------------------------------
    # Spawning floor
    # ------------------------------------------------------------------------------------------------------------------
    if main_floor.get_x() < -2400:
        BACKGROUND.remove(main_floor)
        main_floor = Floor((2400, 250), main_velocity, BACKGROUND)
    if reserve_floor.get_x() < -2400:
        BACKGROUND.remove(reserve_floor)
        reserve_floor = Floor((2400, 250), main_velocity, BACKGROUND)
    # ------------------------------------------------------------------------------------------------------------------
    # Checking collision
    # ------------------------------------------------------------------------------------------------------------------
    if player.is_collided_with(bush1) or player.is_collided_with(bush2):
        # Sound playing
        # --------------------------------------------------------------------------------------------------------------
        DIE_SOUND.play()
        # --------------------------------------------------------------------------------------------------------------
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
            BACKGROUND.draw(screen)
            FOREGROUND.draw(screen)
            screen.blit(GAME_OVER, (410, 79))
            screen.blit(RESTART_BUTTON, (564, 136))
            # ----------------------------------------------------------------------------------------------------------
            pygame.display.flip()
        # Updating variables
        # --------------------------------------------------------------------------------------------------------------
        main_velocity = -12  # the whole map velocity
        score = 0
        timer = 0
        # --------------------------------------------------------------------------------------------------------------
        # Removing objects from groups
        # --------------------------------------------------------------------------------------------------------------
        FOREGROUND.remove(player)
        FOREGROUND.remove(bush1)
        FOREGROUND.remove(bush2)
        # --------------------------------------------------------------------------------------------------------------
        # Initializing new objects
        # --------------------------------------------------------------------------------------------------------------
        player = TRex((50, 176), FOREGROUND)
        bush1 = Barrier(1300, main_velocity, FOREGROUND)
        bush2 = Barrier(2000, main_velocity, FOREGROUND)
        BACKGROUND.remove(main_floor)
        BACKGROUND.remove(reserve_floor)
        main_floor = Floor((0, 250), main_velocity, BACKGROUND)
        reserve_floor = Floor((2400, 250), main_velocity, BACKGROUND)
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
    show_score(score, screen)
    BACKGROUND.draw(screen)
    FOREGROUND.draw(screen)
    # ------------------------------------------------------------------------------------------------------------------
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()