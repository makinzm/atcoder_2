DEBUG = False

n, w = map(int, input().split())
xy_s = [list(map(int, input().split())) for _ in range(n)]
xy_s_with_index = [(i, xy) for i, xy in enumerate(xy_s)]
q = int(input())
queryies = [list(map(int, input().split())) for _ in range(q)]

x_groups = dict()
for i, (x, y) in xy_s_with_index:
    if x not in x_groups:
        x_groups[x] = []
    x_groups[x].append((y, i))

if len(x_groups) < w:
    [print("Yes") for _ in range(q)]
    exit()

timings = dict()

if DEBUG:
    print(f"{x_groups=}")

for x in x_groups:
    x_groups[x].sort(key=lambda x: x[0])
    for i, y_info in enumerate(x_groups[x]):
        if i not in timings:
            timings[i] = set([y_info])
        else:
            timings[i].add(y_info)
if DEBUG:
    print(f"x_groups: {x_groups}")
    print(f"timings: {timings}")

timings_with_real_time = []
last_time = 0

for index, group in timings.items():
    if len(group) < w:
        break
    only_times = list(map(lambda x: x[0], group))
    current_times = list(map(lambda x: x - last_time, only_times))
    latest_time = max(max(current_times), 0)
    timings_with_real_time.append((latest_time, group))

query_with_index = [(i, query) for i, query in enumerate(queryies)]

query_with_index.sort(key=lambda x: x[1][0])

if DEBUG:
    print(f"{timings_with_real_time=}")
    print(f"{query_with_index=}")

answers = ["Yes" for _ in range(q)]

last_time_group = 0
already_checked = set()

for query in query_with_index:
    i, (t, a) = query
    a -= 1
    if DEBUG:
        print("----")
        print(f"{i=}")
        print(f"{t=} {a=}")
        print(f"{last_time_group=}")
    if a in already_checked:
        answers[i] = "No"
        continue
    for time, group in timings_with_real_time[last_time_group:]:
        if DEBUG:
            print(f"{time=}")
            print(f"{group=}")
            print(f"{answers=}")
        group_only_index = set(map(lambda x: x[1], group))
        if time > t:
            if answers[i] is None:
                answers[i] = "Yes"
            break
        last_time_group += 1
        if DEBUG:
            print(f"{i=}")
            print(f"{a=}")
            print(f"{group=}")
            print(f"{group_only_index=}")
        already_checked |= group_only_index
        if a in already_checked:
            answers[i] = "No"
        else:
            answers[i] = "Yes"

[print(ans) for ans in answers]
