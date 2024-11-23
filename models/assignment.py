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
    """
    Represents an assignment with its details.
    Attributes:
        name (str): The name of the assignment.
        assig_type (str): assignment (e.g., "Formative" or "Summative").
        score (float): The score of the assignment (out of 100).
        weight (float): assignment weight (percentage of total course weight).
    """

    def __init__(self, name, assig_type, score, weight):
        """
        Initializes an Assignment instance.
        """
        self.name = name
        self.assig_type = assig_type
        self.score = score
        self.weight = weight

    def get_weighted_score(self):
        """ Calculates and return sthe weighted score of the assignment.

        Derived by multiplying the score (as a percentage)
        by the weight of the assignment. """

        return (self.score / 100) * self.weight

