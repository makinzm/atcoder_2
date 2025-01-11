abcd = list(map(int, input().split()))

sorted_abcd = sorted(abcd)

first = 0
second = 0

first_sign = ""
second_sign = ""

for i in sorted_abcd:
    if first_sign == "":
        first_sign = i
        first += 1
    elif first_sign == i:
        first += 1
    else:
        if second_sign == "":
            second_sign = i
            second += 1
        else:
            if i == first_sign:
                first += 1
            elif i == second_sign:
                second += 1
            else:
                print("No")
                exit()

if (first, second) == (2, 2) or (first, second) == (1, 3) or (first, second) == (3, 1):
    print("Yes")
else:
    print("No")
