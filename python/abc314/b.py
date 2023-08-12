n = int(input())
c = []
a = []
for i in range(n):
    c.append(int(input()))
    a.append(set(list(map(int,input().split()))))
x = int(input())

ans_lst = []
for i in range(n):
    if x in a[i]:
        ans_lst.append((i,len(a[i])))

ans_lst = sorted(ans_lst,key=lambda x: x[1])

if len(ans_lst) > 0:
    min_k = ans_lst[0][1]

    k = 0
    answers = []

    for i in range(len(ans_lst)):
        if ans_lst[i][1] ==  min_k:
            answers.append(ans_lst[i][0]+1)
            k+=1
        else:
            break

    print(k)
    [print(i, end=" "if idx != k-1 else "\n") for idx,i in enumerate(answers)]
else:
    print(0)
    print()