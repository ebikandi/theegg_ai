# from random as r  # Random number generators
from cow import Cow  # Custom class

# seed random number generator

if __name__ == '__main__':
    cowsInMarket = []
    boughtCows = []
    weightToCarry = 0
    milkProduction = 0
    totalCows = int(input("¿Cuantas vacas hay en Tolosa?\n"))
    maxWeight = int(input("¿Cuanto peso puedes transportar?\n"))
    for i in range(1, totalCows+1):
        weight = int(input("Introducir peso vaca %d:\n" % i))
        milk = int(input("Introducir cantidad de leche de la vaca %d:\n" % i))
        newCow = Cow(i, weight, milk)
        cowsInMarket.append(newCow)

    # ordenar las vacas por el ratio en orden descendente
    cowsInMarket.sort(key=lambda c: c.ratio, reverse=True)
    # ir cogiendo las vacas y calculando la produccion de leche hasta llegar al peso maximo
    for c in cowsInMarket:
        remainingWeight = maxWeight - weightToCarry
        if c.weight > remainingWeight:
            continue
        else:
            boughtCows.append(c)
            milkProduction += c.milk
            weightToCarry += c.weight
            if weightToCarry == maxWeight:
                break

    # Imprimir resultado
    print("\n******************************************\n")
    print("Produccion maxima de leche: %d" % milkProduction)
    print("Peso a llevar: %d; Peso maximo estipulado: %d" %
          (weightToCarry, maxWeight))
    print("Vacas compradas:")
    for c in boughtCows:
        c.printInfo()
    print("Todas las vacas:")
    for c in cowsInMarket:
        c.printInfo()
