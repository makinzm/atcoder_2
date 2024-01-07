from collections import deque

MOD = 998244353

q = int(input())

start = 0
stop = 1
state_stack = deque([1])
ans = (0, 1, 1, 1)

for _ in range(q):
    order = input()
    if order[0] == "1":
        x = int(order.split()[1])
        stop += 1
        state_stack.append(x)
    elif order[0] == "2":
        start += 1
    elif order[0] == "3":
        pre_start, pre_stop, printed_ans, pre_ans = ans
        if pre_start == start and pre_stop == stop:
            print(printed_ans)
            continue
        ans_up = pre_ans
        if pre_start != start:
            ans_up %= 10 ** (pre_stop - start)
        ans_up *= 10 ** (stop - pre_stop)
        ans_down = 0
        count = 1
        # reverse
        for i in reversed(range(pre_stop, stop)):
            ans_down += state_stack[i] * count
            count *= 10
        true_ans = ans_up + ans_down
        ans = (start, stop, true_ans, true_ans % MOD)
        print(ans[3])
    else:
        raise ValueError("invalid order")
