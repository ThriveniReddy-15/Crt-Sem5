from collections import defaultdict

def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    diagonals = defaultdict(list)

    # Store elements of each diagonal
    for r in range(rows):
        for c in range(cols):
            diagonals[r - c].append(mat[r][c])

    # Sort each diagonal
    for key in diagonals:
        diagonals[key].sort(reverse=True)

    # Put sorted elements back
    for r in range(rows):
        for c in range(cols):
            mat[r][c] = diagonals[r - c].pop()

    return mat

