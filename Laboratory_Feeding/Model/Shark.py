from Model.Animal import Animal
import string


class Shark(Animal):
    pass

    def __init__(self, common_name: string, genus: string, species: string, max_length: float, max_age: int or string,
                 biome: string):
        super().__init__(common_name, genus, species, max_length, max_age)
        self.biome = biome
