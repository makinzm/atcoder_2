n,t,a = map(int, input().split())

remain = n - t - a

if t > remain + a or a > remain + t:
    print("Yes")
else:
    print("No")
