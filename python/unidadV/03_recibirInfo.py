# pip install pandas
# pip install openpyxl
import pandas as pd

def menu():
  menu = '''
  ********* Menu Principal **********
  1.- Insertar
  2.- Leer
  3.- Actualizar
  4.- Salir

  Selecciona un numero? 
  '''
  opcion = input( menu )
  return int(opcion)

def opcion_seleccionada( opcion ):
  if( opcion == 1 ):
    insertar()
  else:
    print('Fin del proyecto')

def insertar():
  alumno = {}
  alumno['id'] = input('Ingresa el ID: ')
  alumno['nombre'] = input('Ingresa el nombre: ')
  alumno['apellidos'] = input('Ingresa los apellidos: ')
  print( alumno )

opcion = menu()
opcion_seleccionada( opcion )

