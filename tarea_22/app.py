from cow import Cow  # Custom class

def max(x, y):
    if(x[0] > y[0]):
        return x
    return y


# Algoritmo recursivo para calcular la produccion de leche
def getMaxProduction(cowsInMarket, maxWeight, index, actualMilk, actualWeight, boughtCows):
    if(index < len(cowsInMarket)):
        actualCow = cowsInMarket[index]
        if(actualWeight + actualCow.weight > maxWeight):
            return getMaxProduction(cowsInMarket, maxWeight, index +1 , actualMilk, actualWeight, boughtCows)
        else:
            return max(getMaxProduction(cowsInMarket, maxWeight, index +1, actualMilk + actualCow.milk, actualWeight + actualCow.weight, boughtCows[:] + [actualCow]),
                getMaxProduction(cowsInMarket, maxWeight, index +1, actualMilk, actualWeight, boughtCows))
    return [actualMilk, actualWeight, boughtCows]


if __name__ == '__main__':
    cowsInMarket = []
    totalCows = int(input("¿Cuantas vacas hay en Tolosa?\n"))
    int(input("¿Cuanto peso puedes transportar?\n"))
    for i in range(1, totalCows+1):
        weight = int(input("Introducir peso vaca %d:\n" % i))
        milk = int(input("Introducir cantidad de leche de la vaca %d:\n" % i))
        newCow = Cow(i, weight, milk)
        cowsInMarket.append(newCow)
    
    # ir cogiendo las vacas y calculando la produccion de leche hasta llegar al peso maximo
    [maxProduction, weightToCarry, boughtCows] = getMaxProduction(cowsInMarket, maxWeight, 0, 0, 0, [])
    print("MAX: %d" % maxProduction)    

    # Imprimir resultado
    print("\n******************************************\n")
    print("Produccion maxima de leche: %dl" % maxProduction)
    print("Peso a llevar: %dkg ; Peso maximo: %dkg" %
          (weightToCarry, maxWeight))
    print("Vacas compradas:")
    for bc in boughtCows:
        bc.printInfo()
    print("Todas las vacas:")
    for cm in cowsInMarket:
        cm.printInfo()
