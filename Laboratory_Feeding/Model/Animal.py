import string


class Shark:

    def __init__(self, common_name: string, genus: string, species: string, max_length: float, max_age: int or string):
        self.velocity = 0
        self.common_name = common_name
        self.genus = genus
        self.species = species
        self.max_length = max_length
        self.max_age = max_age
        self.shark_list = []

    def print_identity(self):
        print('Common name: ', self.common_name)
        print('Scientific name: ', self.genus, self.species)
        print('Max length: ', self.max_length, 'feet')
        print('Max age: ', self.max_age, 'years')

    # How do I print as a list of all the sharks with all of their attributes???

    def faster(self):
        self.velocity += 1

    def slower(self):
        if self.velocity > 0:
            self.velocity -= 1


horn = Shark('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25)
swell = Shark('Swell Shark', 'Cephaloscyllium', 'ventriosum', 3.5, 10)
white = Shark('Great White Shark', 'Carcharadon', 'carcharias', 20.0, 70)
shortfin_mako = Shark('Shortfin Mako', 'Isurus', 'oxyrinchus', 12.0, 30)
longfin_mako = Shark('Longfin Mako', 'Isurus', 'paucus', 14.0, 'Unknown')
lemon = Shark('Lemon Shark', 'Negaprion', 'bevriostris', 11.0, 27)
bull = Shark('Bull Shark', 'Carcharhinus', 'leucas', 11.5, 14)
great_hammer = Shark('Great Hammerhead Shark', 'Sphyrna', 'mokarran', 20.0, 35)
nurse = Shark('Nurse Shark', 'Ginglymostoma', 'cirratum', 14.0, 35)
porbeagle = Shark('Porbeagle Shark', 'Lamna', 'nasus', 6.6, 65)
black_tip = Shark('Blacktip Reef Shark', 'Carcharhinus', 'melanopterus', 5.2, 13)