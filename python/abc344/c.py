n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))

available_set = set()
for a_i in a:
    for b_i in b:
        for c_i in c:
            available_set.add(a_i + b_i + c_i)

q = int(input())
x = list(map(int, input().split()))

for i in range(q):
    if x[i] in available_set:
        print("Yes")
    else:
        print("No")
