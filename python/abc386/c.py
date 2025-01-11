k = int(input())
s = input()
t = input()

s_index = 0
t_index = 0

flag = False

DEBUG = False

while s_index < len(s) or t_index < len(t):
    if s_index < len(s) and t_index < len(t) and s[s_index] == t[t_index]:
        s_index += 1
        t_index += 1
        if s_index == len(s) and t_index == len(t):
            flag = True
            break
    else:
        if DEBUG:
            print(f"Pattern A: {s[s_index:]} {t[t_index+1:]}")
            print(f"Pattern B: {s[s_index+1:]} {t[t_index:]}")
            print(f"Pattern C: {s[s_index+1:]} {t[t_index+1:]}")
        if s[s_index:] == t[t_index+1:]:
            flag = True
            break
        elif s[s_index+1:] == t[t_index:]:
            flag = True
            break
        elif s[s_index+1:] == t[t_index+1:]:
            flag = True
            break
        else:
            break

print("Yes" if flag else "No")
