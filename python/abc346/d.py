debug = False

# 0101... part_1
# 1010... part_2
# それぞれ作る場合のコストを出して, ある場所だけ 11 or 00 になるようにすることを考えれば良い

n = int(input())
s = input()
c = list(map(int, input().split()))

part_1 = []
# part_1[i] = i 番目までの文字列を 0101... にするための最小コスト
part_2 = []
# part_2[i] = i 番目までの文字列を 1010... にするための最小コスト

for i in range(n):
    if i == 0:
        if s[i] == "0":
            part_1.append(0)
            part_2.append(c[0])
        else:
            part_1.append(c[0])
            part_2.append(0)
    else:
        if i % 2 == 0:
            if s[i] == "0":
                part_1.append(part_1[-1])
                part_2.append(part_2[-1] + c[i])
            else:
                part_1.append(part_1[-1] + c[i])
                part_2.append(part_2[-1])
        else:
            if s[i] == "0":
                part_1.append(part_1[-1] + c[i])
                part_2.append(part_2[-1])
            else:
                part_1.append(part_1[-1])
                part_2.append(part_2[-1] + c[i])

if debug:
    print(part_1)
    print(part_2)

ans = sum(c)

def get_cost(sub_s, aim_s, cost_i, cost_i_plus_1):
    cost = 0
    if aim_s[0] != sub_s[0]:
        cost += cost_i
    if aim_s[1] != sub_s[1]:
        cost += cost_i_plus_1
    return cost

for i in range(n-1):
    # 自分自身と後を11にする
    former_part_1_cost = 0
    # 自分自身と後を00にする
    former_part_2_cost = 0
    if i > 0:
        if i % 2 == 0:
            # 10 を採用する
            former_part_1_cost = part_2[i-1]
            # 01 を採用する
            former_part_2_cost = part_1[i-1]
        else:
            # 01 を採用する
            former_part_1_cost = part_1[i-1]
            # 10 を採用する
            former_part_2_cost = part_2[i-1]
    latter_part_1_cost = 0
    latter_part_2_cost = 0
    if i < n-1:
        if i % 2 == 0:
            # 01 を採用する
            latter_part_1_cost = part_1[-1] - part_1[i+1]
            # 10 を採用する
            latter_part_2_cost = part_2[-1] - part_2[i+1]
        else:
            # 10 を採用する
            latter_part_1_cost = part_2[-1] - part_2[i+1]
            # 01 を採用する
            latter_part_2_cost = part_1[-1] - part_1[i+1]

    if debug:
        print(f"i: {i}, former_part_1_cost: {former_part_1_cost}, former_part_2_cost: {former_part_2_cost}, latter_part_1_cost: {latter_part_1_cost}, latter_part_2_cost: {latter_part_2_cost}")

    main_cost_1 = get_cost(s[i:i+2], "11", c[i], c[i+1])
    main_cost_2 = get_cost(s[i:i+2], "00", c[i], c[i+1])

    if debug:
        print(f"i: {i}, main_cost_1: {main_cost_1}, main_cost_2: {main_cost_2}")

    cost_1 = main_cost_1 + former_part_1_cost + latter_part_1_cost
    cost_2 = main_cost_2 + former_part_2_cost + latter_part_2_cost
    
    if debug:
        print(f"i: {i}, cost_1: {cost_1}, cost_2: {cost_2}")
    ans = min(ans, cost_1, cost_2)

print(ans)
