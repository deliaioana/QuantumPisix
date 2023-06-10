import requests
import json


def get_circuit_size(circuit):
    n = len(circuit['cats'])
    m = int(len(circuit['gates']) / n)
    return n, m


def convert_cats_states(cats_states):
    return [int(state == 'idle') for state in cats_states]


def get_cats_states_sorted(circuit):
    cats = circuit['cats']
    cats_states = [(cat.rect.center[1], cat.state) for cat in cats]
    cats_states = sorted(cats_states)
    cats_states = list(zip(*cats_states))[1]

    cats_states = convert_cats_states(cats_states)

    cats_states = ''.join([str(state) for state in cats_states])
    print('cats_states: ', cats_states)

    return cats_states


def get_real_gate_name(name):
    return 'h'


def compute_line(size, real_names_list, controlled_list):
    line = []
    for i in range(size):
        if controlled_list[i] is None:
            pair = (False, real_names_list[i])
            line.append(pair)
        else:
            pair = (True, (i, controlled_list[i], real_names_list[i]))
            line.append(pair)
    return line


def get_gates_sorted(n, m, circuit):
    gates = circuit['gates']

    heights = [gate.rect.center[1] for gate in gates]
    current_min_height = min(heights)
    matrix = []

    for i in range(n):
        line = [(gate.rect.center[0], get_real_gate_name(gate.name[8:]), gate)
                for gate in gates if gate.rect.center[1] == current_min_height]
        sorted(line)
        real_names_list = list(zip(*line))[1]
        controlled_list = list(zip(*line))[2]
        controlled_list = [gate.controlled_by for gate in controlled_list]
        line = compute_line(m, real_names_list, controlled_list)
        matrix.append(line)

        if i < n-1:
            current_min_height = min(i for i in heights if i > current_min_height)

    return matrix


def get_output(circuit):
    return circuit['output']


def process_circuit_info(circuit):
    n, m = get_circuit_size(circuit)
    cats_states = get_cats_states_sorted(circuit)
    gates_matrix = get_gates_sorted(n, m, circuit)
    output = get_output(circuit)

    circuit = {'n': n, 'm': m, 'gates': gates_matrix, 'cats': cats_states, 'output': output}

    print('TO JSON\n', circuit)
    circuit_json = json.dumps(circuit)
    return circuit_json


class Request:
    url = "http://localhost:8082"

    def __init__(self, circuit):
        self.circuit = circuit

    def send_request(self):
        info_json = process_circuit_info(self.circuit)
        response = requests.post(url=self.url, json=info_json)
        data = response.text
        return data
