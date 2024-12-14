scores = list(map(int, input().split()))

score_map = {
    'A': scores[0],
    'B': scores[1],
    'C': scores[2],
    'D': scores[3],
    'E': scores[4]
}

candidates_string = """ABCDE
BCDE
ACDE
ABDE
ABCE
ABCD
CDE
BDE
ADE
BCE
ACE
BCD
ABE
ACD
ABD
ABC
DE
CE
BE
CD
AE
BD
AD
BC
AC
AB
E
D
C
B
A"""

candidates = candidates_string.split('\n')

def calculate_score(candidate):
    return sum([score_map[c] for c in candidate])

candidates_with_score = [(candidate, calculate_score(candidate)) for candidate in candidates]

sorted_candidates_score_and_alphabet = sorted(candidates_with_score, key=lambda x: (-x[1], x[0]))

[print(candidate) for candidate, score in sorted_candidates_score_and_alphabet]
