""" En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre las palabras que contienen exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas las palabras de la lista original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.

Ejemplo 1:

Input: find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

Output: ["hello", "platzi"]

Ejemplo 2:

Input: find_words_with_two_vowels(["text", "test", "python", "example"])
Output: [] """

# solucion utilizando el metodo len
words = ["hello", "Python", "world", "platzi"]
def find_words_with_two_vowels(words):
    words_with_two_vowels = [palabra for palabra in words if len([letra for letra in palabra if letra in "aeiouAEIOU"]) == 2]
    return words_with_two_vowels
    pass
#solucion usando el metodo sum
def find_words_with_two_vowels_sum(words):
    words_with_two_vowels = [palabra for palabra in words if sum([1 for letra in palabra if letra in "aeiouAEIOU"]) == 2]
    return words_with_two_vowels

print(find_words_with_two_vowels(words))
print(find_words_with_two_vowels_sum(words))