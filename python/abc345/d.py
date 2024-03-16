debug =True

from collections import deque
from copy import deepcopy
from re import T

n,h,w = map(int,input().split())

boxes = []

for _ in range(n):
    a,b = map(int,input().split())
    boxes.append((a,b))

q: list[int,list[str],int] = deque()

initial_index = -1
initial_state = list("." * w * h)
initial_place = 0
q.append((initial_index,initial_state,initial_place))

def update_state(state:str, y:int, x: int, place: int) -> tuple[str, int]:
    """
    stateに対して,縦y,横xの箱をplaceから置いたときの次の状態を返す
    """
    if debug:
        print("try to update_state")
        print(f"state: {state}")
        print(f"y: {y}, x: {x}, place: {place}")
    current_x = place % w
    current_y = place // w
    next_x = current_x + x
    next_y = current_y + y
    if next_x >= w + 1 or next_y >= h + 1:
        if debug:
            print("out of range")
        return state, -1
    next_state = deepcopy(state)
    for i in range(y):
        for j in range(x):
            if state[(current_y + i) * w + (current_x + j)] == "#":
                if debug:
                    print("already used")
                return state, -1
            next_state[(current_y + i) * w + (current_x + j)] = "#"
    
    # xの探索が全て完了した場合、左上で探索していない場所を返す    
    if next_x == w - 1:
        for i in range(h):
            for j in range(w):
                if next_state[i * w + j] == ".":
                    if debug:
                        print(f"next_place: {i * w + j}, i: {i}, j: {j}")
                        print("-----")
                        print(f"next_state: {next_state}")
                    return next_state, i * w + j
        return next_state, h * w
    else:
        next_place = current_y * w + next_x
        if debug:
            print(f"next_place: {next_place}, i: {next_x}, j: {current_y}")
            print("-----")
            print(f"next_state(2): {next_state}")
        return next_state, next_place

def check_all_used(state: list[str]) -> bool:
    return all([s == "#" for s in state])

count = 0

while len(q) > 0:
    count += 1
    if debug:
        print(f"count: {count}")
    last_index,state, place = q.popleft()
    if last_index == n-1:
        break
    next_index = last_index + 1
    # 1. Unused
    q.append((next_index,state, place))
    # 2. Ordinally Used
    next_state, next_place = update_state(state,boxes[next_index][0], boxes[next_index][1], place)
    if next_place == h * w or check_all_used(next_state):
        print("Yes")
        exit()
    if next_place != -1:
        if debug:
            print("Ordinally Used")
            print(next_index)
            print(next_state)
            print(next_place)
            print("-----")
        q.append((next_index, next_state, next_place))
    # 3. Transposed Used
    next_state, next_place = update_state(state,boxes[next_index][1], boxes[next_index][0], place)
    if next_place == h * w or check_all_used(next_state):
        print("Yes")
        exit()
    if next_place != -1:
        if debug:
            print("Transposed Used")
            print(next_index)
            print(next_state)
            print(next_place)
            print("-----")
        q.append((next_index, next_state, next_place))

print("No")