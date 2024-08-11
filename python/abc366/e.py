n, d = map(int, input().split())

x = []
y = []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

max_x = 10 ** 6 + d

def calc(xs):
    # - max_x <= x <= max_x
    # x_sum(x) = x_sum[x]
    x_sum = [0] * (max_x * 2 + 1)
    sorted_xs = sorted(xs)
    # Sum(|-max_x-xi|) = Sum(max_x+xi)
    x_sum[-max_x] = sum(xs) + max_x * n

    # x_i < x を満たす x_i の個数
    i = 0
    for x in range(-max_x + 1, max_x + 1):
        while i < n and sorted_xs[i] < x:
            i += 1
        # x_sum(x) = Sum(|x-xj|) = 1_{0<=j<=i_x} Sum(x-xj) + 1_{i_x<j<n} Sum(xj-x)
        # = 1_{0<=j<=i_x} Sum(x-1 - xj + 1) + 1_{i_x<j<n} Sum(xj - (x+1) + 1)
        # = 1_{0<=j<=i_x} Sum(x-1 - xj) + 1_{i_x<j<n} Sum(xj - x) - 1_{i_x<j<n} + 1_{0<=j<=i_x}
        # x_sum(x-1)
        # = Sum(|x-1-xj|) = 1_{0<=j<=i_(x-1)} Sum(x-1-xj) + 1_{i_(x-1)<j<n} Sum(xj-x+1)
        # ここで i_(x-1) <= i_x であることに注意して式変形をすると
        # x_sum(x) - x_sum(x-1) = (x-1 - x_(i_x)) - (x_(i_x) - (x-1)) - 1_{i_x<j<n} + 1_{0<=j<=i_x}
        # = - (n - i_x) - i_x
        x_sum[x] = x_sum[x - 1] + i - (n - i)
    return x_sum

x_sum = calc(x)
y_sum = calc(y)

# 尺取り法は、ある区間に対して、その区間を左端から右端まで動かすことで、その区間に対する条件を満たす区間を求めるアルゴリズムです。
# そのため、以下でソートを行うことで、x_sum, y_sum に対して尺取り法を行うことができます。
x_sum.sort()
y_sum.sort()

ans = 0
y_index = 0

for x_index in range(len(x_sum))[::-1]:
    # x_index - 1 よりも x_index のほうが x_sum の値が小さいため もっと y_index を進められるか確かめる
    while y_index < len(y_sum) and y_sum[y_index] + x_sum[x_index] <= d:
        y_index += 1
    ans += y_index

print(ans)


