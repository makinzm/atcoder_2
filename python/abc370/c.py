s = input()
t = input()

s = list(s)
t = list(t)

debug = False

change_index = []
for i in range(len(s)):
    if t[i] < s[i]:
        change_index.append(i)

if debug:
    print(change_index)

reversed_change_index = []

for i in range(len(s)):
    if s[i] < t[i]:
        reversed_change_index.append(i)

change_index = change_index + reversed_change_index[::-1]

if debug:
    print(change_index)

x = []
for i in change_index:
    s[i] = t[i]
    x.append("".join(s))

print(len(x))
for i in x:
    print(i)
