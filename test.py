# input 연습
a = int(input())
b = float(input())
c = input()

print(type(a), type(b), type(c))

# map 연습
d, e = map(int, input())
f, g = map(int, input().split())

print(d, e, type(d), type(e))
print(f, e, type(f), type(e))

# print 연습
print(d, e, sep="\n")
print(d, e, end="&")
