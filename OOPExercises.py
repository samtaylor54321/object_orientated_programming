################################## NOTES ON OBJECT ORIENTATED PROGRAMMING ##############################

### Class Notes

# Class are nouns

# Attributes are adjectives (these can be at an instance level or at a  class level)
# and describe the properties of a particular class

# Methods are verbs (functions which can be applied to specific instances of a given class). These can either be instance based
# in which they depend on the self parameter or they can be @staticmethods which don't depend on broader attributes or methods.
# Self allows instance attributes to persist between methods, they disappear otherwise and this isn't helpful.

# abstraction and encapsulation means hiding functionality 'under the hood' and just providing the user with the high
# level details

# child class will inherit methods and attributes from a parent class. On a single level this comes from a base class but a derived
# class can inherit from mutliple base classes. This can be chained together across multiple levels.

# Attributes and methods of classes can be Public, Protected or Private. Public can be used by anything. Protected means that only base class and
# derived classes can use it and are identified by an _ whilst Private can only be used by the class itself and not
# derived classes and are signified by __ .

# It is possible to overide the methods and attributes of base classes in derived classes. Super() returns control to the
# base class again rather than the derived class.

# In the diamond problem, ordering is important and primacy of ordering and method resolution order gives priorities.

# Overload refers to using special operators for new cases (addition is an example of this) and allows objects
# of a class to interact with one another

# Abstract Base Class ensures consistancy across different classes. This can be instantiated itself and also
# prevents derived classes from being created without it

### Exercise One

# Write and object oriented program that performs the following tasks:
# 1. Define a class called "Employee" and create an instance of that class
# 2. Create an attribute called name and assign it with a value
# 3. Change the name you previously defined within a method and call this method by making use of the object you
#    created

class Employee:
    name = "Sam"
    def updateName(self, name):
        self.name = name

employeeOne = Employee()
print(employeeOne.name)
employeeOne.updateName("Frank")
print(employeeOne.name)

### Exercise Two

# Write an object oriented program to create a precious stone. Not more than 5 precious stones can be held in possession at a
# given point of time. If there are more than 5 precious stones, delete the first stone and store the new one.

class preciousStones:
    current_stones = 0
    stones = []
    def __init__(self, name):
        # what stone is the instance of this class
        self.name = name
        # add one to current stones
        preciousStones.current_stones += 1
        #
        if preciousStones.current_stones <=5:
            preciousStones.stones.append(self)
        else:
            del preciousStones.stones[0]
            preciousStones.stones.append(self)

    @staticmethod
    def DisplayStones():
        for stone in preciousStones.stones:
            print(stone.name, end = ' ')
        print()

stoneOne = preciousStones("Diamond")
stoneTwo = preciousStones("Ruby")
stoneThree = preciousStones("Emerald")
stoneFour = preciousStones("Saphire")
stoneFive = preciousStones("Onyx")
stoneFive.DisplayStones()
stoneSix = preciousStones("Amber")
stoneFive.DisplayStones()

### Exercise Three

# Similar to a library management system, write a program to provide layers of abstraction for a car rental system.
# Your program should perform the following:

# 1. Hatchback, Sedan, SUV should be type of cars that are being provided for rent
# 2. Cost per day: Hatchback - $30, Sedan - $50, SUV - $100
# 3. Give a prompt to the customer asking him the type of car and the number of days he would like to borrow and provide the
# fare details to the user.

class rentalCompany:
    def __init__(self, availableCars):
        self.cars = availableCars

    def printAvailableCars(self):
        print("Cars currently available and daily rate:  ")
        print('Ford Fiesta: £', self.cars['Ford Fiesta'])
        print('Ford Mondeo: £', self.cars['Ford Mondeo'])
        print('Ford Kuga: £', self.cars['Ford Kuga'])

    def printTotalRental(self, daysRequired, typeOfCar):
        return self.cars[typeOfCar * numberOfDays]

fordGarage = rentalCompany({'Ford Fiesta': 30, 'Ford Mondeo': 50, 'Ford Kuga': 100})
while True:
    print("Press 1 to list vehicles")
    print("Press 2 to select vehicle")
    print("Press 3 to exist")
    userChoice = int(input())
    if userChoice == 1:
        fordGarage.printAvailableCars()
    elif userChoice == 2:
        print("Which car would you like to borrow")
        typeOfCar = input()
        print("How long would you like to borrow it for")
        daysRequired = input()
        fare = fordGarage.printTotalRental()
        print("Total price is £", fare)
        print("Thank you")
    elif userChoice == 3:
        quit()

### Exercise Four

# Write an object oriented program that performs the following tasks:
# 1. Create a class called Chair from the base class Furniture
# 2. Teakwood should be the type of furniture that is used by all furnitures by default
# 3. The user can be given an option to change the type of wood used for chair if he wishes to
# 4. The number of legs of a chair should be a property that should not be altered outside the class

class Furniture:
    typeOfFurniture = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        self._numberOfLegs = 4
        print("This chair as {} legs and is made of {}".format(self._numberOfLegs, self.typeOfFurniture))

    def updateWood(self, typeOfWood):
        self.typeOfFurniture = typeOfWood
        print("This chair as {} legs and is made of {}".format(self._numberOfLegs, self.typeOfFurniture))

chair = Chair()
chair.updateWood("Oak")

### Exercise Five

# Create a class called Square and perform the following tasks -
# (i) Create two objects for this class squareOne and squareTwo
# (ii) Find the result of side of squareOne to the power of side of squareTwo
# Example: If squareOne has length of 2cm each side and squareTwo has a length of 4cm each side, squareOne **
# squareTwo should return 16, which is 2 to the power of 4.
# Hint: While performing SquareOne ** SquareTwo, you need to overload __pow__() method

class Square:
    sides = 4
    def __init__(self, length):
        self.length = length

    def __pow__(SquareOne, squareTwo):
        return(SquareOne.length ** squareTwo.length)

squareOne = Square(2)
squareTwo = Square(4)
print("The result of the side of Sqaure one to the power of Square two is", squareOne ** squareTwo)
