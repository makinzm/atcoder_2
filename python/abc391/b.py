n,m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]

def include_t(s_row_i, s_col_i):
    for t_row_i, t_row in enumerate(t):
        for t_col_i, t_col in enumerate(t_row):
            if s[s_row_i+t_row_i][s_col_i+t_col_i] != t[t_row_i][t_col_i]:
                return False
    return True

for s_row_i, s_row in enumerate(s):
    for s_col_i, s_col in enumerate(s_row):
        if s_row_i + m > n or s_col_i + m > n:
            continue
        if include_t(s_row_i, s_col_i):
            print(f"{s_row_i+1} {s_col_i+1}")
            exit()
 
