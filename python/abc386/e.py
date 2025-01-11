n,k = map(int, input().split())

a = list(map(int, input().split()))

DEBUG = False

if DEBUG:
    def true_xor_sum(arr):
        res = arr[0]
        for i in range(1, len(arr)):
            res ^= arr[i]
        return res

from more_itertools import distinct_combinations

ans = 0
prev_ans = None
prev_comb = None

def xor_sum(arr, prev_ans, prev_comb):
    if prev_ans is None and prev_comb is None:
        res = arr[0]
        for i in range(1, len(arr)):
            res ^= arr[i]
        return res
    else:
        set_arr = set(arr)
        set_prev_comb = set(prev_comb)
        if len(set_arr) == len(arr) and len(set_prev_comb) == len(prev_comb):
            diff_comb = (set_arr | set_prev_comb) - (set_arr & set_prev_comb)
        else:
            diff_comb = []
            arr = list(arr)
            prev_comb = list(prev_comb)
            for i in arr:
                if i not in prev_comb:
                    diff_comb.append(i)
                else:
                    prev_comb.remove(i)
            diff_comb += prev_comb
        if DEBUG:
            print(f"    {diff_comb=}")
        res = prev_ans
        for i in diff_comb:
            res ^= i
        return res

order_combinations = list(distinct_combinations(a, k))
sorted_combinations = sorted(order_combinations)

for comb in sorted_combinations:
    current_ans = xor_sum(comb, prev_ans, prev_comb)
    if DEBUG:
        true_current_ans = true_xor_sum(comb)
        if current_ans != true_current_ans:
            print(f"OUT comb: {comb}")
            print(f"current_ans: {current_ans}")
            print(f"true_current_ans: {true_current_ans}")
        else:
            print(f"OK: {comb=}, {current_ans=}")
    ans = max(ans, current_ans)
    prev_ans = current_ans
    prev_comb = comb

print(ans)
