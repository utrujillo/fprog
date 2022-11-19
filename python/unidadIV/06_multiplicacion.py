matrixA = [
  [1, 4, 4],
  [2, 4, 3]
]

matrixB= [
  [4, 5],
  [2, 4],
  [4, 5],
]

rowMatrixA = len(matrixA)
rowMatrixB = len(matrixB) 

matrixACompare = True
columnsA = 0
for index in range(0, len(matrixA)):
  if( index == 0 ):
    columnsA = len(matrixA[index])
  else:
    if( columnsA != len(matrixA[index]) ):
      matrixACompare = False

matrixBCompare = True
columnsB = 0
for index in range(0, len(matrixB)):
  if( index == 0 ):
    columnsB = len(matrixB[index])
  else:
    if( columnsB != len(matrixB[index]) ):
      matrixBCompare = False

if( matrixACompare == True and matrixBCompare == True ):
  print( 'Matrix a ', rowMatrixA, 'x', columnsA )
  print( 'Matrix a ', rowMatrixB, 'x', columnsB )

