class Cow:
    def __init__(self, id, weight, milk):
        self.id = id
        self.weight = weight
        self.milk = milk

    def printInfo(self):
        print("Vaca %d de %dkg que produce %dl" %
              (self.id, self.weight, self.milk))
