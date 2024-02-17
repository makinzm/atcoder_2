n = int(input())
a = list(map(int, input().split()))
st = []
for i in range(n-1):
    st.append(list(map(int, input().split())))

for i in range(n-1):
    _n = a[i]//st[i][0]
    a[i+1] += st[i][1]*_n

print(a[-1])
