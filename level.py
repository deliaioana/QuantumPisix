class Level:
    def __init__(self, cats, gates, number_of_free_spaces, output_img):
        self.cats = cats
        self.gates = gates
        self.number_of_free_spaces = number_of_free_spaces
        self.output_img = output_img
        self.current_state_of_gates = [[] * len(cats)]
