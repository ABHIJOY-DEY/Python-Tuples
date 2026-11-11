# You are using Python
n = int(input())
items = []
for i in range(n):
    data = eval(input())
    items.append(data)
treshold = int(input())
result = []
for item_id , quantities in items:
    for quantity in quantities:
        if quantity>treshold:
            result.append(quantity)
print(*result)