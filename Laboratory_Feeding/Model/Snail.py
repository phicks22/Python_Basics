from Model.Animal import Animal
import string


class Snail(Animal):
    pass

    def __init__(self, common_name: string, genus: string, species: string, max_length: float,
                 max_age: int, omnivore):
        super().__init__(common_name, genus, species, max_length, max_age)
        self.omnivore = omnivore

