import requests
import json


def get_circuit_size(circuit):
    n = len(circuit['cats'])
    m = int(len(circuit['gates']) / n)
    return n, m


def get_cats_states_sorted(circuit):
    cats = circuit['cats']
    cats_states = [(cat.rect.center[1], cat.state) for cat in cats]
    cats_states = sorted(cats_states)
    cats_states = list(zip(*cats_states))[1]

    print('cats_states: ', cats_states)
    return cats_states


def get_gates_sorted(n, circuit):
    gates = circuit['gates']

    heights = [gate.rect.center[1] for gate in gates]
    current_min_height = min(heights)
    matrix = []

    for i in range(n):
        line = [(gate.rect.center[0], gate.name[8:]) for gate in gates if gate.rect.center[1] == current_min_height]
        sorted(line)
        line = list(zip(*line))[1]
        matrix.append(line)

        if i < n-1:
            current_min_height = min(i for i in heights if i > current_min_height)

    return matrix


def get_output(circuit):
    return circuit['output']


def process_circuit_info(circuit):
    n, m = get_circuit_size(circuit)
    cats_states = get_cats_states_sorted(circuit)
    gates_matrix = get_gates_sorted(n, circuit)
    output = get_output(circuit)

    circuit = {'n': n, 'm': m, 'gates': gates_matrix, 'cats': cats_states, 'output': output}
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
