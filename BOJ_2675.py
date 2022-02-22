
T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    change_w = ""
    for j in S:
        change_w += j*R
    print(change_w)