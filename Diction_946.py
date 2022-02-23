n = int(input())
dic = {}
for i in range(n):
    key, value = input().split()
    dic[key] = value
print(dic.get(input(),"Unkown Country"))