n = int(input())
h = list(map(int, input().split()))

debug = False
t = 0
t_remainder = 0

for i in range(n):
    num_interval = h[i] // 5
    remainder = h[i] % 5
    if t_remainder == 0:
        if remainder == 0:
            t += num_interval * 3
            t_remainder = 0
        elif remainder == 1:
            t += num_interval * 3 + 1
            t_remainder = 1
        elif remainder == 2:
            t += num_interval * 3 + 2
            t_remainder = 2
        else:
            t += num_interval * 3 + 3
            t_remainder = 0
    elif t_remainder == 1:
        if remainder == 0:
            t += num_interval * 3
            t_remainder = 1
        elif remainder == 1:
            t += num_interval * 3 + 1
            t_remainder = 2
        else:
            t += num_interval * 3 + 2
            t_remainder = 0
    else:
        if remainder == 0:
            t += num_interval * 3
            t_remainder = 2
        elif remainder in [1,2,3]:
            t += num_interval * 3 + 1
            t_remainder = 0
        else:
            t += num_interval * 3 + 2
            t_remainder = 1

    if debug:
        print(f"i={i}, num_interval={num_interval}, remainder={remainder}, t={t}, t_remainder={t_remainder}")

print(t)

