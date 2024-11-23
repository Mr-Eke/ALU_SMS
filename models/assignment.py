#!/usr/bin/python3
import json

# Helper function: helps load data from JSON files
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# saves data to JSON files
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

class Assignment:
    """Defines an assignment
    """
    def __init__(self, name, assig_type, score, weight):
        self.name = name
        self.assig_type = assig_type
        self.score = score
        self.weight = weight

    def get_weighted_score(self):
        return (self.score / 100) * self.weight
