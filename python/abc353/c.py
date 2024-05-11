n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a) * (n - 1)

sorted_a = sorted(a)

threshold = 10 ** 8

def find_over_number(i):
    # threshold - sorted[i] を超える sorted[j] を持つ最小の j を返す
    left = -1 # candidate
    right = n-1 # out of candidate
    while right - left > 1:
        mid = (left + right) // 2
        if sorted_a[mid] >= threshold - sorted_a[i]:
            right = mid
        else:
            left = mid
    return right

all_count = 0
for i in range(n):
    index = find_over_number(i)
    if (index == n-1) and (sorted_a[i] + sorted_a[index] < threshold):
        index = -1
    
    if index != -1:
        if index <= i:
            all_count += n - index - 1
        else:
            all_count += n - index
    else:
        all_count += 0

print(sum_a - threshold * (all_count // 2) )
