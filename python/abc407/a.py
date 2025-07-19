a,b = map(int,input().split())

x = a/b

x_min = int(x)
x_max = int(x) + 1

if abs(x_min - x) > abs(x_max - x):
    print(x_max)
else:
    print(x_min)

