from bisect import bisect_right

DEBUG = True

n = int(input())

max_prime = int(n ** 0.5)

def eratosthenes(n):
    prime_list = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            prime_list.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return prime_list

prime_list = eratosthenes(max_prime)
prime_set = set(prime_list)

root_n = n ** 0.5
int_root_n = int(root_n)

ans = 0
for i in prime_list:
    current_y_max = root_n // i
    index = bisect_right(prime_list, current_y_max)
    if prime_list[index - 1] > i:
        index -= 1
    ans += max(0, index)
ans //= 2

root_8 = n ** 0.125
int_root_8 = int(root_8)

ans += bisect_right(prime_list, int_root_8)

print(int(ans))

