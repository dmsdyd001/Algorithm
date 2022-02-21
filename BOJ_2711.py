T = int(input())

#for i in range(T):
#    a,s = input().split()
#    a = int(a)
#    print(s[:a-1] + s[a:], sep="")

for i in range(T):
    index, word = input().split()
    index = int(index)#숫자
    print(word[:index - 1] + word[index:])