lst = list(map(int, input().split()))
remove_color = input()

remove_i = -1
if remove_color == "Red":
    remove_i = 0
elif remove_color == "Green":
    remove_i = 1
elif remove_color == "Blue":
    remove_i = 2

if remove_i == -1:
    raise ValueError("Invalid color")

lst.pop(remove_i)

print(min(lst))
