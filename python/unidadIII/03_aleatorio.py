import random

randomNumber = random.randint(0, 50)
# a - 97 hasta z - 122
randomLetter = chr( random.randint(ord('a'), ord('z')) )
# print( randomLetter )
nombre = 'Juan Penas'
nombre2 = 'Juan Penas '

print('Eliminando espacios', len(nombre2.strip()))

print('Mayusculas', nombre.upper())
print('Minusculas', nombre.lower())
print('Reemplazar a', nombre.replace('a', 'aaa '))
print('Longitud', len(nombre) )
print('Invertir', nombre[::-1])
print('Enumerar cadena', enumerate(nombre))
for index, letra in enumerate(nombre):
  print('valor', letra)