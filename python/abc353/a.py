n = int(input())
h = list(map(int, input().split()))

zero = h[0]
flag = True
for i in range(n):
    if h[i] > zero:
        flag = False
        print(i + 1)
        break

if flag:
    print(-1)
