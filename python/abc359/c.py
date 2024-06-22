s_x, s_y = map(int, input().split())
t_x, t_y = map(int, input().split())

height = abs(t_y - s_y)
if s_x % 2 == 0:
    left_max = s_x - height
    right_max = s_x + height + 1
else:
    left_max = s_x - height - 1
    right_max = s_x + height

if t_y % 2 != 0:
    left_max += 1
    right_max += 1
    t_x += 1

left_block = left_max // 2
right_block = right_max // 2
ans_block = t_x // 2

if left_block <= ans_block <= right_block:
    width = 0
else:
    width = min(abs(left_block - ans_block), abs(right_block - ans_block))

debug = False
if debug:
    print(left_max, right_max)
    print(width, height)

print(height + width)

