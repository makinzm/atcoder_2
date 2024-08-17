from itertools import product

def generate_arrays(n):
    # 1から5までの数字をn個使った全ての組み合わせを生成
    arrays = list(product(range(1, 6), repeat=n))
    return arrays

n, k = map(int,input().split())
result = generate_arrays(n)

a = list(map(int, input().split()))

ans_lst = []

for i in result:
    for index, j in enumerate(i):
        if 1 <= j <= a[index]:
            pass
        else:
            break
        if index == n-1:
            ans_lst.append(i)

sorted_ans_lst = sorted(ans_lst)

for i in sorted_ans_lst:
    if sum(i) % k == 0:
        print(" ".join(map(str, i)))

