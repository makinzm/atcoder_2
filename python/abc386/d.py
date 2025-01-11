n, m = map(int, input().split())

xyc = [input().split() for _ in range(m)]

sorted_xyc = sorted(xyc, key=lambda x: int(x[0]) * 10 ** 10 + int(x[1]))

DEBUG = False

if DEBUG:
    print(sorted_xyc)

last_black = (n, n)
last_white = (n, n)

for x, y, c in sorted_xyc:
    x, y = int(x) - 1, int(y) - 1
    if DEBUG:
        print(f"x: {x}, y: {y}, c: {c}")
        print(f"last_black: {last_black}")
        print(f"last_white: {last_white}")
    if c == "B":
        if y >= last_white[1]:
            print("No")
            exit()
        last_black = (x, y)
    else:
        last_white = (x, y)


print("Yes")

