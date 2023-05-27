from collections import defaultdict

n = int(input())
u = []
pairs = defaultdict(set)

for _ in range(n-1):
    tmp = list(map(int,input().split()))
    u.append(tmp)
    pairs[tmp[0]-1].add(tmp[1]-1)
    pairs[tmp[1]-1].add(tmp[0]-1)

"""
星の最小単位は2
- 最後に孤立しているものの数で決められる.
- 孤立したものを切って行って考える方針でいく


- どう作成するか...?
  - 孤立判定は,要素でできる.
  - ただ,計算量が大変なことになりそう.
"""

count = 0
answers = []
while(True):
    kara_count = 0
    print(count)
    count+=1
    for i in range(n):
        print(i,pairs[i])
    
    removing_set = set()
    for i in range(n):
        if len(pairs[i])==1:
            removing_set.add(i)
            pairs[i] = set()
        elif len(pairs[i])==0:
            kara_count+=1
    for i in range(n):
        if not i in removing_set:
            for j in removing_set:
                try:
                    pairs[i].remove(j)
                except KeyError:
                    pass
    answers.append(len(removing_set))
    if kara_count==n:
        break

print(answers)
