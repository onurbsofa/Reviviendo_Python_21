"""
En este desafío encontrarás una función llamada solution que recibe un parámetro llamado valor. Debes encontrar el tipo de dato del parámetro valor y retornarlo desde la función solution.
"""
def found_type(value):
   return type(value)

print(found_type(5))#para verlo en consola $ python3 primer_desafio.py
print(found_type("hola"))
print(found_type(5.0))
print(found_type(True))