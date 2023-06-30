import pygame
import button
import cat as felines
from pygame import mixer
import game_element
import os
import levels
from check_request import Request

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
SIMULATING = False
A_BUTTON_WAS_CLICKED = False
CURRENT_LEVEL_NUMBER = -1
CURRENT_LEVEL_WAS_DRAWN = False
ACTIVE_SCREEN = 'menu'

LEVELS_FIRST_PAGE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
LEVELS_SECOND_PAGE = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
UNLOCKED_LEVELS = [1]
MOVING_SPRITES = pygame.sprite.Group()
MOVABLE_SPRITES = []
CURRENT_OUTPUT = []
CAMERAS = []
ACTIVE_CATS = []
ACTIVE_GATE_GENERATORS_SPRITES = pygame.sprite.Group()
ACTIVE_GATE_GENERATORS_LIST = []
FREE_SPACES_GROUP = pygame.sprite.Group()
FREE_SPACES_LIST = []
PLAYABLE_LEVELS = levels.Levels()
PLATFORMS_GROUP = pygame.sprite.Group()
PLATFORMS_LIST = []
RESPONSE_DATA = ''
LEVEL_VERDICT = None
MEASURED_OUTPUT = ''

CURRENT_CONTROL_INFO = {'in_progress': False, 'controlled_object': None, 'controlling_object': None,
                        'controlling_row': 0, 'controlled_row': 0,
                        'controlled_pos_x': 0, 'controlled_pos_y': 0, 'controlling_pos_x': 0, 'controlling_pos_y': 0}


def refresh_current_control_info():
    global CURRENT_CONTROL_INFO
    CURRENT_CONTROL_INFO = {'in_progress': False, 'controlled_object': None, 'controlling_object': None}


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
    IMAGES['next_levels'] = pygame.image.load('assets/buttons/next_levels.png').convert_alpha()
    IMAGES['next_levels_hover'] = pygame.image.load('assets/buttons/next_levels_hover.png').convert_alpha()
    IMAGES['previous_levels'] = pygame.image.load('assets/buttons/previous_levels.png').convert_alpha()
    IMAGES['previous_levels_hover'] = pygame.image.load('assets/buttons/previous_levels_hover.png').convert_alpha()

    IMAGES['menu_title'] = pygame.image.load('assets/titles/quantum_pisix_title.png').convert_alpha()
    IMAGES['levels_title'] = pygame.image.load('assets/titles/levels_title.png').convert_alpha()
    IMAGES['options_title'] = pygame.image.load('assets/titles/options_title.png').convert_alpha()
    IMAGES['how_to_play_title'] = pygame.image.load('assets/titles/how_to_play_title.png').convert_alpha()
    IMAGES['how_to_text'] = pygame.image.load('assets/other/how_to.png').convert_alpha()

    IMAGES['free_space'] = pygame.image.load('assets/level/free_space_test.png').convert_alpha()
    IMAGES['camera'] = pygame.image.load('assets/level/camera.png').convert_alpha()
    IMAGES['gate-zone'] = pygame.image.load('assets/level/gate_zone.png').convert_alpha()

    IMAGES['camera_hover'] = pygame.image.load('assets/level/hover/camera_hover.png').convert_alpha()
    IMAGES['button_hover'] = pygame.image.load('assets/level/hover/button_hover.png').convert_alpha()
    IMAGES['box_gate_hover'] = pygame.image.load('assets/level/hover/box_gate_hover.png').convert_alpha()
    IMAGES['cat_hover'] = pygame.image.load('assets/level/hover/cat_hover.png').convert_alpha()
    IMAGES['catnip_gate_hover'] = pygame.image.load('assets/level/hover/catnip_gate_hover.png').convert_alpha()
    IMAGES['milk_gate_hover'] = pygame.image.load('assets/level/hover/milk_gate_hover.png').convert_alpha()
    IMAGES['mouse_gate_hover'] = pygame.image.load('assets/level/hover/mouse_gate_hover.png').convert_alpha()
    IMAGES['output_hover'] = pygame.image.load('assets/level/hover/output_hover.png').convert_alpha()
    IMAGES['cat-food_gate_hover'] = pygame.image.load('assets/level/hover/cat-food_gate_hover.png').convert_alpha()
    IMAGES['control_hover'] = pygame.image.load('assets/level/hover/control_hover.png').convert_alpha()
    IMAGES['flash'] = pygame.image.load('assets/level/flash.png').convert_alpha()

    BUTTONS['play'] = button.Button(500, 300, IMAGES['play'], IMAGES['play_hover'], 1)
    BUTTONS['quit'] = button.Button(500, 400, IMAGES['quit'], IMAGES['quit_hover'], 1)
    BUTTONS['options'] = button.Button(65, 650, IMAGES['options'], IMAGES['options_hover'], 1)
    BUTTONS['sound'] = button.Button(500, 300, IMAGES['sound'], IMAGES['sound_hover'], 1)
    BUTTONS['help'] = button.Button(500, 400, IMAGES['help'], IMAGES['help_hover'], 1)
    BUTTONS['back'] = button.Button(500, 600, IMAGES['back'], IMAGES['back_hover'], 1)
    BUTTONS['menu'] = button.Button(500, 500, IMAGES['menu'], IMAGES['menu_hover'], 1)
    BUTTONS['check'] = button.Button(500, 650, IMAGES['check'], IMAGES['check_hover'], 1)
    BUTTONS['next_levels'] = button.Button(950, SCREEN_WIDTH / 2, IMAGES['next_levels'], IMAGES['next_levels_hover'], 1)
    BUTTONS['previous_levels'] = button.Button(50, SCREEN_WIDTH / 2, IMAGES['previous_levels'],
                                               IMAGES['previous_levels_hover'], 1)


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


def place_level_buttons(page):
    global UNLOCKED_LEVELS

    displayed_levels = LEVELS_FIRST_PAGE
    if page == 2:
        displayed_levels = LEVELS_SECOND_PAGE

    for i in range(len(displayed_levels)):
        x = int(200 * (i % 4 + 1))
        y = int(200 + 100 * (i // 4 + 1))

        if displayed_levels[i] in UNLOCKED_LEVELS:
            level_name = 'level_' + str(displayed_levels[i])
            img_name = 'assets/buttons/' + level_name + '.png'
            hover_img_name = 'assets/buttons/' + level_name + '_hover.png'

            level_button_img = pygame.image.load(img_name).convert_alpha()
            level_button_hover_img = pygame.image.load(hover_img_name).convert_alpha()

            level_button = button.Button(x, y, level_button_img, level_button_hover_img, 1)
            create_button_and_call_function_on_press(level_button, lambda: update_current_level(displayed_levels[i]))

        else:
            img_name = 'assets/buttons/locked_level.png'
            level_button_img = pygame.image.load(img_name).convert_alpha()
            level_button = button.Button(x, y, level_button_img, level_button_img, 1)
            create_button_and_call_function_on_press(level_button, lambda: update_current_level(displayed_levels[i]))


def update_current_level(x):
    global CURRENT_LEVEL_NUMBER, ACTIVE_SCREEN, CURRENT_LEVEL_WAS_DRAWN, UNLOCKED_LEVELS

    if x in UNLOCKED_LEVELS:
        CURRENT_LEVEL_WAS_DRAWN = False
        CURRENT_LEVEL_NUMBER = x
        ACTIVE_SCREEN = 'level_' + str(x)


def is_circuit_completed():
    for free_space in FREE_SPACES_LIST:
        if free_space.is_visible:
            return False
    return True


def show_message(message):
    popup_font = pygame.font.Font(None, 40)
    popup_text = popup_font.render(message, True, (0, 0, 0))

    popup_width = popup_text.get_width() + 20
    popup_height = popup_text.get_height() + 20

    popup_surface = pygame.Surface((popup_width, popup_height))
    popup_surface.fill((199, 249, 204))

    popup_rect = popup_surface.get_rect()
    popup_rect.center = (SCREEN.get_width() // 2, SCREEN.get_height() // 2)

    SCREEN.blit(popup_surface, popup_rect)
    SCREEN.blit(popup_text, (popup_rect.x + 10, popup_rect.y + 10))

    pygame.display.update()
    pygame.time.delay(int(2 * 1000))


def restart_level():
    refresh_current_control_info()
    empty_level_objects()
    update_current_level(CURRENT_LEVEL_NUMBER)


def get_all_placed_gates():
    gates = []

    for element in MOVABLE_SPRITES:
        if element.name.startswith("SPAWNED_"):
            gates.append(element)

    return gates


def get_wanted_output():
    current_level = PLAYABLE_LEVELS.get_levels()[CURRENT_LEVEL_NUMBER]
    return current_level.output_info


def get_circuit_info(gates, cats, output):
    return {'gates': gates, 'cats': cats, 'output': output}


def win_level():
    global CURRENT_LEVEL_NUMBER

    current_level = CURRENT_LEVEL_NUMBER
    UNLOCKED_LEVELS.append(current_level + 1)
    show_message('Great job! Loading the next level...')
    update_current_level(current_level + 1)


def lose_level():
    show_message('Incorrect output! Let\'s try again!')
    restart_level()


def simulate_circuit(data):
    global SIMULATING, RESPONSE_DATA, MEASURED_OUTPUT
    SIMULATING = True
    RESPONSE_DATA = data
    MEASURED_OUTPUT = max(RESPONSE_DATA, key=RESPONSE_DATA.get)
    MEASURED_OUTPUT = MEASURED_OUTPUT[::-1]
    print('measured: ', MEASURED_OUTPUT)


def is_correct_answer(real_output, output_info):
    target_output = ''.join([str(c) for c in output_info])

    for state in real_output:
        state = state[::-1]
        for i, q in enumerate(state):
            print('qubit: ', q, ', target: ', target_output[i])
            if target_output[i] != q:
                if target_output[i] in ['0', '1']:
                    return False

                if target_output[i] == 3:
                    index_q2 = target_output.index('2')
                    if state[index_q2] != q:
                        return False

    return True


def handle_check_response(data):
    global LEVEL_VERDICT
    simulate_circuit(data)
    level_verdict = is_correct_answer(data, PLAYABLE_LEVELS.get_levels()[CURRENT_LEVEL_NUMBER].output_info)
    print('level verdict: ', level_verdict)

    LEVEL_VERDICT = level_verdict


def measure_cats():
    if not is_circuit_completed():
        show_message('Complete the circuit first! Meow!')

    else:
        gates = get_all_placed_gates()
        cats = ACTIVE_CATS
        output = get_wanted_output()

        circuit = get_circuit_info(gates, cats, output)

        request = Request(circuit)
        data = request.send_request()
        print('response = ', data)
        handle_check_response(data)


def place_cat(cat, x, y):
    idle_frames = get_cat_sprites('assets/cats/', cat[0], 'idle')
    asleep_frames = get_cat_sprites('assets/cats/', cat[0], 'asleep')
    super_frames = get_cat_sprites('assets/cats/', cat[0], 'super')

    current_state = cat[1]

    cat = felines.Cat(idle_frames, asleep_frames, super_frames, current_state, x, y)
    MOVING_SPRITES.add(cat)
    ACTIVE_CATS.append(cat)


def place_platform(size, y):
    path = 'assets/level/platforms/'
    object_name = 'platform_' + str(size)
    platform_images = get_object_sprites(path, object_name)
    platform = game_element.Element('platform', platform_images, PIXELS['level-width-center'], y + 40, 0.2)

    PLATFORMS_GROUP.add(platform)
    PLATFORMS_LIST.append(platform)


def place_common_elements():
    global CURRENT_LEVEL_NUMBER

    SCREEN.blit(IMAGES['gate-zone'], (150, 10))

    current_output_image_name = 'assets/level/outputs/level_' + str(CURRENT_LEVEL_NUMBER) + '.png'
    output_image = pygame.image.load(current_output_image_name).convert_alpha()
    output_frames = [output_image]

    output_element = game_element.Element('output', output_frames, 925, SCREEN_HEIGHT / 2, 0)

    MOVING_SPRITES.add(output_element)
    CURRENT_OUTPUT.append(output_element)


def place_row(row_number, y, cat, number_of_free_spaces):
    total_width = number_of_free_spaces * PIXELS['gate-width'] + (number_of_free_spaces + 1) * PIXELS['col-space'] \
                  + PIXELS['cat-width'] * 2
    starting_x = PIXELS['level-width-center'] - 0.5 * total_width

    if number_of_free_spaces in [1, 2, 3, 4]:
        place_platform(number_of_free_spaces, y)

    place_cat(cat, starting_x + 0.5 * PIXELS['cat-width'], y)

    for i in range(number_of_free_spaces):
        free_space_x = starting_x + PIXELS['cat-width'] + i * (PIXELS['gate-width'] + PIXELS['col-space']) \
                       + 0.5 * PIXELS['gate-width'] + PIXELS['col-space']
        free_space = game_element.Element('free_space', [IMAGES['free_space']], free_space_x, y, 0, row_number, i + 1)
        FREE_SPACES_GROUP.add(free_space)
        FREE_SPACES_LIST.append(free_space)

    camera = game_element.Element('camera', [IMAGES['camera']],
                                  starting_x + total_width - 0.5 * PIXELS['cat-width'], y, 0)
    MOVING_SPRITES.add(camera)
    CAMERAS.append(camera)


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


def get_only_correct_state_frames(frames, state):
    wanted_frames = []
    for frame in frames:
        copy = str(frame)
        if copy.split('_')[1] == str(state):
            wanted_frames.append(frame)
    return wanted_frames


def get_cat_sprites(path, cat, state):
    path = os.path.join(path, str(cat))
    frames = os.listdir(path)
    frames = get_only_correct_state_frames(frames, state)
    frames.sort(key=lambda x: int(x.split('_')[-1][:-4]))
    frames = [path + '/' + f for f in frames if os.path.isfile(path + '/' + f)]

    frames_as_list = []

    for frame in frames:
        img = pygame.image.load(frame).convert_alpha()
        frames_as_list.append(img)

    return frames_as_list


def spawn_gate(gate, position):
    sprites = get_object_sprites('assets/level/gates/', gate)

    x, y = position
    name = "SPAWNED_" + gate
    speed = 0.2
    if gate == 'box_gate':
        speed = 0.09
    elif gate == 'mouse_gate':
        speed = 0.09

    element = game_element.Element(name, sprites, x, y, speed)
    MOVING_SPRITES.add(element)
    MOVABLE_SPRITES.append(element)

    return element


def place_gate_generators(gates):
    number_of_gates = len(gates)
    total_width = number_of_gates * PIXELS['gate-width'] + (number_of_gates - 1) * PIXELS['gate-space']
    starting_x = PIXELS['level-width-center'] - 0.5 * total_width

    for i, gate in enumerate(gates):
        sprites = get_object_sprites('assets/level/gates/', gate)

        x = starting_x + i * (PIXELS['gate-width'] + PIXELS['gate-space']) \
            + 0.5 * PIXELS['gate-width'] + PIXELS['gate-space']

        element = game_element.Element(gate, sprites, x, PIXELS['gates-y'], 0.2)
        ACTIVE_GATE_GENERATORS_SPRITES.add(element)
        ACTIVE_GATE_GENERATORS_LIST.append(element)


def filter_free_spaces_by_visibility():
    global FREE_SPACES_GROUP, FREE_SPACES_LIST

    FREE_SPACES_GROUP.empty()
    for free_space in FREE_SPACES_LIST:
        if free_space.is_visible:
            FREE_SPACES_GROUP.add(free_space)


def draw_level():
    global CURRENT_LEVEL_NUMBER, MOVING_SPRITES, FREE_SPACES_GROUP, FREE_SPACES_LIST, \
        ACTIVE_GATE_GENERATORS_SPRITES, ACTIVE_GATE_GENERATORS_LIST, ACTIVE_CATS, CURRENT_OUTPUT, CAMERAS

    empty_level_objects()

    current_level = PLAYABLE_LEVELS.get_levels()[CURRENT_LEVEL_NUMBER]

    number_of_cats = len(current_level.cats)
    total_height = PIXELS['row-height'] * number_of_cats + PIXELS['row-space'] * (number_of_cats - 1)
    starting_y = PIXELS['level-height-center'] - total_height * 0.5

    for i in range(number_of_cats):
        y = starting_y + i * (PIXELS['row-height'] + PIXELS['row-space']) + PIXELS['row-space'] \
            + 0.5 * PIXELS['row-height']
        place_row(i + 1, y, current_level.cats[i], current_level.number_of_free_spaces)

    place_common_elements()
    place_gate_generators(current_level.gates)


def create_button_and_call_function_on_press(button_name, func):
    global A_BUTTON_WAS_CLICKED, ACTIVE_SCREEN
    if button_name.draw(SCREEN) and not A_BUTTON_WAS_CLICKED:
        A_BUTTON_WAS_CLICKED = True
        func()


def empty_level_objects():
    global CURRENT_LEVEL_NUMBER, MOVING_SPRITES, FREE_SPACES_GROUP, FREE_SPACES_LIST, \
        ACTIVE_GATE_GENERATORS_SPRITES, ACTIVE_GATE_GENERATORS_LIST, ACTIVE_CATS, CURRENT_OUTPUT, \
        CAMERAS, PLATFORMS_GROUP, PLATFORMS_LIST, MOVABLE_SPRITES, RESPONSE_DATA, SIMULATING, LEVEL_VERDICT, \
        MEASURED_OUTPUT

    ACTIVE_GATE_GENERATORS_SPRITES.empty()
    ACTIVE_GATE_GENERATORS_LIST = []
    MOVING_SPRITES.empty()
    ACTIVE_CATS = []
    CAMERAS = []
    CURRENT_OUTPUT = []
    FREE_SPACES_GROUP.empty()
    FREE_SPACES_LIST.clear()
    CURRENT_LEVEL_NUMBER = get_level_from_screen()
    PLATFORMS_GROUP.empty()
    PLATFORMS_LIST.clear()
    MOVABLE_SPRITES = []
    RESPONSE_DATA = ''
    SIMULATING = False
    LEVEL_VERDICT = None
    MEASURED_OUTPUT = ''


def create_button_and_change_screen(button_name, new_screen):
    global A_BUTTON_WAS_CLICKED, ACTIVE_SCREEN, CURRENT_LEVEL_WAS_DRAWN, SIMULATING

    if button_name.draw(SCREEN) and not A_BUTTON_WAS_CLICKED:
        refresh_current_control_info()
        SIMULATING = False
        if ACTIVE_SCREEN.startswith('level_'):
            empty_level_objects()
        elif ACTIVE_SCREEN == 'options' and new_screen.startswith('level_'):
            CURRENT_LEVEL_WAS_DRAWN = False
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


def get_hover_objects():
    objects = []
    objects.extend(ACTIVE_CATS)
    objects.extend(ACTIVE_GATE_GENERATORS_LIST)
    objects.extend(CURRENT_OUTPUT)
    objects.extend(CAMERAS)
    return objects


def get_hover_image(element):
    if isinstance(element, felines.Cat):
        return IMAGES['cat_hover']
    else:
        name = element.name
        if name == 'output':
            return IMAGES['output_hover']
        elif name == 'camera':
            return IMAGES['camera_hover']
        elif name in ['catnip_gate', 'cat-food_gate', 'milk_gate', 'box_gate', 'mouse_gate', 'control']:
            image_name = name + '_hover'
            return IMAGES[image_name]


def is_inside_hover_element(element, x, y):
    return element.rect.collidepoint(x, y)


def get_hover_image_position(x, y):
    if x + 260 > SCREEN_WIDTH:
        return x - 260, y
    return x + 10, y


def handle_control_gate_click():
    show_message('Please click on the controlled gate')
    CURRENT_CONTROL_INFO['in_progress'] = True


def get_control_height(controlled_row, controlling_row):
    return abs(controlled_row - controlling_row)


def compute_middle_point(first_pos, second_pos):
    return int((first_pos[0] + second_pos[0]) / 2), int((first_pos[1] + second_pos[1]) / 2)


def place_control_object_in_position(control_height, position, is_upside_down):
    path = 'assets/level/gates/spawned_control/'
    object_name = 'control_' + str(control_height)

    if is_upside_down:
        object_name = 'control_upside_down_' + str(control_height)

    control_sprites = get_object_sprites(path, object_name)
    control_obj = game_element.Element('PLACED_control', control_sprites, position[0], position[1], 0)
    MOVING_SPRITES.add(control_obj)
    MOVABLE_SPRITES.append(control_obj)


def place_control_object(controlled_row, controlling_row, controlled_pos, controlling_pos):
    control_height = get_control_height(controlled_row, controlling_row)
    is_upside_down = controlling_row - controlled_row > 0
    position = compute_middle_point(controlled_pos, controlling_pos)

    place_control_object_in_position(control_height, position, is_upside_down)


def handle_placed_control():
    show_message('You have successfully used a control gate!')
    print(CURRENT_CONTROL_INFO)

    controlled_row = CURRENT_CONTROL_INFO['controlled_row']
    controlling_row = CURRENT_CONTROL_INFO['controlling_row']

    controlled_position = CURRENT_CONTROL_INFO['controlled_pos_x'], CURRENT_CONTROL_INFO['controlled_pos_y']
    controlling_position = CURRENT_CONTROL_INFO['controlling_pos_x'], CURRENT_CONTROL_INFO['controlling_pos_y']

    CURRENT_CONTROL_INFO['controlled_object'].controlled_by = controlling_row - 1
    place_control_object(controlled_row, controlling_row, controlled_position,
                         controlling_position)


def start_game_loop():
    global A_BUTTON_WAS_CLICKED, ACTIVE_SCREEN, RUNNING, CURRENT_LEVEL_WAS_DRAWN, FREE_SPACES_GROUP, \
        FREE_SPACES_LIST, SIMULATING

    init_variables()
    play_music()

    while RUNNING:

        SCREEN.fill((52, 78, 91))
        SCREEN.blit(IMAGES['menu_bg'], (0, 0))

        if ACTIVE_SCREEN == 'menu':
            place_centered_image(IMAGES['menu_title'], 200)
            create_button_and_change_screen(BUTTONS['play'], 'levels_1')
            create_button_and_call_function_on_press(BUTTONS['quit'], quit_main_loop)

        elif ACTIVE_SCREEN == 'levels_1':
            place_centered_image(IMAGES['levels_title'], 100)
            place_level_buttons(1)
            create_button_and_change_screen(BUTTONS['back'], 'menu')
            create_button_and_change_screen(BUTTONS['next_levels'], 'levels_2')

        elif ACTIVE_SCREEN == 'levels_2':
            place_centered_image(IMAGES['levels_title'], 100)
            place_level_buttons(2)
            create_button_and_change_screen(BUTTONS['back'], 'menu')
            create_button_and_change_screen(BUTTONS['previous_levels'], 'levels_1')

        elif ACTIVE_SCREEN.startswith('level_'):
            SCREEN.blit(IMAGES['level_bg'], (0, 0))
            place_common_elements()
            if not CURRENT_LEVEL_WAS_DRAWN:
                draw_level()
                CURRENT_LEVEL_WAS_DRAWN = True

            PLATFORMS_GROUP.draw(SCREEN)
            MOVING_SPRITES.draw(SCREEN)
            ACTIVE_GATE_GENERATORS_SPRITES.draw(SCREEN)
            MOVING_SPRITES.update()

            if SIMULATING:
                PLATFORMS_GROUP.update()

            filter_free_spaces_by_visibility()
            FREE_SPACES_GROUP.draw(SCREEN)

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
            place_centered_image(IMAGES['how_to_text'], 350)
            create_button_and_change_screen(BUTTONS['back'], 'options')

        if not SIMULATING:

            if LEVEL_VERDICT is not None:
                if LEVEL_VERDICT:
                    win_level()
                else:
                    lose_level()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    position = pygame.mouse.get_pos()
                    for element in MOVABLE_SPRITES:
                        if element.is_position_inside(position):
                            element.is_moving = True
                            if element.is_attached_to_free_space:
                                element.is_attached_to_free_space = False
                                element.free_space.is_visible = True
                                element.free_space.attached_gate = None
                                element.free_space = None

                    for element in ACTIVE_GATE_GENERATORS_LIST:
                        if element.is_position_inside(position):
                            if element.name == 'control':
                                handle_control_gate_click()
                            else:
                                new_gate = spawn_gate(element.name, position)
                                if new_gate.is_position_inside(position):
                                    new_gate.is_moving = True
                                    if new_gate.is_attached_to_free_space:
                                        new_gate.is_attached_to_free_space = False
                                        new_gate.free_space.is_visible = True
                                        new_gate.free_space.attached_gate = None
                                        new_gate.free_space = None

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    for element in MOVABLE_SPRITES:
                        if element.is_moving:
                            element.is_moving = False
                            is_attached = False

                            for free_space in FREE_SPACES_LIST:
                                if element.is_inside_free_space(free_space):
                                    free_space.attach_gate(element)
                                    is_attached = True

                                    if CURRENT_CONTROL_INFO['in_progress'] and \
                                            CURRENT_CONTROL_INFO['controlled_object'] is None:
                                        CURRENT_CONTROL_INFO['controlled_object'] = element
                                        CURRENT_CONTROL_INFO['controlled_row'] = free_space.get_row()

                                        CURRENT_CONTROL_INFO['controlled_pos_x'], \
                                            CURRENT_CONTROL_INFO['controlled_pos_y'] = free_space.get_pos()
                                        show_message('Now click on the controlling empty zone in the same column.')

                                    elif CURRENT_CONTROL_INFO['in_progress'] and \
                                            CURRENT_CONTROL_INFO['controlling_object'] is None:
                                        CURRENT_CONTROL_INFO['controlling_object'] = element
                                        CURRENT_CONTROL_INFO['controlling_row'] = free_space.get_row()

                                        CURRENT_CONTROL_INFO['controlling_pos_x'], \
                                            CURRENT_CONTROL_INFO['controlling_pos_y'] = free_space.get_pos()

                                        handle_placed_control()
                                        refresh_current_control_info()

                            if not is_attached:
                                MOVING_SPRITES.remove(element)
                                MOVABLE_SPRITES.remove(element)
                                element.__del__()

                if event.type == pygame.MOUSEBUTTONUP:
                    A_BUTTON_WAS_CLICKED = False

                if event.type == pygame.QUIT:
                    RUNNING = False

        else:
            PLATFORMS_GROUP.update()
            MOVING_SPRITES.update()

            for cat in ACTIVE_CATS:
                cat.move_in_circuit()

                for element in MOVABLE_SPRITES:
                    if cat.is_next_to_element(element):
                        MOVING_SPRITES.remove(element)
                        MOVABLE_SPRITES.remove(element)
                        cat.change_state(element.name)

                if cat.is_next_to_camera(CAMERAS[0].get_pos()[0]):
                    cat.collapse_state(int(MEASURED_OUTPUT[ACTIVE_CATS.index(cat)]))
                    pygame.time.delay(int(2 * 1000))
                    SIMULATING = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        objects = get_hover_objects()

        for element in objects:
            if is_inside_hover_element(element, mouse_x, mouse_y):
                hover_image = get_hover_image(element)
                hover_image_position = get_hover_image_position(mouse_x, mouse_y)
                SCREEN.blit(hover_image, hover_image_position)
                break

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()


start_game_loop()
