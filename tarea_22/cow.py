class Cow:
    def __init__(self, id, weight, milk):
        """
        Inicializa una clase Cow (Vaca) con el peso y la capacidad de producir leche que tiene.
        A la vez, calcula el ratio. Es decir, respecto el peso que tiene, la cantidad de leche
        que puede producir. A ratio mas alto mejor, ya que significará que puede producir mas 
        leche proporcionalmente.
        """
        self.id = id
        self.weight = weight
        self.milk = milk
        self.ratio = milk/weight

    def printInfo(self):
        print("Vaca %d de %dkg que produce %dl. Ratio: %.3f" %
              (self.id, self.weight, self.milk, self.ratio))
