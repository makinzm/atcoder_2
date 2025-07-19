from more_itertools import distinct_combinations

h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

a_all_xor = 0
for i in range(h):
    for j in range(w):
        a_all_xor ^= a[i][j]

available_memory = set()

def change_coordinate_to_index(x, y):
    return x * w + y

def change_index_to_coordinate(index):
    x = index // w
    y = index % w
    return x, y

def is_available_comb(comb, from_parent=False):
    if tuple(comb) in available_memory:
        return True
    if DEBUG:
        print(f"\t\t{from_parent=} Checking combination: {comb}")
    if len(comb) == 0:
        return True
    assert len(comb) % 2 == 0, "Combination length must be even"
    first_comb = comb[0]
    first_x, first_y = change_index_to_coordinate(first_comb)
    candidate_index_same_x = change_coordinate_to_index(first_x, first_y + 1)
    candidate_index_same_y = change_coordinate_to_index(first_x + 1, first_y)
    if candidate_index_same_x in comb:
        removed_comb = [
            index for index in comb if index != candidate_index_same_x and index != first_comb
        ]
        return is_available_comb(removed_comb)
    elif candidate_index_same_y in comb:
        removed_comb = [
            index for index in comb if index != candidate_index_same_y and index != first_comb
        ]
        return is_available_comb(removed_comb)
    return False

def all_xor(comb):
    result = a_all_xor
    for index in comb:
        x, y = change_index_to_coordinate(index)
        result ^= a[x][y]
    return result

DEBUG = False
DEBUG2 = False
total_num = 0

ans = 0
for num in range(0, h * w + 1, 2):
    if DEBUG:
        print(f"Checking combinations of size {num}")
    for comb in distinct_combinations(range(h*w), num):
        if not is_available_comb(comb, from_parent=True):
            continue
        available_memory.add(tuple(comb))
        if DEBUG2:
            total_num += 1
        result = all_xor(comb)
        if DEBUG:
            print(f"\tCurrent combination: {comb}, {result=}")
        ans = max(ans, result)

if DEBUG2:
    print(f"Total combinations checked: {total_num}")

print(ans)

