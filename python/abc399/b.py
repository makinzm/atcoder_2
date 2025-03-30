n = int(input())
p = list(map(int, input().split()))

ranks = [ -1 for _ in range(n) ]

r = 1

defined = 0

while True:
    max_scores_in_round = 0
    k = 0
    round_list = []
    for i in range(n):
        if ranks[i] == -1:
            if p[i] > max_scores_in_round:
                max_scores_in_round = p[i]
                k = 1
                round_list = [i]
            elif p[i] == max_scores_in_round:
                k += 1
                round_list.append(i)
    for i in round_list:
        ranks[i] = r
    defined += len(round_list)
    r += k

    if defined == n:
        break

for i in ranks:
    print(i)

