""" En este desafío, debes dibujar un triángulo equilatero usando bucles.

Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, respectivamente. Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable. """

def print_triangle(size, character):
  triangle = ''
  for i in range(size):
    triangle += " " * (size - i - 1)
    triangle += character  + character * (2 * i)
    if i != size - 1:
        triangle += "\n"
  return triangle
  pass
print(print_triangle(3,"*"))