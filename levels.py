import level


class Levels:
    def __init__(self):
        self.levels = []

        level_1 = level.Level([('cookie', 'idle'), ('peanut', 'idle'), ('foxy', 'idle'), ('miso', 'idle')],
                              ['milk_gate', 'catnip_gate', 'box_gate', 'cat-food_gate', 'mouse_gate'], 4, "", [1])
        level_2 = level.Level([('miso', 'idle'), ('miso', 'idle')], ['milk_gate'], 1, "", [1, 1])
        level_3 = level.Level([('foxy', 'idle'), ('peanut', 'idle'), ('miso', 'asleep'), ('cookie', 'idle')],
                              ['catnip_gate'], 1, "", [1, 1, 1])
        level_4 = level.Level([('miso', 'asleep'), ('foxy', 'asleep'), ('peanut', 'asleep'), ('cookie', 'asleep')],
                              ['milk_gate', 'catnip_gate', 'box_gate', 'cat-food_gate', 'mouse_gate'],
                              5, "", [0, 0, 0, 0])
        level_5 = level.Level([('miso', 'idle')], ['catnip_gate'], 2, "", [1])
        level_6 = level.Level([('foxy', 'idle')], ['catnip_gate'], 3, "", [1])
        level_7 = level.Level([('cookie', 'super'), ('peanut', 'super')], ['catnip_gate'], 4, "", [1])
        level_8 = level.Level([('peanut', 'idle')], ['catnip_gate'], 5, "", [2])

        self.levels.append(0)
        self.levels.append(level_1)
        self.levels.append(level_2)
        self.levels.append(level_3)
        self.levels.append(level_4)
        self.levels.append(level_5)
        self.levels.append(level_6)
        self.levels.append(level_7)
        self.levels.append(level_8)

    def get_levels(self):
        return self.levels

