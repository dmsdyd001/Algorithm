
	# a.너 하얀 칸이니? b. 너 말 있니?

chess = [list(input()) for i in range(8)]
count = 0

for i in range(8):
	for j in range(8):
		if (i % 2 == j % 2) and (chess[i][j] == "F"):
			count += 1
print(count)