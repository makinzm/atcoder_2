k = int(input())

debug = False

def find_kth_palindrome(k):
    def count_palindromes(length):
        if length == 1:
            return 10  # 0から9までの10個
        elif length % 2 == 0:
            return 9 * 10 ** (length // 2 - 1)
        else:
            return 9 * 10 ** (length // 2)

    def generate_palindrome(num, odd):
        s = str(num)
        return int(s + (s[:-1] if odd else s)[::-1])

    if k <= 10:
        return k - 1

    length = 1
    count = 0
    while True:
        palindromes_count = count_palindromes(length)
        if count + palindromes_count > k:
            break
        count += palindromes_count
        length += 1

    if debug:
        print(f"{count = }, {length = }")

    k -= count
    odd = length % 2 != 0

    left = k + 10 ** ((length - 1) // 2) - 1
    if debug: 
        print(f"{left = }, {odd = }")
    return generate_palindrome(left, odd)

print(find_kth_palindrome(k))

