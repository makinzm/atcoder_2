# This is wrong because I forget to consider separated kinds

n = int(input())
a = list(map(int, input().split()))

kinds = []
prev = a[0]
cnt = 1

for i in range(1, n):
    if a[i] == prev:
        cnt += 1
    else:
        kinds.append(cnt)
        cnt = 1
        prev = a[i]

if cnt > 0:
    kinds.append(cnt)

# The number of kinds of balls
f = [0 for _ in range(n)]

current_kind_index = 0
prev_index = 0
current_sum = 1

for i in range(n):
    if prev_index + kinds[current_kind_index] == i:
        current_sum += 1
        prev_index = i
        current_kind_index += 1
    f[i] = current_sum

ans = 0
# ∑∑ f[j] - f[i] = ∑∑ f[j] - (n - i + 1) * f[i] = ∑ (∑　f[j]) - (n - i + 1) * f[i])

print(f)

cumsum = [0 for _ in range(n + 1)]

for i in range(n):
    cumsum[i + 1] = cumsum[i] + f[i]

print(cumsum)

for i in range(1, n + 1):
    sum_fj = cumsum[n] - cumsum[i-1]
    sum_fi = (n - i + 1) * f[i-1]
    ans += sum_fj - sum_fi + (n - i + 1)
    print(ans, sum_fj, sum_fi)

print(ans)

