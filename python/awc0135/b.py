import numpy as np

n = int(input())
ps_list = []
for _ in range(n):
    ps_list.append(list(map(int, input().split())))

ps_array = np.array(
    list(map(lambda x: x[1] / x[0], ps_list))
)

ans = np.argmax(ps_array) + 1
print(ans)
