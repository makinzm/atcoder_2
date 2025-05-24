s = input()

lst = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

is_ans = False
for ans in lst:
    if ans not in s:
        is_ans = True
        print(ans)
        break

if not is_ans:
    raise ValueError("No answer found")
