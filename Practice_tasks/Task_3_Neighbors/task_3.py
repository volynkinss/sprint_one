n = int(input())  # number of lines
m = int(input())  # number of coloumns
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(" "))))  # filling matrix by user entered
index_n = int(input())  # coordinate of line by user for required number
index_m = int(input())  # coordinate of coloumn by user for required number


def neighborhood_count(n, m, index_n, index_m):
    neighbors = (
        []
    )  # list of neighbors of the required number to be filled and returned after func
    if index_n < (n - 1):
        neighbors.append(matrix[index_n + 1][index_m])
    if index_m < (m - 1):
        neighbors.append(matrix[index_n][index_m + 1])
    if index_n != 0:
        neighbors.append(matrix[index_n - 1][index_m])
    if index_m != 0:
        neighbors.append(matrix[index_n][index_m - 1])
    return neighbors


for i in sorted(
    neighborhood_count(n, index_n, index_m)
):  # output result with " " for user
    print(i, end=" ")
