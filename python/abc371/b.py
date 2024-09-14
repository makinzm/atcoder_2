n, m = map(int, input().split())

already_seen = set()

for _ in range(m):
    a, b = input().split()
    a = int(a) - 1
    if (a not in already_seen) and b == "M":
        print("Yes")
    else:
        print("No")
    if b == "M":
        already_seen.add(a)
