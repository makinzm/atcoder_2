s = input()

is_ok = True

if s[0] == "<":
    for i in range(1, len(s) - 1):
        if s[i] != "=":
            is_ok = False
            break
    if s[-1] != ">":
        is_ok = False
else:
    is_ok = False

print("Yes" if is_ok else "No")