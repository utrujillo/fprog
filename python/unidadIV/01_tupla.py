# tuplas: No se pueden cambiar una vez inicializadas
tupla = (1, "a", 3.14)
print( type(tupla) )

# Listas: Si se pueden modificar de forma dinamica
lista = [1, "a", 3.14, 'b', 10]
print( type(lista) )

# Append sirve para agregar valores a la lista
lista.append('Nuevo valor')
print(lista)

# Pop,, sirve para eliminar valores en la lista
# pop(indice) 
lista.pop(1)
print(lista)

# Recorrer lista con for
# for valor in lista:
#   print('valor', valor)

# Tamanho de la lista
print( len(lista) )

# Recorrer lista con while
inicio = 0
while inicio < len(lista):
  print( lista[inicio] )
  inicio += 1

# Unir listas
lista2 = [ 'j', 'k', 'l' ]
nuevaLista = lista + lista2
print(nuevaLista)