n = int(input())
q = list(list(map(int, input().split())) for i in range(n))
q_num = int(input())
q_list = list(list(map(int, input().split())) for i in range(q_num))

# int is not //
def ans(q, r, t, d):
    x = (d-r)//q
    if (d-r)%q != 0:
        x += 1
    return q * x + r

for i in range(q_num):
    t = q_list[i][0]
    d = q_list[i][1]
    print(ans(q[t-1][0], q[t-1][1], t, d))


