import string


class Animal:

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


    def faster(self):
        self.velocity += 1

    def slower(self):
        if self.velocity > 0:
            self.velocity -= 1


horn = Animal('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25)
swell = Animal('Swell Shark', 'Cephaloscyllium', 'ventriosum', 3.5, 10)
white = Animal('Great White Shark', 'Carcharadon', 'carcharias', 20.0, 70)
shortfin_mako = Animal('Shortfin Mako', 'Isurus', 'oxyrinchus', 12.0, 30)
longfin_mako = Animal('Longfin Mako', 'Isurus', 'paucus', 14.0, 'Unknown')
lemon = Animal('Lemon Shark', 'Negaprion', 'bevriostris', 11.0, 27)
bull = Animal('Bull Shark', 'Carcharhinus', 'leucas', 11.5, 14)
great_hammer = Animal('Great Hammerhead Shark', 'Sphyrna', 'mokarran', 20.0, 35)
nurse = Animal('Nurse Shark', 'Ginglymostoma', 'cirratum', 14.0, 35)
porbeagle = Animal('Porbeagle Shark', 'Lamna', 'nasus', 6.6, 65)
black_tip = Animal('Blacktip Reef Shark', 'Carcharhinus', 'melanopterus', 5.2, 13)
