n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(" "))))
index_n = int(input())
index_m = int(input())
print(matrix[index_n][index_m])
neighbors = []
if index_n < (n - 1):
    neighbors.append(matrix[index_n + 1][index_m])
if index_m < (m - 1):
    neighbors.append(matrix[index_n][index_m + 1])
if index_n != 0:
    neighbors.append(matrix[index_n - 1][index_m])
if index_m != 0:
    neighbors.append(matrix[index_n][index_m - 1])

for i in sorted(neighbors):
    print(i, end=" ")
