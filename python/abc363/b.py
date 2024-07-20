import numpy as np

num, threshold, minimum_person = map(int, input().split())

longs = np.array(list(map(int, input().split())))
days = 0

while(True):
    num_longer_person = np.sum(longs >= threshold)
    if num_longer_person >= minimum_person:
        break
    else:
        threshold -= 1
        days += 1

print(days)

