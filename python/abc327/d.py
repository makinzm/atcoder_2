# Pythonは参照渡しのため,更新が反映されることに注意

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

edges = []
for i in range(m):
    edges.append((a[i],b[i]))

def add_edge(graph: list[int], vertex_a: int, vertex_b: int) -> None:
    if vertex_a in graph:
        graph[vertex_a].add(vertex_b)
    else:
        graph[vertex_a] = {vertex_b}

def is_partially_cyclic(vertex: list[int], visited: dict[int,bool], parent: int, graph: dict[int,set[int]]) -> bool:
    visited[vertex] = True
    for neighbor in graph[vertex]:
        # 隣人に対して訪問をしていない場合
        if not visited[neighbor]:
            # 隣人に対して巡回がある場合
            if is_partially_cyclic(neighbor, visited, vertex, graph):
                return True
            # 隣人に対して巡回がない場合
            else:
                pass
        # 隣人に訪問済み にもかかわらず, それが 現在の親でない場合
        elif neighbor != parent:
            return True
    return False

def is_cyclic(edges: list[tuple[int,int]]) -> bool:
    graph = {}
    for edge in edges:
        a, b = edge
        add_edge(graph, a, b)
        add_edge(graph, b, a)
    
    visited = {i: False for i in graph}
    for vertex in graph:
        if not visited[vertex]:
            if is_partially_cyclic(vertex, visited, -1, graph):
                return True
    return False

print("No") if is_cyclic(edges) else print("Yes")
