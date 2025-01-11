# Create A list whose length is n and all elements are random but 0 <= a[i] < 2**60
import random

n = 2 * 10**5
a = []
for i in range(n):
    a.append(random.randint(0, 2**60))
print(" ".join(map(str, a)))
