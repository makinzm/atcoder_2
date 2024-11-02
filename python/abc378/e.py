n, m = map(int, input().split())
a = list(map(int, input().split()))

# 結果を計算する
total_sum = 0

# 各 A[i] が含まれる (l, r) の組み合わせを数える
for i in range(1, n + 1):
    # A[i-1] が含まれるのは (1, i) から (i, n) までの (i * (n - i + 1)) 組
    left_count = i      # 1 から i までの選び方
    right_count = n - i + 1  # i から n までの選び方
    contribution = a[i - 1] * left_count * right_count
    total_sum += contribution

cumulative_sum = [0] * (n + 1)
for i in range(1, n + 1):
    cumulative_sum[i] = cumulative_sum[i - 1] + a[i - 1]

how_many_times_over_m = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if cumulative_sum[j] - cumulative_sum[i - 1] > m:
            how_many_times_over_m += (cumulative_sum[j] - cumulative_sum[i - 1]) // m

total_sum -= how_many_times_over_m * m

print(total_sum)

