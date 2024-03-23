debug = False

h,w,m = map(int, input().split())

commands = []
for i in range(m):
    t, a, x = map(int, input().split())
    commands.append((t, a, x))

if debug:
    print(f"commands: {commands}")

current_h = h
current_w = w

visited_h = set()
visited_w = set()

color_count = {}

for i in range(m):
    t, a, x = commands[-i-1]
    if debug:
        print(f"t: {t}, a: {a}, x: {x}")
    if t == 1:
        if a in visited_h:
            continue
        visited_h.add(a)
        current_h -= 1
        if current_w > 0:
            color_count[x] = color_count.get(x, 0) + current_w
    else:
        if a in visited_w:
            continue
        visited_w.add(a)
        current_w -= 1
        if current_h > 0:
            color_count[x] = color_count.get(x, 0) + current_h
    if debug:
        print(f"current_h: {current_h}, current_w: {current_w}")
        print(f"visited_h: {visited_h}, visited_w: {visited_w}")
        print(f"color_count: {color_count}")

# fill 0

sum_count = sum(color_count.values())
if sum_count < h * w:
    color_count[0] = (h * w) - sum_count + color_count.get(0, 0)

sorted_color = sorted(color_count.items(), key=lambda x: x[0])

print(len(sorted_color))

for color, count in sorted_color:
    print(color, count)
