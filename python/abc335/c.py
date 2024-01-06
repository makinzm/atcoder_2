from copy import deepcopy

n, q = list(map(int, input().split()))
q_lst = []
for i in range(q):
    tmp_q = input().split()
    if tmp_q[0] == "1":
        q_lst.append([int(tmp_q[0]), tmp_q[1]])
    else:
        q_lst.append([int(tmp_q[0]), int(tmp_q[1]) - 1])

head_places = {}
current_state = [1,0]

head_places[0] = current_state

count = 0
for i in range(q):
    if q_lst[i][0] == 1:
        if q_lst[i][1] == "R":
            current_state[0] += 1
        elif q_lst[i][1] == "L":
            current_state[0] -= 1
        elif q_lst[i][1] == "U":
            current_state[1] += 1
        elif q_lst[i][1] == "D":
            current_state[1] -= 1
        count += 1
        head_places[count] = deepcopy(current_state)

count = 0

for i in range(q):
    if q_lst[i][0] == 1:
        count += 1
    else:
        if 1 + q_lst[i][1] > count:
            back_number = 1 + q_lst[i][1] - count
            print(back_number, 0)
        else:
            back_number = count - q_lst[i][1]
            print(head_places[back_number][0], head_places[back_number][1])
