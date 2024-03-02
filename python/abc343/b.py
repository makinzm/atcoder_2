n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    answers = []
    for i in range(len(a)):
        if a[i] == 1:
            answers.append(i+1)
    print(" ".join(map(str, answers)))
