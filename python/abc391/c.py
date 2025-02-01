n,q = map(int, input().split())

queryies = [input().split() for _ in range(q)]

ans = 0
pegion_places = dict()
for i in range(1, n+1):
    pegion_places[i] = i
place_pegions = dict()
for i in range(1, n+1):
    place_pegions[i] = set([i])

for query in queryies:
    if query[0] == "1":
        pegion, nest = map(int, query[1:])
        pegion_place = pegion_places[pegion]
        if len(place_pegions[pegion_place]) == 2:
            ans -= 1
        place_pegions[pegion_place].remove(pegion)
        if len(place_pegions[nest]) == 1:
            ans += 1
        place_pegions[nest].add(pegion)
        pegion_places[pegion] = nest
    else:
        print(ans)

