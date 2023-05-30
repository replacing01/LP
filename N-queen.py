#N_queen           
def isSafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 1:
            return False
    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1
    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1
    return True
def nQueen(arr, x, n):
    if x >= n:
        return True
    for col in range(n):
        if isSafe(arr, x, col, n):
            arr[x][col] = 1
            if nQueen(arr, x + 1, n):
                return True
            arr[x][col] = 0
    return False
n = int(input("Enter the value of n for n x n board: "))
arr = [[0] * n for _ in range(n)]
print("\nThe solution for", n, "Queens Problem is:\n")
if nQueen(arr, 0, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print("\nNote: Here 1 represents that a Queen is placed at that position.")
