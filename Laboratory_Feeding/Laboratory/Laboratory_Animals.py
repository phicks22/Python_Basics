from Model.Shark import Shark
from Model.Snake import Snake
from Model.Snail import Snail


class Laboratory_Animals:

    def __init__(self):
        self.animal_dict = dict()

# animal_obj = properties of class Animal - (common_name, genus, species, ...)
    def add_animal(self, aquarium_key, animal_obj):
        if aquarium_key not in self.animal_dict.keys():
            aquarium = list()
            aquarium.append(animal_obj)
            self.animal_dict[aquarium_key] = aquarium
        else:
            existing_list = self.animal_dict.get(aquarium_key)
            existing_list.append(animal_obj)
            self.animal_dict[aquarium_key] = existing_list

#TODO need function to read Parkers_Lab to create the initial dictionary

lab = Laboratory_Animals()
horn = Shark('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25, 'Temperate')
swell = Shark('Swell Shark', 'Cephaloscyllium', 'ventriosum', 3.5, 10, 'Temperate')
corn = Snake('Corn Snake', 'Pantherophis', 'guttatus', 6.0, 8, False)
moon = Snail('Moon Snail', 'Neverita', 'reclusiana', 5.5, 7, False)
lab.add_animal('Shark', horn)
lab.add_animal('Shark', swell)
lab.add_animal('Snake', corn)
lab.add_animal('Snail', moon)

for key in lab.animal_dict.keys():
    print(key, '===', lab.animal_dict.get(key)[0])
