matriz = [
  [1, 5, 10, 20],
  [1, 5],
  [4, 2, 90, 5]
]

# Forma A es utilizar for each
for row in matriz:
  print('Fila :', end=' ')
  for col in row:
    print(col, end=' ')
  print()

# Forma B es utilizar un for in
print("===== Segunda forma =======")
for row in range(0, len(matriz)):
  for col in range(0, len(matriz[row])):
    print(matriz[row][col], end=' ')
  print()