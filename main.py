import pygame
import button
import cat as felines
from pygame import mixer
import game_element
import os
import levels


mixer.init()
IS_MUSIC_PLAYING = False

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

PIXELS = {'row-space': 20, 'col-space': 30, 'cat-height': 80, 'cat-x': 200, 'level-height-center': 350,
          'level-width-center': 500, 'gate-width': 100, 'cat-width': 85, 'row-height': 100,
          'gates-y': 65, 'gate-space': 20}

CLOCK = pygame.time.Clock()
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Quantum Pisix')

IMAGES = {}
BUTTONS = {}

RUNNING = True
A_BUTTON_WAS_CLICKED = False
CURRENT_LEVEL_NUMBER = None
CURRENT_LEVEL_WAS_DRAWN = False
ACTIVE_SCREEN = 'menu'

LEVELS = [1, 2, 3, 4, 5, 6, 7, 8]
MOVING_SPRITES = pygame.sprite.Group()
MOVABLE_SPRITES = []
PLAYABLE_LEVELS = levels.Levels()


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
    IMAGES['output'] = pygame.image.load('assets/level/level_1_output.png').convert_alpha()
    IMAGES['camera'] = pygame.image.load('assets/level/camera.png').convert_alpha()
    IMAGES['gate-zone'] = pygame.image.load('assets/level/gate_zone.png').convert_alpha()

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
    global ACTIVE_SCREEN, A_BUTTON_WAS_CLICKED, CURRENT_LEVEL_NUMBER
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
    global CURRENT_LEVEL_NUMBER, ACTIVE_SCREEN, CURRENT_LEVEL_WAS_DRAWN

    CURRENT_LEVEL_WAS_DRAWN = False
    CURRENT_LEVEL_NUMBER = x
    ACTIVE_SCREEN = 'level_' + str(x)


def measure_cats():
    print('Your cats are very pretty today :)')


def place_cat(cat, x, y):
    frames = get_object_sprites('assets/cats/', cat[0])
    cat = felines.Cat(frames, x, y)
    MOVING_SPRITES.add(cat)


def place_common_elements():
    SCREEN.blit(IMAGES['gate-zone'], (150, 10))
    SCREEN.blit(IMAGES['output'], (875, 10))


def place_row(y, cat, number_of_free_spaces):

    total_width = number_of_free_spaces * PIXELS['gate-width'] + (number_of_free_spaces + 1) * PIXELS['col-space'] \
                  + PIXELS['cat-width'] * 2
    starting_x = PIXELS['level-width-center'] - 0.5 * total_width

    place_cat(cat, starting_x + 0.5 * PIXELS['cat-width'], y)

    for i in range(number_of_free_spaces):
        free_space_x = starting_x + PIXELS['cat-width'] + i * (PIXELS['gate-width'] + PIXELS['col-space']) \
                       + 0.5 * PIXELS['gate-width'] + PIXELS['col-space']
        free_space = game_element.Element([IMAGES['free_space']], free_space_x, y, 0)
        MOVING_SPRITES.add(free_space)

    camera = game_element.Element([IMAGES['camera']], starting_x + total_width - 0.5 * PIXELS['cat-width'], y, 0)
    MOVING_SPRITES.add(camera)


def get_level_from_screen():
    screen = ACTIVE_SCREEN
    return int(screen.split('_')[1])


def get_object_sprites(path, obj):
    path = os.path.join(path, str(obj))
    frames = os.listdir(path)
    frames.sort(key=lambda x: int(x.split('_')[-1][:-4]))
    frames = [path + '/' + f for f in frames if os.path.isfile(path + '/' + f)]

    frames_as_list = []

    for frame in frames:
        img = pygame.image.load(frame).convert_alpha()
        frames_as_list.append(img)

    return frames_as_list


def place_gates(gates):
    number_of_gates = len(gates)
    total_width = number_of_gates * PIXELS['gate-width'] + (number_of_gates - 1) * PIXELS['gate-space']
    starting_x = PIXELS['level-width-center'] - 0.5 * total_width

    for i, gate in enumerate(gates):
        sprites = get_object_sprites('assets/level/gates/', gate)

        x = starting_x + i * (PIXELS['gate-width'] + PIXELS['gate-space']) \
                       + 0.5 * PIXELS['gate-width'] + PIXELS['gate-space']

        element = game_element.Element(sprites, x, PIXELS['gates-y'], 0.2)
        MOVING_SPRITES.add(element)
        MOVABLE_SPRITES.append(element)


def draw_level():
    global LEVELS, CURRENT_LEVEL_NUMBER, MOVING_SPRITES

    MOVING_SPRITES.empty()
    CURRENT_LEVEL_NUMBER = get_level_from_screen()

    current_level = PLAYABLE_LEVELS.get_levels()[CURRENT_LEVEL_NUMBER]

    place_common_elements()
    place_gates(current_level.gates)

    number_of_cats = len(current_level.cats)
    total_height = PIXELS['row-height'] * number_of_cats + PIXELS['row-space'] * (number_of_cats - 1)
    starting_y = PIXELS['level-height-center'] - total_height * 0.5

    for i in range(number_of_cats):
        y = starting_y + i * (PIXELS['row-height'] + PIXELS['row-space']) + PIXELS['row-space'] \
            + 0.5 * PIXELS['row-height']
        place_row(y, current_level.cats[i], current_level.number_of_free_spaces)


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
            create_button_and_change_screen(BUTTONS['back'], 'level_' + str(CURRENT_LEVEL_NUMBER))

        elif ACTIVE_SCREEN == 'help':
            place_centered_image(IMAGES['how_to_play_title'], 100)
            place_centered_image(IMAGES['how_to_text'], 200)
            create_button_and_change_screen(BUTTONS['back'], 'options')

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                for element in MOVABLE_SPRITES:
                    if element.is_inside(position):
                        element.is_moving = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for element in MOVABLE_SPRITES:
                    element.is_moving = False

            if event.type == pygame.MOUSEBUTTONUP:
                A_BUTTON_WAS_CLICKED = False

            if event.type == pygame.QUIT:
                RUNNING = False

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()


start_game_loop()
