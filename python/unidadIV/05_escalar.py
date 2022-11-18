matrix = [
  [1, 5, 10, 20],
  [1, 5],
  [4, 2, 90, 5]
]

newMatrix = []

escale = 2

for index in range(0, len(matrix)):
  newMatrix.append([])
  for col in range(0, len(matrix[index])):
    newMatrix[index].append( matrix[index][col] * escale )

print(matrix)
print( newMatrix )