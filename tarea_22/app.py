from cow import Cow  # Custom class

def max(x, y):
    if(x > y):
        return x
    return y

def getMaxProduction(cowsInMarket, maxWeight, index, actualMilk, actualWeight):
    if(index < len(cowsInMarket)):
        actualCow = cowsInMarket[index]
        if(actualWeight + actualCow.weight > maxWeight):
            return getMaxProduction(cowsInMarket, maxWeight, index +1 , actualMilk, actualWeight)
        else:
            return max(getMaxProduction(cowsInMarket, maxWeight, index +1, actualMilk + actualCow.milk, actualWeight + actualCow.weight),
                getMaxProduction(cowsInMarket, maxWeight, index +1, actualMilk, actualWeight))
    return actualMilk


if __name__ == '__main__':
    cowsInMarket = [
        Cow(1, 360, 40),
        Cow(2, 250, 35),
        Cow(3, 400, 43),
        Cow(4, 180, 28),
        Cow(5, 50, 12),
        Cow(6, 90, 13),
    ]
    # cowsInMarket = []
    boughtCows = []
    weightToCarry = 0
    milkProduction = 0
    # totalCows = int(input("¿Cuantas vacas hay en Tolosa?\n"))
    maxWeight = 700 #int(input("¿Cuanto peso puedes transportar?\n"))
    # for i in range(1, totalCows+1):
    #     weight = int(input("Introducir peso vaca %d:\n" % i))
    #     milk = int(input("Introducir cantidad de leche de la vaca %d:\n" % i))
    #     newCow = Cow(i, weight, milk)
    #     cowsInMarket.append(newCow)

    
    
    # ir cogiendo las vacas y calculando la produccion de leche hasta llegar al peso maximo
    maxProduction = getMaxProduction(cowsInMarket, maxWeight, 0, 0, 0)
    print("MAX: %d" % maxProduction )    

    # Imprimir resultado
    # print("\n******************************************\n")
    # print("Produccion maxima de leche: %d" % milkProduction)
    # print("Peso a llevar: %d; Peso maximo estipulado: %d" %
    #       (weightToCarry, maxWeight))
    # print("Vacas compradas:")
    # for c in boughtCows:
    #     c.printInfo()
    # print("Todas las vacas:")
    # for c in cowsInMarket:
    #     c.printInfo()
