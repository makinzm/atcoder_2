q = int(input())

top = 0

where_am_i_adding = []
what_length = []

missing_headings = 0
missing_length = 0

for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        where_am_i_adding.append(top)
        what_length.append(s[1])
        top += s[1]
    elif s[0] == 2:
        missing_length += what_length[missing_headings]
        missing_headings += 1
    else:
        num = missing_headings + s[1] - 1
        print(where_am_i_adding[num] - missing_length)

