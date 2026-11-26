matrix = []
n = 3

# Input n*n matrix
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(int(input(f"Input tmp[{i}][{j}]: ")))
    matrix.extend([tmp])

# Output the matrix
print("Matrix: ")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print('\n')

# Output elements on the main diagonal
print("Elements on the main diagonal: ", end="")
sum = 0
for i in range(n):
    print(matrix[i][i], end=" ")
    sum += matrix[i][i]

# Output sum of elements on the main diagonal
print(f"\nSum of main diagonal: {sum}")
