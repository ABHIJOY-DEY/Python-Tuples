n = int(input())
arr = list(map(int,input().split()))
result = []
product = 1
for x in arr:
    product*=x
    result.append(product)
print(tuple(result))