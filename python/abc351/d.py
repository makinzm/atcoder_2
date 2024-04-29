# Reference: 
# riened, 2024-04-27, AtCoder, accessed 2024-04-28
# https://atcoder.jp/contests/abc351/submissions/52863630

from collections import deque

h,w = map(int, input().split())
s = [input() for _ in range(h)]

# 0 means liberty when DFS
# -1 means wall or not started point when DFS
# i which is greater than 0 means stuck, 
#   whose value is the DFS iteration id started from 2 (initial value is 1)
matrix = [0 for i_j in range(h*w)]

directions = ((0,1), (1,0), (0,-1), (-1,0))

def is_over(i, j):
    return i < 0 or i >= h or j < 0 or j >= w

ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            matrix[i*w+j] = -1
            for dir in directions:
                ni = i+dir[0]
                nj = j+dir[1]
                # Check stuck point
                if not is_over(ni, nj) and matrix[ni*w + nj] == 0:
                    matrix[ni*w + nj] = 1

iteration_id = 2

def dfs(i, j) -> int:
    global iteration_id

    ans = 0
    # Starting point is a wall or an already checked point
    if matrix[i*w+j] == -1:
        return ans
    # Starting point is a stuck point
    if matrix[i*w+j] > 0:
        ans += 1
        return ans
    
    q = deque()

    def act_for_new_liberty(x, y) -> None:
        """
        Act for new liberty point.
        1. Mark this point in-available from available liberty point
        2. Increment count
        3. Append this point to the queue
        """
        nonlocal ans        
        # This point is already checked in this DFS,
        # so we don't have to start from this point
        matrix[x*w+y] = -1
        # This point is liberty point, so increment count
        ans += 1
        q.append((x, y))
    
    def partial_dfs(x, y) -> None:
        nonlocal ans
        for dir in directions:
            nx = x + dir[0]
            ny = y + dir[1]
            if is_over(nx, ny):
                continue
            # Available liberty point
            if matrix[nx*w+ny] == 0:
                act_for_new_liberty(nx, ny)
            # Available stuck point
            elif matrix[nx*w+ny] != -1 and matrix[nx*w+ny] != iteration_id:
                matrix[nx*w+ny] = iteration_id
                ans += 1
    
    act_for_new_liberty(i, j)
    while len(q) > 0:
        x, y = q.popleft()
        partial_dfs(x, y)
    return ans

for i in range(h):
    for j in range(w):
        localized_ans = dfs(i, j)
        ans = max(ans, localized_ans)
        iteration_id += 1

print(ans)
