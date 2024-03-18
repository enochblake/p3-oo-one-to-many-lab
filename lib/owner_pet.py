class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner="John Doe"):
        self.name = name
        self.pet_type = pet_type.lower()
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            print("No such pet")
            raise ValueError("No such pet")
        self._pet_type = pet_type


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("value has to be of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
        pets = self.pets()
        return sorted(pet.name for pet in pets)


owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)

print(owner.get_sorted_pets())