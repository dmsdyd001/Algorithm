num = [int(input()) for i in range(9)]
max_num = max(num)

print(max_num, num.index(max_num)+1, sep="\n")

