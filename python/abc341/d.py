# from math import lcm

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)


n,m,k = map(int, input().split())

if n > m:
    n, m = m, n

lcm_nm = lcm(n, m)
what_n = lcm_nm // n - 1
what_m = lcm_nm // m - 1
what = what_n + what_m

turn = k // what
min_turn = k % what

base_ans = turn * lcm_nm
current_n = base_ans
current_n_index = 0
current_m = base_ans
current_m_index = 0

ans_n = True

if min_turn == 0:
    print(base_ans - min(n, m))
else:
    for i in range(min_turn):
        if current_n == current_m:
            current_n += n
            current_n_index += 1
            ans_n = True
        else:
            if current_n + n < current_m + m:
                current_n += n
                current_n_index += 1
                ans_n = True
            else:
                current_m += m
                current_m_index += 1
                ans_n = False
    if ans_n:
        print(base_ans + current_n_index * n)
    else:
        print(base_ans + current_m_index * m)
