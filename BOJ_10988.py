#슬라이싱 사용

t = input()
if t == t[::-1]:
  print(1)
else:
  print(0)

#한줄 코드
# print(1 if t == t[::-1] eles 0)
# print(int(t == t[::-1]))

#반복문 사용
word = input()
cnt = 0

for i in range(len(word)):
    if word[i] == word[len(word)-1-i]:
        cnt += 1
    else:
        cnt += 0
if cnt == len(word):
    print(1)
else:
    print(0)