
class Laboratory_Animals:

    def __init__(self):
        self.animal_dict = dict()

    def add_animal(self, aquarium_key, animal_obj):
        if aquarium_key not in self.animal_dict.keys():
            aquarium = list()
            aquarium.append(animal_obj)
            self.animal_dict[aquarium] = aquarium
        else:
            existing_list = self.animal_dict.get(aquarium_key)
            existing_list.append(animal_obj)
            self.animal_dict[aquarium_key] = existing_list
