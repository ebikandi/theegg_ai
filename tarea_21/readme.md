# Tarea 21

# Calculo de la fraccion irreducible

## Solución

Para esta tarea de ha optado por usar Python para empezar a familiarizarse con el lenguaje. La solución se consigue siguiendo la [**explicación** presentada en el enunciado](http://www.nachocabanes.com/retos/reto.php?n=013). Es decir:

1. **Convertir la fracción en entero.** Como la fracción tendrá como mucho 4 decimales, esto se consigue multiplicando la fraccion po 10.000. A este número le llamaremos el entero.

2. **Encontrar el Máximo Común Divisor (MCD) entre el entero y 10.000.** Empezar desde el entero que se ha conseguido multiplicando la fracción e ir restando 1 hasta encontrar el primer número cuyo remanente con el entero y 10.000 sea 0. (Esto se podía haber hecho usando la función Math.gcd() de Python, pero para el ejercicio se ha optado por hacerlo a mano.)

3. **Dividir el entero y 10.000 con el MCD para conseguir el numerador y denominador respectivamente**.

## Programa

El programa está escrito en Python. Se divide en 3 partes:

1. Función para calcular el Máximo Común Divisor.

2. Función principal que:

   Recibe el número como argumento, hequea que esta dentro del rango aceptado [0.0001, 0.9999] y lo convierte en entero.

   LLama a la función para conseguir el MCD y recibe el resultado.

   Divide el entero y 10.000 para conseguir la fracción irreducible e imprime el resultado.

3. Bucle infinito para ir pidiento los números al usuario e imprimir el resultado.

## Ejecución

El programa esta escrito usando el compilador de **Python 3.8.3** por lo que se aconseja usar esa versión para ejecutarla. Para eso es suficiente ir a la carpeta de la tarea en una ventana de terminal y teclear `python3 app.py`.

El prompt empezará a imprimir el mensaje para pedir un número para hacer el calculo. Introduciendo 1 pararemos el programa.

```console
╰─$ python3 app.py
Mete un número entre [0.0001, 0.9999]: (1 para salir)
0.376
Fraccion minima de 0.3760: 47/125
Mete un número entre [0.0001, 0.9999]: (1 para salir)
1
```
