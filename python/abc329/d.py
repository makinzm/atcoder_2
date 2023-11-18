n,m = map(int,input().split())
a = list(map(int,input().split()))

voted_dict = {}
previous_winner = None

for i in range(m):
    if a[i] in voted_dict:
        voted_dict[a[i]] += 1
    else:
        voted_dict[a[i]] = 1
    if i == 0:
        print(a[i])
        previous_winner = a[i]
    else:
        if voted_dict[a[i]] > voted_dict[previous_winner]:
            print(a[i])
            previous_winner = a[i]
        elif voted_dict[a[i]] == voted_dict[previous_winner]:
            if previous_winner < a[i]:
                print(previous_winner)
            else:
                print(a[i])
                previous_winner = a[i]
        else:
            print(previous_winner)
