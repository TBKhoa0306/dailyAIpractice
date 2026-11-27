matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sum of main diagonal
sum_main_diagonal = sum(matrix[i][i] for i in range(len(matrix)))

#WAY 1: list comprehension
number_of_row = len(matrix)
number_of_col = len(matrix[0])
# Transpose the matrix
transpose_matrix = [[matrix[i][j] for i in range(number_of_row)] for j in range(number_of_col)]

print("Sum of the main diagonal: ", sum_main_diagonal)
print("The transposition matrix: ", transpose_matrix)

#WAY 2: 
# result_matrix = []
# for i in range(number_of_row):
#     tmp_matrix = []
#     for j in range(number_of_col):
#         tmp_matrix.append(matrix[j][i])
#     result_matrix.append(tmp_matrix)

# print(result_matrix)