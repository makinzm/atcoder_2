from more_itertools import distinct_permutations

num, kaibun_length = map(int, input().split())
base_string = input()

count = 0

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

def is_k_palindrome(s, k, num):
    for i in range(num - k + 1):
        if is_palindrome(s[i:i + k]):
            return True
    return False

base_list = list(base_string)
count = 0
for perm in distinct_permutations(base_list):
    count += not is_k_palindrome(perm, kaibun_length, num)

print(count)

