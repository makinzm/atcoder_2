n,m = map(int,input().split())
s = input()
c = list(map(int,input().split()))

init_dict = dict() # M
last_dict = dict() # M
convert_dict = dict() # N
for i in reversed(range(n)):
    try:
        convert_dict[last_dict[c[i]]] = i
    except KeyError:
        init_dict[c[i]] = i
    last_dict[c[i]] = i

for k,v in last_dict.items():
    convert_dict[v] = init_dict[k]

[print(s[convert_dict[i]], end=""if i != n-1 else "\n") for i in range(n)]

