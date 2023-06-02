def calculate_submatrix_sum(matrix, p, q, r, s):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create the prefix sum matrix
    prefix_sum = [[0] * cols for _ in range(rows)]
    print(prefix_sum)

    # Calculate the prefix sum
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                prefix_sum[i][j] = matrix[i][j]
            elif i == 0:
                prefix_sum[i][j] = matrix[i][j] + prefix_sum[i][j-1]
            elif j == 0:
                prefix_sum[i][j] = matrix[i][j] + prefix_sum[i-1][j]
            else:
                prefix_sum[i][j] = matrix[i][j] + prefix_sum[i -
                                                             1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

    # Calculate the sum of submatrix
    sum_submatrix = prefix_sum[r][s] - prefix_sum[r][q -
                                                     1] - prefix_sum[p-1][s] + prefix_sum[p-1][q-1]

    return sum_submatrix


# Test the function
matrix = [
    [0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4]
]
p, q = 1, 1
r, s = 3, 3
submatrix_sum = calculate_submatrix_sum(matrix, p, q, r, s)
print("Sum is", submatrix_sum)
