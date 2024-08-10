n = int(input())
strings = [input() for _ in range(n)]

m = 0
for string in strings:
    m = max(m, len(string))

answers = [ list("あ" * n) for _ in range(m) ]

for i in range(n):
    try:
        for j in range(len(strings[i])):
            answers[j][n - i - 1] = strings[i][j]
        for j in range(len(strings[i]), m):
            answers[j][n - i - 1] = "あ"
    except:
        raise ValueError(f"i={i}, j={j} answers={answers} n-i-1={n-i-1} strings[i]={strings[i]}")
for answer in answers:
    answer = "".join(answer)
    # remove tailint "あ"
    answer = answer.rstrip("あ")
    # remove "あ" to "*"
    answer = answer.replace("あ", "*")
    print(answer)

