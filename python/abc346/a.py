n = int(input())
a = list(map(int, input().split()))

b = []

for i in range(n-1):
    tmp_b = a[i] * a[i+1]
    b.append(tmp_b)

b_string = " ".join(str(i) for i in b)

print(b_string)
