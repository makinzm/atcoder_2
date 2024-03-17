MAX_NUM = 10 ** 20

def _get_num_neq(x):
    """Get the number of Neq Numbers which is equal to or less than x."""
    num_of_digits = len(str(x))
    
    current_digit = x % 10
    next_digit = (x // 10) % 10
    ans = 0
    for i in range(num_of_digits):
        # 次の桁が現状の桁の候補に入る場合は、少なくカウントする
        # また、最高桁の場合は次の桁が0のため、少なくカウントされることがこの条件に含まれている
        # また、0が連続している場合はカウントとして current_digit が 0であるため増加しない
        if current_digit >= next_digit:
            ans += current_digit * (9 ** i)
        else:
            ans += (current_digit + 1) * (9 ** i)
        
        x //= 10
        current_digit = x % 10
        next_digit = (x // 10) % 10
    return ans

max_k = _get_num_neq(MAX_NUM)
debug = False
if debug:
    print(max_k)
    print("OK" if max_k > 10 ** 12 else "NG")

def solve(k):
    """k番目のNeq Numberを求める"""
    # out
    min_num = 0
    # safe
    max_num = MAX_NUM
    while max_num - min_num > 1:
        mid = (max_num + min_num) // 2
        num_neq_of_mid = _get_num_neq(mid)
        if num_neq_of_mid >= k:
            max_num = mid
        else:
            min_num = mid

    return max_num

if __name__ == "__main__":
    t = int(input())
    cases = []
    for _ in range(t):
        case_i = int(input())
        cases.append(case_i)
    
    for case in cases:
        print(solve(case))
