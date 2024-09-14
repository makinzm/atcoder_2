from more_itertools import distinct_permutations

debug = False

n = int(input())

m_g = int(input())
g_edge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m_g)]
g = [ [ False for _ in range(n) ] for _ in range(n)]
for i in range(m_g):
    a, b = g_edge[i]
    g[a][b] = True
    g[b][a] = True

m_h = int(input())
h_edge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m_h)]
h = [ [ False for _ in range(n) ] for _ in range(n) ]
for i in range(m_h):
    a , b = h_edge[i]
    h[a][b] = True
    h[b][a] = True

a = [list(map(int, input().split())) for _ in range(n-1)]
price = [ [ 0 for _ in range(n) ] for _ in range(n)]

for i in range(n-1):
    for j in range(n - i - 1):
        price[i][i+1+j] = a[i][j]
        price[i+1+j][i] = a[i][j]

ans = n * 10 ** 7

# O(10^6) ~ 8^2 x 8!
for permutation in distinct_permutations(range(n)):
    amount = 0
    for i in range(n):
        for j in range(n):
            if h[permutation[i]][permutation[j]] != g[i][j]:
                amount += price[permutation[i]][permutation[j]]
    amount //= 2
    if debug:
        print(f"{amount=}, {permutation=}")
    ans = min(amount, ans)

print(ans)

