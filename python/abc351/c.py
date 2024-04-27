n = int(input())
a = list(map(int,input().split()))

box = []

i = 0
flag = True

while(i < n):
    if flag:
        box.append(a[i])
    if len(box) <= 1:
        i += 1
        flag = True
    else:
        if box[-1] != box[-2]:
            i += 1
            flag = True
        else:
            last_box = box.pop()
            box.pop()
            box.append(last_box + 1)
            flag = False

print(len(box))
