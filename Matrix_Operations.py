import numpy as np

# Define two 3x3 matrices with mixed positive and negative numbers
A = np.array([[ 4, -7,  2],
              [-3,  5,  9],
              [ 8, -6, -1]])

B = np.array([[-2,  3, -5],
              [ 7, -8,  4],
              [-9,  1,  6]])

# Matrix addition
matrix_add = A + B

# Matrix subtraction
matrix_sub = A - B

# Matrix multiplication (dot product)
matrix_mult = A @ B # the same as "np.dot(A, B)"

# Print results
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nA + B:")
print(matrix_add)
print("\nA - B:")
print(matrix_sub)
print("\nA * B:")
print(matrix_mult)