""" 
En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.

Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista, la función debe devolver None. Si hay más de un palíndromo con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.

Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante como hacia atrás.

Ejemplo 1:


Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

Output: "racecar"

Ejemplo 2:


Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])

Output: None 
"""
""" solucion de platzi
def find_largest_palindrome(words):
   largest = 0
   palindrome = ""

   for word in words:
      if word == word[::-1]:
         if len(word) > largest:
            palindrome = word
            largest = len(word)
      
   return palindrome if palindrome else None
   pass """

#intentar solucionar con list comprehension
def find_largest_palindrome(words):
  
  pass