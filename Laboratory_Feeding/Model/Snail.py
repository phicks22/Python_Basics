import string


class Snail:

    def __init__(self, common_name: string, genus: string, species: string, max_length: float or string,
                 max_age: int or string):
        self.velocity = 0
        self.common_name = common_name
        self.genus = genus
        self.species = species
        self.max_length = max_length
        self.max_age = max_age

    def print_identity(self):
        print('Common name: ', self.common_name)
        print('Scientific name: ', self.genus, self.species)
        print('Max length: ', self.max_length, 'inches')
        print('Max age: ', self.max_age, 'years')

    def faster(self):
        self.velocity += 1

    def slower(self):
        if self.velocity > 0:
            self.velocity -= 1

moon = Snail('Moon Snail', 'Neverita', 'reclusiana', 5.5, 7)
unicorn = Snail('Angular Unicorn', 'Acanithucella', 'spirata', 'Unknown', 'Unknown')
kellets = Snail('Kellet\'s Welk', 'Kelletia', 'keletii', 6.9, 50)
chestnut = Snail('Chestnut Cowrie', 'Neobernaya', 'spadicia', 2.6, 'Unknown')