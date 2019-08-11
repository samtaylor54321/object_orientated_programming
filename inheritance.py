class Furniture:
    def __init__(self):
        self._typeOfWood = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        # super is used to call base class methods. You will learn more about super in next section.
        # Here we are calling the init of our base class to initialise the type of wood as Teakwood
        super().__init__()
        self.__numberOfLegs = 4

    def setWoodType(self, typeOfWood):
        self._typeOfWood = typeOfWood

    def displayChairSpecification(self):
        print("This chair is made of {} and has {} legs".format(self._typeOfWood, self.__numberOfLegs))

chair = Chair()
print("Would you like to change the type of wood from Teakwood? Y/N")
userChoice = input()
if userChoice is 'Y':
    print("Enter the type of wood you would like your chair to be made of")
    typeOfWood = input()
    chair.setWoodType(typeOfWood)
chair.displayChairSpecification()
