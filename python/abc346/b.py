base_string = "wbwbwwbwbwbw"

n = len(base_string)

all_string = base_string * 30

w, b = map(int, input().split())

length = w + b

is_ok = False

for i in range(n):
    sub_string = all_string[i:i+length]
    w_count = sub_string.count("w")
    b_count = sub_string.count("b")
    if w_count == w and b_count == b:
        is_ok = True
        break

print("Yes" if is_ok else "No")

