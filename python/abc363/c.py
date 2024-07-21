from more_itertools import distinct_permutations
from numba import jit

num, kaibun_length = map(int, input().split())
base_string = input()

count = 0

@jit(nopython=True, cache=True)
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

@jit(nopython=True)
def is_k_palindrome(s, k):
    for i in range(num - k + 1):
        if is_palindrome(s[i:i + k]):
            return True
    return False

count = sum(
    not is_k_palindrome(perm, kaibun_length) for perm in distinct_permutations(base_string)
)

print(count)

