class Level:
    def __init__(self, cats, gates, number_of_free_spaces, output_image, output_info):
        self.cats = cats
        self.gates = gates
        self.number_of_free_spaces = number_of_free_spaces
        self.current_state_of_gates = [[] * len(cats)]
        self.output_image = output_image
        self.output_info = output_info
