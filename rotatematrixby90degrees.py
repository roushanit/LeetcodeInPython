def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
        
# Giving input to see output in op
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rotate(matrix)

# Print result
for row in matrix:
    print(row)
