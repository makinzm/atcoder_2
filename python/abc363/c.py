from itertools import permutations

num, kaibun_length = map(int, input().split())
base_string = input()

count = 0

palidoromes_dict = {}

def is_palindrome(s):
    if s in palidoromes_dict:
        return palidoromes_dict[s]
    ans =  s == s[::-1]
    palidoromes_dict[s] = ans
    return ans

def is_k_palindrome(s, k):
    for i in range(num - k + 1):
        if is_palindrome(s[i:i + k]):
            return True
    return False

count = sum(
    not is_k_palindrome(perm, kaibun_length) for perm in set(permutations(base_string))
)

print(count)

