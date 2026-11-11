# You are using Python
size = int(input())
a = list(map(int,input().split()))
n = int(input())

i = n-1
while i<len(a):
    a.pop(i)
    i += n-1

print(tuple(a))