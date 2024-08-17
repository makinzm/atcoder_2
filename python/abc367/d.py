from collections import defaultdict

def count_valid_paths(n, m, a):
    cumulative_sum_clockwise = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        cumulative_sum_clockwise[i] = cumulative_sum_clockwise[i - 1] + a[(i - 1) % n]
    
    a_reversed = a[::-1]
    cumulative_sum_counterclockwise = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        cumulative_sum_counterclockwise[i] = cumulative_sum_counterclockwise[i - 1] + a_reversed[(i - 1) % n]
    
    def count_paths(cumulative_sum):
        remainder_count = defaultdict(int)
        count = 0
        for i in range(n + 1):
            remainder = cumulative_sum[i] % m
            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        return count

    count_clockwise = count_paths(cumulative_sum_clockwise)
    count_counterclockwise = count_paths(cumulative_sum_counterclockwise)

    overcounted_paths = 0
    for i in range(1, n):
        if (cumulative_sum_clockwise[i] - cumulative_sum_clockwise[0]) % m == 0:
            overcounted_paths += 1

    return count_clockwise + count_counterclockwise - overcounted_paths

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(count_valid_paths(n, m, a))
