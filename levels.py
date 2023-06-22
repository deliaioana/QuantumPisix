import level


class Levels:
    def __init__(self):
        self.levels = []

        level_1 = level.Level([('foxy', 'idle')], ['box_gate'], 1, "", [1])
        level_2 = level.Level([('peanut', 'asleep')], ['box_gate'], 1, "", [0])
        level_3 = level.Level([('cookie', 'idle')], ['milk_gate'], 1, "", [0])
        level_4 = level.Level([('miso', 'asleep')], ['milk_gate'], 1, "", [1])

        level_5 = level.Level([('foxy', 'idle'), ('cookie', 'asleep')], ['milk_gate'], 4, "", [1, 0])
        level_6 = level.Level([('cookie', 'idle')], ['catnip_gate'], 1, "", [2])
        level_7 = level.Level([('peanut', 'asleep')], ['catnip_gate'], 1, "", [2])
        level_8 = level.Level([('miso', 'asleep')], ['cat-food_gate'], 1, "", [0])

        level_9 = level.Level([('cookie', 'idle')], ['cat-food_gate'], 1, "", [1])
        level_10 = level.Level([('miso', 'asleep')], ['mouse_gate'], 1, "", [1])
        level_11 = level.Level([('peanut', 'idle')], ['mouse_gate'], 1, "", [0])
        level_12 = level.Level([('foxy', 'asleep'), ('peanut', 'asleep')], ['milk_gate', 'control'], 1, "", [0, 0])

        level_13 = level.Level([('miso', 'idle'), ('cookie', 'idle')], ['milk_gate', 'control'], 2, "", [0, 0])
        level_14 = level.Level([('foxy', 'asleep'), ('peanut', 'asleep')],
                               ['catnip_gate', 'control', 'milk_gate', 'box_gate'], 2, "", [2, 3])
        level_15 = level.Level([('miso', 'asleep'), ('cookie', 'asleep'), ('peanut', 'asleep'), ('foxy', 'asleep')],
                               ['milk_gate', 'control', 'catnip_gate'], 4, "", [2, 3, 3, 3])
        level_16 = level.Level([('foxy', 'asleep'), ('cookie', 'idle'), ('miso', 'asleep')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               3, "", [2, 0, 1])

        level_17 = level.Level([('miso', 'idle'), ('cookie', 'idle'), ('peanut', 'idle'), ('foxy', 'idle')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               1, "", [0, 1, 0, 1])
        level_18 = level.Level([('cookie', 'asleep'), ('foxy', 'asleep'), ('miso', 'idle')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               3, "", [1, 0, 2])
        level_19 = level.Level([('peanut', 'idle'), ('cookie', 'asleep')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               4, "", [2, 2])
        level_20 = level.Level([('cookie', 'idle'), ('foxy', 'idle')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               3, "", [2, 3])

        level_21 = level.Level([('miso', 'asleep'), ('cookie', 'asleep'), ('peanut', 'asleep'), ('foxy', 'asleep')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               2, "", [3, 3, 2, 1])
        level_22 = level.Level([('cookie', 'idle'), ('foxy', 'asleep')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               3, "", [2, 3])
        level_23 = level.Level([('miso', 'idle'), ('cookie', 'idle'), ('peanut', 'idle'), ('foxy', 'idle')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               4, "", [3, 1, 2, 0])
        level_24 = level.Level([('foxy', 'asleep')],
                               ['milk_gate', 'control', 'cat-food_gate', 'box_gate', 'mouse_gate', 'catnip_gate'],
                               4, "", [2])

        self.levels.append(0)
        self.levels.append(level_1)
        self.levels.append(level_2)
        self.levels.append(level_3)
        self.levels.append(level_4)
        self.levels.append(level_5)
        self.levels.append(level_6)
        self.levels.append(level_7)
        self.levels.append(level_8)
        self.levels.append(level_9)
        self.levels.append(level_10)
        self.levels.append(level_11)
        self.levels.append(level_12)
        self.levels.append(level_13)
        self.levels.append(level_14)
        self.levels.append(level_15)
        self.levels.append(level_16)
        self.levels.append(level_17)
        self.levels.append(level_18)
        self.levels.append(level_19)
        self.levels.append(level_20)
        self.levels.append(level_21)
        self.levels.append(level_22)
        self.levels.append(level_23)
        self.levels.append(level_24)

    def get_levels(self):
        return self.levels

