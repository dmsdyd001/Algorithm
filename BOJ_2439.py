#T = int(input())
#for i in range(1, T+1):
#    print((T-i)*" "+(i)*"*")


#T = int(input())
#for i in range(1, T+1):
#    print(" "*(T-i),"*"*i)


n = int(input()) #5
#for i in range(n):
#    print("*" * (i + 1))


for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))
    #전체갯수에서 -를 하여 공백을 계산해준다