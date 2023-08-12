import numpy as np

n = int(input())
s = input()
q = int(input())
txc = []
for i in range(q):
    _t, _x, _c = input().split()
    _t = int(_t)
    _x = int(_x)
    txc.append((_t,_x,_c))

current_dict = dict()
for i in range(n):
    current_dict[i] = s[i]

current_lst = []
for i in range(n):
    if current_dict[i].isupper():
        current_lst.append(1)
    else:
         current_lst.append(0)
current_lst = np.array(current_lst)

for i in range(q):
    t,x,c = txc[i]
    if t == 1:
        current_dict[x-1] = c
        if c.isupper():
            current_lst[x-1] = 1.0
        else:
            current_lst[x-1] = 0.0
    elif t == 2:
        current_lst = np.zeros(n)
    else:
        current_lst = np.ones(n)

[print(current_dict[i].upper() if current_lst[i] == 1 else current_dict[i].lower(), end=""if i != n-1 else "\n") for i in range(n)]
