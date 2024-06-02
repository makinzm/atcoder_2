MOD = 998244353

def solve(n, m):
    result = 0

    bit_position = 0
    while (1 << bit_position) <= n:
        bit_base = 1 << bit_position
        group_size = 2 * bit_base
        if m & bit_base:
            num_group = (n + 1) // group_size
            remainder = (n + 1) % group_size
            result += num_group * bit_base
            result += max(0, remainder - bit_base)
            result %= MOD
        bit_position += 1

    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solve(n, m))

