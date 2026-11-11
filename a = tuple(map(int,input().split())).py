a = tuple(map(int,input().split()))
even = ()
for x in a:
    if x%2 == 0:
        even +=(x,)
print("New Tuple With Even Integers:")
print(even)