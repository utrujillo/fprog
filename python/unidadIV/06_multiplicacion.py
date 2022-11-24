matrixA = [
  [1, 4, 4],
  [2, 4, 3]
]

matrixB= [
  [4,],
  [2, 4],
  [4, 5],
]

rowMatrixA = len(matrixA)
rowMatrixB = len(matrixB) 

def matrixCompare(matrix):
  matrixCompare = True
  columns = 0
  for index in range(0, len(matrix)):
    if( index == 0 ):
      columns = len(matrix[index])
    else:
      if( columns != len(matrix[index]) ):
        matrixCompare = False
  return matrixCompare

matrixACompare = matrixCompare(matrixA)
matrixBCompare = matrixCompare(matrixB)

if( matrixACompare == True and matrixBCompare == True ):
  print( 'Se puede multiplicar' )
else:
  print('No se puede multiplicar')
