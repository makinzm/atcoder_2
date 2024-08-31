n = int(input())

right_hand = -1
left_hand = -1

right_fatigue = 0
left_fatigue = 0

for i in range(n):
    a,s = input().split()
    a = int(a)
    if s == "R":
        if right_hand == -1:
            right_hand = a
        else:
            right_fatigue += abs(right_hand - a)
            right_hand = a
    else:
        if left_hand == -1:
            left_hand = a
        else:
            left_fatigue += abs(left_hand - a)
            left_hand = a

print(right_fatigue + left_fatigue)

