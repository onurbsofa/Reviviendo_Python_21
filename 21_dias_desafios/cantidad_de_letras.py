""" En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.
Ejemplo 1:


Input: "Hola mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
} """

def count_letters(phrase):
  dict_return = {letra: phrase.count(letra) for letra in phrase}
  return dict_return
  pass

print(count_letters("Hola mundo"))


