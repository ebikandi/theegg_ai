# Tarea 23

# Algoritmo del solitario

Esta tarea trata sobre entender el sistema de cifrado del [solitario](http://www.ugr.es/~anillos/textos/pdf/2011/EXPO-1.Criptografia/02a14.htm#:~:text=Solitaire%20es%20un%20cifrado%20%22stream,modo%20%22output%2Dfeedback%22.&text=Para%20cifrar%2C%20se%20genera%20una,m%C3%B3dulo%2026%2C%20del%20texto%20cifrado.) e implementar lógica que cifre y descifre un mensaje basandose en ese algoritmo.

Al correr el programa en **app.py** el prompt le pedirá al usuario que escriba un mensaje a cifrar y le mostrará dos resultados:
  - El mensaje resultado de cifrar el valor introducido con el solitario.
  - El resultado de descifrar el cifrado anterior para compararlo con el valor introducido.

# Solucion

La solución implementada se basa en los pasos descritos en [este post](http://www.ugr.es/~anillos/textos/pdf/2011/EXPO-1.Criptografia/02a14.htm#:~:text=Solitaire%20es%20un%20cifrado%20%22stream,modo%20%22output-feedback%22.&text=Para%20cifrar,%20se%20genera%20una,m%C3%B3dulo%2026,%20del%20texto%20cifrado.) y cada paso explicado en el post, esta reflejado a modo de función en el código. 

# Ejecución

El programa esta escrito usando el compilador de **Python 3.8.3** por lo que se aconseja usar esa versión para ejecutarla. Para eso es suficiente ir a la carpeta de la tarea en una ventana de terminal y teclear `python3 app.py`.

El prompt empezará a imprimir el mensaje para pedir el valora cifrar. Al introducir el valor nos dará el resultado cifrado y el mensaje originado desde la cadena cifrada.