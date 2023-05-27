n = int(input())
s = input()
t = input()

flag = True
for i in range(n):
    if s[i] == t[i]:
        flag = True
    elif s[i] == "1" and t[i] == "l":
        flag = True
    elif t[i] == "1" and s[i] == "l":
        pass
    elif s[i] == "0" and t[i] == "o":
        pass
    elif s[i] == "o" and t[i] == "0":
        pass
    else:
        flag = False
    
    if not flag:
        break

print("Yes" if flag else "No")


