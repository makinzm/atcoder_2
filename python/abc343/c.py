MAX_X = 10 ** 6 + 1

cubics = [i ** 3 for i in range(0, MAX_X + 1)]

palindromes = [
    i for i in cubics if str(i) == str(i)[::-1]
]

n = int(input())

max_index = len(palindromes) - 1 # Out
min_index = 0 # Safe

while max_index - min_index > 1:
    mid_index = (max_index + min_index) // 2
    if palindromes[mid_index] <= n:
        min_index = mid_index
    else:
        max_index = mid_index

print(palindromes[min_index])
