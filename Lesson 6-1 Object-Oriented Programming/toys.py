class Toy:
    description: str
    lovable: float
    
    def __init__(self, description: str, lovable: float):
        self.description = description
        self.lovable = lovable

    def getDescription(self) -> str:
        return self.description

    def getLovable(self) -> float:
        return self.lovable

    def setDescription(self, description: str):
        self.description = description

    def setLovable(self, lovable: float):
        self.lovable = lovable


    def __repr__(self) -> str:
        return '{0} (love factor: {1})'.format(self.description, self.lovable)

class ToyChest:
    toys: list

    def __init__(self):
        self.toys = []

    def addToy(self, toy: Toy):
        self.toys.append(toy)

    def findToy(self, descr: str) -> Toy:
        for toy in self.toys:
            if descr == toy.getDescription():
                return toy

        return None

    def loveMore(self, descr: str):
        toy = self.findToy(descr)
        if toy != None:
            toy.lovable += 1     

    def disposeToy(self, descr: str):
        i = 0
        while i < len(self.toys):
            if descr == self.toys[i].description:
                del self.toys[i]
            else:
                i += 1

    def disposeUnlovedToys(self):
        i = 0
        while i < len(self.toys):
            if self.toys[i].lovable < 3:
                del self.toys[i]
            else:
                i += 1

    def __repr__(self):
        return str(self.toys)


chest = ToyChest()

mytoy = Toy('G.I. Joe', 1)
chest.addToy(Toy('G.I. Joe', 1))
chest.addToy(Toy('Baby', 9))
chest.addToy(Toy('Teddy Bear', 7))

chest.loveMore('Teddy Bear')


print(str(chest))
