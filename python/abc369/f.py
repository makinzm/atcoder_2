from bisect import bisect_right

debug = False

h, w, n = map(int, input().split())
coins = [
    list(map(int, input().split())) for _ in range(n)
]

coins = sorted(coins, key=lambda x: x[0] * 10**6 + x[1])

if debug:
    print(f"{coins=}")

# dp[i]: the minimum value x when the length = i
# WARN: However, the sequence may not accomplished, but the point is accomplished
list_dp_x = [ float("inf") for _ in range(n) ]
# gotten_coins_indexes[i]: the index which meets the minimum x when the length = i
# WARN: However, the sequence may not accomplished, but the point is accomplished
gotten_coins_indexes = [ -100 for _ in range(n) ]
# previous_coin_indexes[i]: the index of previous coin if the coin i is selected
previous_coin_indexes = [ -100 for _ in range(n) ]

for i in range(n):
    should_insert_index = bisect_right(list_dp_x, coins[i][1])
    list_dp_x[should_insert_index] = coins[i][1]
    gotten_coins_indexes[should_insert_index] = i
    previous_coin_indexes[i] = gotten_coins_indexes[should_insert_index-1] if should_insert_index > 0 else -1
    if debug:
        print(f"{i=}, {should_insert_index=}, {list_dp_x=}, {gotten_coins_indexes=}, {previous_coin_indexes=}")
        print(f"{list_dp_x[should_insert_index]}, {gotten_coins_indexes[should_insert_index]}, {previous_coin_indexes[i]}")

# this value is only used when deciding where to insert
del list_dp_x

num_gotten_coin = n
while gotten_coins_indexes[num_gotten_coin-1] <= -1:
    num_gotten_coin -= 1

if debug:
    print(f"{num_gotten_coin=}")

last_coin_index = gotten_coins_indexes[num_gotten_coin-1]
# this value in only used when deciding which coin is the last coin
del gotten_coins_indexes

path = [[h,w]]

while last_coin_index >= 0:
    path.append(coins[last_coin_index])
    last_coin_index = previous_coin_indexes[last_coin_index]

path.append([1,1])

path = path[::-1]

ans = []
for i in range(1, len(path)):
    destination = path[i]
    start = path[i-1]

    num_down = destination[0] - start[0]
    num_right = destination[1] - start[1]

    ans += ["D"] * num_down
    ans += ["R"] * num_right

print(num_gotten_coin)
print("".join(ans))

