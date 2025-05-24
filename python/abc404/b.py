n = int(input())

s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

def rotate_90(square_graph):
    n = len(square_graph)
    rotated_graph = []
    for i in range(n):
        new_row = []
        for j in range(n):
            new_row.append(square_graph[n - j - 1][i])
        rotated_graph.append(new_row)
    return rotated_graph

ans = n * n

for r in range(4):
    s_changed = s.copy()
    for j in range(r):
        s_changed = rotate_90(s_changed)
    current_ans = r
    for i in range(n):
        for j in range(n):
            if s_changed[i][j] != t[i][j]:
                current_ans += 1
    ans = min(ans, current_ans)

print(ans)

