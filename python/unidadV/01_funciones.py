def saludo():
  print('Ya falta poco, aguanten!!')

def saludo2(cadena):
  print(cadena)

def suma():
  print(10+5)

def suma_parametros(numero1, numero2):
  print( numero1 + numero2 )

def suma_parametros_regreso(numero1, numero2):
  return numero1 + numero2

# suma_parametros(10, 5)
# suma_parametros(100, 50)

suma = suma_parametros_regreso(1,1)
print('La suma de tus elementos es ', suma)

# saludo2('hOLA MUNDO NUEVAMENTE')
# saludo2(10)

# suma()
# saludo()
# print('Hola mundo')
# saludo()