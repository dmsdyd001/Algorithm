l1 = input()
nl1 = [list(map(int, input().split())) for i in range(2)]
l2 = input()
nl2 = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    print([nl1[i][j]*nl2[i][j] for j in range(4)])



list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[i][j] * list_b[i][j], end=" ")
    print()