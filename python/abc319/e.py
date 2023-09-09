from math import lcm

n,x,y = list(map(int,input().split()))

# 頑張って早く到着したい.
# Qで出発したときに逐次的に乗っていては間に合わなさそう.
# ただ,出発時刻に対して modの8パターンに対して求めてしまって,計算すれば間に合う.

ans_lst = []

pt_s = []
p_lst = []

for _ in range(n-1):
    tmp = list(map(int,input().split()))
    pt_s.append(tmp)
    p_lst.append(tmp[0])

def calculate_2(now, mod):
    if now % mod == 0:
        return now
    else:
        tmp = now + (mod - (now % mod))
        assert tmp % mod == 0
        return tmp

def calculate(start):
    time = start + x
    for pt in pt_s:
        time = calculate_2(time,pt[0])
        time += pt[1]
    time += y
    return time

q_n = int(input())
q_lst = []
for i in range(q_n):
    q_lst.append(int(input()))

# q の最小公倍数
q_mn = lcm(*p_lst)

for i in range(q_mn):
    ans_lst.append(calculate(i))

for q in q_lst:
    mod = -1
    if q_mn != 0:
        mod = q % q_mn
    else:
        mod = 0
    print(ans_lst[mod] + q - mod)
