
a = list(map(int,input().split()))
index = int(input())
value = int(input())

a[index] = value
print (tuple((map(str,a))))