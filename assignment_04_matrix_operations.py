# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    """Reads an M x N matrix from user input line by line."""
    matrix = []
    print(f"\nEnter elements for {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ").strip().split()
                if len(row_input) != cols:
                    print(f"Error: Row must contain exactly {cols} space-separated numbers.")
                    continue
                row = [float(x) if '.' in x else int(x) for x in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid input! Please enter valid numbers.")
    return matrix


def display_matrix(matrix, title="Matrix"):
    """Displays a 2D list as a neatly aligned grid."""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{val:>4}" for val in row))


# --- OPERATION FUNCTIONS ---

def transpose_matrix(matrix):
    """Computes and returns the transpose of a given matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty N x M grid for the transposed matrix
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


def add_matrices(matrix_a, matrix_b):
    """Computes element-wise sum of two matrices of identical dimensions."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiplies an M x N matrix A by an N x P matrix B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Result matrix will be size M x P
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


# --- MAIN PROGRAM ---

def main():
    print("========================================")
    print("            MATRIX OPERATIONS           ")
    print("========================================")

    # --- PART A: Transpose ---
    print("\n--- PART A: TRANSPOSE A MATRIX ---")
    try:
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
        matrix_a = read_matrix(r, c, "Matrix A")
        
        display_matrix(matrix_a, "Original Matrix")
        transposed = transpose_matrix(matrix_a)
        display_matrix(transposed, "Transposed Matrix")
    except ValueError:
        print("Error: Rows and columns must be integers.")

    # --- PART B: Addition ---
    print("\n--- PART B: ADD TWO MATRICES ---")
    try:
        r = int(input("Enter number of rows for both matrices: "))
        c = int(input("Enter number of columns for both matrices: "))
        mat_1 = read_matrix(r, c, "Matrix 1")
        mat_2 = read_matrix(r, c, "Matrix 2")

        sum_matrix = add_matrices(mat_1, mat_2)
        display_matrix(sum_matrix, "Matrix Sum (Matrix 1 + Matrix 2)")
    except ValueError:
        print("Error: Invalid dimensions entered.")

    # --- PART C: Multiplication ---
    print("\n--- PART C: MULTIPLY TWO MATRICES ---")
    try:
        m = int(input("Enter rows for Matrix A (M): "))
        n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
        p = int(input("Enter columns for Matrix B (P): "))

        mat_a = read_matrix(m, n, "Matrix A")
        mat_b = read_matrix(n, p, "Matrix B")

        product = multiply_matrices(mat_a, mat_b)
        display_matrix(product, "Matrix Product (A × B)")
    except ValueError:
        print("Error: Invalid dimensions entered.")


if __name__ == "__main__":
    main()
