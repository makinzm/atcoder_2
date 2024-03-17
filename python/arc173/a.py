from inspect import stack


MAX_NUM = 10 ** 20
debug = True

def _calculate_stacked_value(
        stacked_value,
        previous_base,
        current_digit,
        next_digit
    ):
    """自明的に 9 通りの数が選べない場合の合計数を計算する助けをする"""
    # 次の文字が現在の文字より小さい場合
    if next_digit != current_digit:
        if next_digit < current_digit:
            # [0:current_digit] \ [next_digit] の数
            stacked_value = stacked_value + (current_digit - 1) * previous_base
        else:
            stacked_value = stacked_value + current_digit * previous_base
    else:
        # [0:current_value) の数だけ自由に動ける (next_digit == current_digit であるため)
        stacked_value = current_digit * previous_base
    return stacked_value

def _get_same_digits_neq_number(x):
    """Get the number of Neq Number that has the same digits as x and less than or equal to x"""
    num_of_digits = len(str(x))
    
    current_digit = x % 10
    next_digit = (x // 10) % 10
    # 自由に選べる場合の基数
    previous_base = 1
    # 自由に選べない場合の合計数 (初期値は x が選べると仮定した際の1通り)
    stacked_value = 1
    for i in range(num_of_digits):
        stacked_value = _calculate_stacked_value(
            stacked_value,
            previous_base,
            current_digit,
            next_digit
        )
        x //= 10
        current_digit = x % 10
        next_digit = (x // 10) % 10
        previous_base *= 9
    return stacked_value

def _get_less_digits_neq_number(x):
    """Get the number of Neq Number that has less digits than x"""
    num_of_digits = len(str(x))
    ans = 0
    for i in range(1, num_of_digits):
        ans += 9 ** i
    return ans

def _get_num_neq(x):
    """Get the number of Neq Number that is less than or equal to x"""
    return _get_same_digits_neq_number(x) + _get_less_digits_neq_number(x)

if False:
    max_k = _get_num_neq(MAX_NUM)
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
