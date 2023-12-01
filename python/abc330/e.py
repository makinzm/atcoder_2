import numpy as np

list_input = lambda: list(map(int, input().split()))

n,q = list_input()
a = np.array(list_input())
ix = []
for _ in range(q):
    ix.append(list_input())

# Mex = min{ the min in the sparce of A, the max in A + 1 }

# When mex is updated, the following case must happen
# 1. The new value must be the mex
# 2. The place of updated must be the max value and A is dense not sparse.
# 3. The value to change must be the old min value.

INI_MEX = -1

max_place = np.argmax(a)
max_value = np.max(a)
min_place = np.argmin(a)
min_value = np.min(a)
length_set = len(set(a))
mex = INI_MEX

def find_mex():
    a_sort = np.sort(a)
    old_value = None
    for a_i in a_sort:
        if old_value is None:
            if a_i > 0:
                return 0
            old_value = a_i
        else:
            if a_i == old_value + 1 or a_i == old_value:
                old_value = a_i
                pass
            else:
                return old_value+1
    return a_i + 1

def calc_mex(input_int = None):
    if length_set == len(a):
        return 0 if np.min(a) > 0 else np.max(a) + 1
    if input_int != mex and mex != INI_MEX:
        return mex
    return find_mex()

mex = calc_mex()

for ix_i in ix:
    a[ix_i[0]-1] = ix_i[1]
    mex = calc_mex(ix_i[1])
    print(mex)
