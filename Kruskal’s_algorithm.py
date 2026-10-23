def kruskal(vertices, edges):
    parent = {v: v for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    edges.sort(key=lambda x: x[2])
    mst = []
    cost = 0

    for u, v, w in edges:
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            mst.append((u, v, w))
            cost += w
            parent[root_u] = root_v

    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Total Cost:", cost)


vertices = [0, 1, 2, 3]

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(vertices, edges)
