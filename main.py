import pygame
import button
import level
import cat as felines
from pygame import mixer
import game_element


mixer.init()
IS_MUSIC_PLAYING = False

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

PIXELS = {'row-space': 20, 'col-space': 20, 'cat-height': 80, 'cat-x': 200, 'level-height-center': 350,
          'level-width-center': 500, 'gate-width': 100, 'cat-width': 85}

CLOCK = pygame.time.Clock()
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Menu')

IMAGES = {}
BUTTONS = {}

RUNNING = True
A_BUTTON_WAS_CLICKED = False
CURRENT_LEVEL = None
CURRENT_LEVEL_WAS_DRAWN = False
ACTIVE_SCREEN = 'menu'

LEVELS = [1, 2, 3, 4, 5, 6, 7, 8]
MOVING_SPRITES = pygame.sprite.Group()


def init_variables():
    global IMAGES, BUTTONS

    IMAGES['options'] = pygame.image.load('assets/buttons/options_button_v2.png').convert_alpha()
    IMAGES['play'] = pygame.image.load('assets/buttons/play_button.png').convert_alpha()
    IMAGES['quit'] = pygame.image.load('assets/buttons/quit_button.png').convert_alpha()
    IMAGES['help'] = pygame.image.load('assets/buttons/help_button.png').convert_alpha()
    IMAGES['back'] = pygame.image.load('assets/buttons/back_button.png').convert_alpha()
    IMAGES['menu'] = pygame.image.load('assets/buttons/menu_button.png').convert_alpha()
    IMAGES['sound'] = pygame.image.load('assets/buttons/sound_button.png').convert_alpha()
    IMAGES['menu_bg'] = pygame.image.load('assets/backgrounds/main_background.png').convert_alpha()
    IMAGES['level_bg'] = pygame.image.load('assets/backgrounds/level_background.png').convert_alpha()
    IMAGES['check'] = pygame.image.load('assets/buttons/check_button.png').convert_alpha()

    IMAGES['options_hover'] = pygame.image.load('assets/buttons/options_button_hover_v2.png').convert_alpha()
    IMAGES['play_hover'] = pygame.image.load('assets/buttons/play_button_hover.png').convert_alpha()
    IMAGES['quit_hover'] = pygame.image.load('assets/buttons/quit_button_hover.png').convert_alpha()
    IMAGES['help_hover'] = pygame.image.load('assets/buttons/help_button_hover.png').convert_alpha()
    IMAGES['back_hover'] = pygame.image.load('assets/buttons/back_button_hover.png').convert_alpha()
    IMAGES['menu_hover'] = pygame.image.load('assets/buttons/menu_button_hover.png').convert_alpha()
    IMAGES['sound_hover'] = pygame.image.load('assets/buttons/sound_button_hover.png').convert_alpha()
    IMAGES['check_hover'] = pygame.image.load('assets/buttons/check_button_hover.png').convert_alpha()

    IMAGES['menu_title'] = pygame.image.load('assets/titles/quantum_pisix_title.png').convert_alpha()
    IMAGES['levels_title'] = pygame.image.load('assets/titles/levels_title.png').convert_alpha()
    IMAGES['options_title'] = pygame.image.load('assets/titles/options_title.png').convert_alpha()
    IMAGES['how_to_play_title'] = pygame.image.load('assets/titles/how_to_play_title.png').convert_alpha()
    IMAGES['how_to_text'] = pygame.image.load('assets/other/how_to.png').convert_alpha()

    IMAGES['free_space'] = pygame.image.load('assets/level/free_space_test.png').convert_alpha()
    IMAGES['output'] = pygame.image.load('assets/level/output_test.png').convert_alpha()
    IMAGES['spiral'] = pygame.image.load('assets/level/spiral_test.png').convert_alpha()
    IMAGES['gates'] = pygame.image.load('assets/level/test_gates.png').convert_alpha()

    BUTTONS['play'] = button.Button(500, 300, IMAGES['play'], IMAGES['play_hover'], 1)
    BUTTONS['quit'] = button.Button(500, 400, IMAGES['quit'], IMAGES['quit_hover'], 1)
    BUTTONS['options'] = button.Button(65, 650, IMAGES['options'], IMAGES['options_hover'], 1)
    BUTTONS['sound'] = button.Button(500, 300, IMAGES['sound'], IMAGES['sound_hover'], 1)
    BUTTONS['help'] = button.Button(500, 400, IMAGES['help'], IMAGES['help_hover'], 1)
    BUTTONS['back'] = button.Button(500, 600, IMAGES['back'], IMAGES['back_hover'], 1)
    BUTTONS['menu'] = button.Button(500, 500, IMAGES['menu'], IMAGES['menu_hover'], 1)
    BUTTONS['check'] = button.Button(500, 650, IMAGES['check'], IMAGES['check_hover'], 1)


def press_sound():
    global IS_MUSIC_PLAYING
    if IS_MUSIC_PLAYING:
        mixer.music.pause()
        IS_MUSIC_PLAYING = False
    else:
        mixer.music.unpause()
        IS_MUSIC_PLAYING = True


def place_centered_image(img, x):
    rect = img.get_rect(center=(500, x))
    SCREEN.blit(img, rect)
    pygame.draw.rect(SCREEN, (34, 87, 122), rect, 1)


def place_level_buttons():
    global ACTIVE_SCREEN, A_BUTTON_WAS_CLICKED, CURRENT_LEVEL
    for i in range(len(LEVELS)):
        x = int(200 * (i % 4 + 1))
        y = int(200 + 100 * (i // 4 + 1))

        level_name = 'level_' + str(i+1)
        img_name = 'assets/buttons/' + level_name + '.png'
        hover_img_name = 'assets/buttons/' + level_name + '_hover.png'

        level_button_img = pygame.image.load(img_name).convert_alpha()
        level_button_hover_img = pygame.image.load(hover_img_name).convert_alpha()

        level_button = button.Button(x, y, level_button_img, level_button_hover_img, 1)
        create_button_and_call_function_on_press(level_button, lambda: update_current_level(i+1))


def update_current_level(x):
    global CURRENT_LEVEL, ACTIVE_SCREEN
    CURRENT_LEVEL = x
    ACTIVE_SCREEN = 'level_' + str(x)


def measure_cats():
    print('Your cats are very pretty today :)')


def get_cat_frames(cat):
    frame_1_name = 'assets/cats/' + str(cat[0]) + '/' + str(cat[0]) + '_' + str(cat[1]) + '_1.png'
    frame_2_name = 'assets/cats/' + str(cat[0]) + '/' + str(cat[0]) + '_' + str(cat[1]) + '_2.png'
    frame_1_img = pygame.image.load(frame_1_name).convert_alpha()
    frame_2_img = pygame.image.load(frame_2_name).convert_alpha()
    return [frame_1_img, frame_2_img]


def place_cat(cat, x, y):
    frames = get_cat_frames(cat)
    cat = felines.Cat(frames, x, y)
    MOVING_SPRITES.add(cat)


def place_common_elements():
    SCREEN.blit(IMAGES['gates'], (150, 10))
    SCREEN.blit(IMAGES['output'], (875, 10))


def place_row(y, cat, number_of_free_spaces):

    total_width = number_of_free_spaces * PIXELS['gate-width'] + (number_of_free_spaces + 1) * PIXELS['col-space'] \
                  + PIXELS['cat-width'] * 2
    starting_x = PIXELS['level-width-center'] - 0.5 * total_width

    place_cat(cat, starting_x + 0.5 * PIXELS['cat-width'], y)

    for i in range(number_of_free_spaces):
        free_space_x = starting_x + PIXELS['cat-width'] + i * (PIXELS['gate-width'] + PIXELS['col-space']) \
                       + 0.5 * PIXELS['gate-width'] + PIXELS['col-space']
        free_space = game_element.Element([IMAGES['free_space']], free_space_x, y)
        MOVING_SPRITES.add(free_space)

    spiral = game_element.Element([IMAGES['spiral']], starting_x + total_width - 0.5 * PIXELS['cat-width'], y)
    MOVING_SPRITES.add(spiral)


def draw_level():
    level_1 = level.Level([('foxy', 'idle'), ('foxy', 'idle')], [2], 3, IMAGES['output'])
    global LEVELS, CURRENT_LEVEL

    place_common_elements()

    number_of_cats = len(level_1.cats)

    for i in range(number_of_cats):
        if number_of_cats % 2 == 0:
            middle = number_of_cats / 2
            distance = i + 1 - middle
            if distance < 1:
                y = PIXELS['level-height-center'] + distance * (PIXELS['cat-height'] + PIXELS['row-space']) \
                    - 0.5 * (PIXELS['cat-height'] + PIXELS['row-space'])
                place_row(y, level_1.cats[i], level_1.number_of_free_spaces)
            else:
                y = PIXELS['level-height-center'] + distance * PIXELS['row-space'] \
                    + (distance + 0.5) * PIXELS['cat-height']
                place_row(y, level_1.cats[i], level_1.number_of_free_spaces)
        else:
            middle = number_of_cats // 2 + 1
            distance = i + 1 - middle
            y = PIXELS['level-height-center'] + distance * (PIXELS['cat-height'] + PIXELS['row-space'])
            place_row(y, level_1.cats[i], level_1.number_of_free_spaces)


def create_button_and_call_function_on_press(button_name, func):
    global A_BUTTON_WAS_CLICKED, ACTIVE_SCREEN
    if button_name.draw(SCREEN) and not A_BUTTON_WAS_CLICKED:
        A_BUTTON_WAS_CLICKED = True
        func()


def create_button_and_change_screen(button_name, new_screen):
    global A_BUTTON_WAS_CLICKED, ACTIVE_SCREEN
    if button_name.draw(SCREEN) and not A_BUTTON_WAS_CLICKED:
        A_BUTTON_WAS_CLICKED = True
        ACTIVE_SCREEN = new_screen


def quit_main_loop():
    global RUNNING
    RUNNING = False


def play_music():
    global IS_MUSIC_PLAYING
    mixer.music.load('assets/music/song.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(loops=-1)
    IS_MUSIC_PLAYING = True


def start_game_loop():
    global A_BUTTON_WAS_CLICKED, ACTIVE_SCREEN, RUNNING, CURRENT_LEVEL_WAS_DRAWN

    init_variables()
    play_music()

    while RUNNING:

        SCREEN.fill((52, 78, 91))
        SCREEN.blit(IMAGES['menu_bg'], (0, 0))

        if ACTIVE_SCREEN == 'menu':
            place_centered_image(IMAGES['menu_title'], 200)
            create_button_and_change_screen(BUTTONS['play'], 'levels')
            create_button_and_call_function_on_press(BUTTONS['quit'], quit_main_loop)

        elif ACTIVE_SCREEN == 'levels':
            place_centered_image(IMAGES['levels_title'], 100)
            place_level_buttons()
            create_button_and_change_screen(BUTTONS['back'], 'menu')

        elif ACTIVE_SCREEN.startswith('level_'):
            SCREEN.blit(IMAGES['level_bg'], (0, 0))
            place_common_elements()
            if not CURRENT_LEVEL_WAS_DRAWN:
                draw_level()
                CURRENT_LEVEL_WAS_DRAWN = True

            MOVING_SPRITES.draw(SCREEN)
            MOVING_SPRITES.update()

            create_button_and_change_screen(BUTTONS['options'], 'options')
            create_button_and_call_function_on_press(BUTTONS['check'], measure_cats)

        elif ACTIVE_SCREEN == 'options':
            place_centered_image(IMAGES['options_title'], 150)
            create_button_and_call_function_on_press(BUTTONS['sound'], lambda: press_sound())
            create_button_and_change_screen(BUTTONS['help'], 'help')
            create_button_and_change_screen(BUTTONS['menu'], 'menu')
            create_button_and_change_screen(BUTTONS['back'], 'level_' + str(CURRENT_LEVEL))

        elif ACTIVE_SCREEN == 'help':
            place_centered_image(IMAGES['how_to_play_title'], 100)
            place_centered_image(IMAGES['how_to_text'], 200)
            create_button_and_change_screen(BUTTONS['back'], 'options')

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                A_BUTTON_WAS_CLICKED = False
            if event.type == pygame.QUIT:
                RUNNING = False

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()


start_game_loop()
