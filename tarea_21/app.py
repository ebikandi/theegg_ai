def get_gcd(num, denom):
  div = num
  while div in range(num + 1):
    if num % div == 0 and denom % div == 0:
      return div
    div -= 1

def minimum_fraction(num):
  if 0 < num < 1:
    denom = 10000
    multiplied = int(num * denom)
    # MCD se puede calcular usando gcd() pero para el ejercicio lo calcularemos a mano.
    divisor = get_gcd(multiplied, denom)
    min_num = multiplied/divisor
    min_denom = denom/divisor
    print("Fraccion minima de %f: %d/%d" %(num, min_num, min_denom))
  else:
    raise Exception()


# minimum_fraction(0.376)
while True:
  try:
    number = float(input("Mete un número entre 0.0001-0.9999: (1 para salir):"))
    if int(number) == 1:
      break
    else:
      minimum_fraction(number)
  except:
    print("Mal input")
    continue
  