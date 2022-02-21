N = int(input())

for i in range(1, 1+N):
    if i % 2 != 0:
        print(N * "* ")
    else:
        print(N * " *")