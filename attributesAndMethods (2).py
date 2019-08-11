class PreciousStone:
    numberOfPreciousStones = 0
    preciousStoneCollection = []
    def __init__(self, name):
        self.name = name
        # Increment the number of preciousStones
        PreciousStone.numberOfPreciousStones += 1
        # Append the precious stone to the list if total number of stones are less than 5
        if PreciousStone.numberOfPreciousStones <= 5:
            PreciousStone.preciousStoneCollection.append(self)
        else:
            # If more than 5 stones are present, delete the first one and store the new one
            del PreciousStone.preciousStoneCollection[0]
            PreciousStone.preciousStoneCollection.append(self)

    @staticmethod
    def displayPreciousStones():
        for preciousStone in PreciousStone.preciousStoneCollection:
            print(preciousStone.name, end = ' ')
        print()

preciousStoneOne  = PreciousStone("Ruby")
preciousStoneTwo  = PreciousStone("Emerald")
preciousStoneThree  = PreciousStone("Sapphire")
preciousStoneFour  = PreciousStone("Diamond")
preciousStoneFive  = PreciousStone("Amber")
preciousStoneFive.displayPreciousStones()
preciousStoneSix = PreciousStone("Onyx")
# Print all the stones after deleting the first stone
preciousStoneSix.displayPreciousStones()
