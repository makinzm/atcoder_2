r = int(input())

num = 0

last_one = r+1

def get_cordinates(x,y):
    return [
        (x+0.5, y+0.5),
        (x+0.5, y-0.5),
        (x-0.5, y+0.5),
        (x-0.5, y-0.5),
    ]

def get_squared_distance(x,y):
    return (x**2 + y**2)

first = -1

DEBUG = False

for X in range(r+1):
    for Y in range(last_one, -1, -1):
        if DEBUG:
            print(f"TRYING: {X=}, {Y=}")
        ok_to_break = False
        for x,y in get_cordinates(X,Y):
            distance = get_squared_distance(x,y)
            if DEBUG:
                print(f"{x=}, {y=}, {distance=}")
            if get_squared_distance(x,y) > r**2:
                last_one = Y
                ok_to_break = True
                break
        if not ok_to_break:
            if first == -1:
                first = Y + 1
            num += Y + 1
            if DEBUG:
                print(f"SUCCESS: {X=}, {Y=}, {num=}")
            break

if first != -1:
    print((num-first) * 4 + 1)
else:
    print(0)
