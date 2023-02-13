import level


class Levels:
    def __init__(self):
        self.levels = []

        level_1 = level.Level([('foxy', 'idle')], ['kiss_gate', 'catnip_gate'], 1, 'output')
        level_2 = level.Level([('miso', 'idle'), ('miso', 'idle')], ['kiss_gate'], 1, 'output')
        level_3 = level.Level([('foxy', 'idle'), ('peanut', 'idle'), ('cookie', 'idle')], ['kiss_gate'], 1, 'output')
        level_4 = level.Level([('miso', 'idle'), ('foxy', 'idle'), ('peanut', 'idle'), ('cookie', 'idle')],
                              ['kiss_gate'], 1, 'output')
        level_5 = level.Level([('miso', 'idle')], ['kiss_gate'], 2, 'output')
        level_6 = level.Level([('foxy', 'idle')], ['kiss_gate'], 3, 'output')
        level_7 = level.Level([('cookie', 'idle')], ['kiss_gate'], 4, 'output')
        level_8 = level.Level([('peanut', 'idle')], ['kiss_gate'], 5, 'output')

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
