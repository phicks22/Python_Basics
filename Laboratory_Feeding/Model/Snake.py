import string
from Model.Animal import Animal


class Snake(Animal):
    pass

    def __init__(self, common_name: string, genus: string, species: string, max_length: float, max_age: int,
                 venomous):
        super().__init__(common_name, genus, species, max_length, max_age)
        self.venomous = venomous
