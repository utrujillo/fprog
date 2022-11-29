# pip install pandas
# pip install openpyxl
import pandas as pd

FILE = 'datos.xlsx'

# Crear datos
usuarios = pd.DataFrame([])

usuario = {
  'id': 1,
  'nombre': 'Juan',
  'apellidos': 'Penas'
}

usuarios = pd.concat(
  [ usuarios, pd.DataFrame([usuario])], 
  ignore_index=True)

usuarios.to_excel(FILE)

#  Leer datos
# usuarios = pd.read_excel( FILE, index_col = 0 )
# print( usuarios )