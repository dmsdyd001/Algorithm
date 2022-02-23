list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]
list_c = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        list_c[i][j] = list_a[i][j] * list_b[i][j]

for i in range(2):
    for j in range(3):
        print(list_c[i][j], end=" ")
    print()
