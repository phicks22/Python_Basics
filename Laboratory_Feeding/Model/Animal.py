import string


class Animal:

    def __init__(self, common_name: string, genus: string, species: string, max_length: float, max_age: int):
        self.velocity = 0
        self.common_name = common_name
        self.genus = genus
        self.species = species
        self.max_length = max_length
        self.max_age = max_age

    def print_identity(self):
        print('Common name: ', self.common_name)
        print('Scientific name: ', self.genus, self.species)
        print('Max length: ', self.max_length, 'feet')
        print('Max age: ', self.max_age, 'years')

    def faster(self):
        self.velocity += 1

    def slower(self):
        if self.velocity > 0:
            self.velocity -= 1
