lista = [ 7, 2, 8, 5, 10, 17 ,4, 8, 4, 25 ]

for pasada in range(0, len(lista) - 1):
  for indice in range(0, len(lista) - 1):
    if(lista[indice] > lista[indice + 1] ):
      aux = lista[indice]
      lista[indice] = lista[indice + 1]
      lista[indice + 1] = aux
  print( "Pasada: ", pasada, " arreglo: ", lista )