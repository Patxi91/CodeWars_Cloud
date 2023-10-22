class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs

def sort_animals(lst):
    # Sort the lst using a custom sorting key
    sorted_list = sorted(lst, key=lambda animal: (animal.number_of_legs, animal.name))
    return sorted_list
