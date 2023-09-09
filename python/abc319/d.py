L = 10**9

n,m = list(map(int,input().split()))
l = list(map(int,input().split()))

# またがってはダメ,
# どうやって作るかわからない.

# 最小のdisplay幅, 

# OUT となる数の最大値
min_l = 0

# OKとなる数の最小値
max_l = (sum(l) + n-1)

def check(value):
    current_row = 0
    current_point = 0
    for item in l:
        if current_row > m-1:
            return False
        if_same_row = current_point + item + 1 if current_point > 0 else current_point + item
        if if_same_row <= value:
            current_point = if_same_row
        else:
            current_row += 1
            if item <= value:
                current_point = item
            else:
                return False
    if current_row > m-1:
        return False
    return True

while(max_l - min_l > 1):
    tested_value = (max_l + min_l) // 2
    if check(tested_value):
        max_l = tested_value
    else:
        min_l = tested_value

print(max_l)
