#include <iostream>
#include <vector>
#include <numeric> // For std::iota

using namespace std;

constexpr int nmax = 200200*2;
int A[nmax], B[nmax];
int parent[nmax];
int rankTree[nmax];

/**
 * Find the parent of x.
 *
 * @param x The element to find the set for.
 * @return The representative of the set that x belongs to.
 */
int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}

/**
 * Union by rankTree function.
 * It joins two subsets into a single subset, by attaching the tree with less rankTree
 * to the root of the tree with more rankTree.
 *
 * @param x An element of the first set.
 * @param y An element of the second set.
 */
void unite(int x, int y) {
    int xRoot = find(x);
    int yRoot = find(y);

    if (xRoot == yRoot) return;

    // Attach smaller rankTree tree under root of high rankTree tree
    if (rankTree[xRoot] < rankTree[yRoot]) {
        parent[xRoot] = yRoot;
    } else if (rankTree[yRoot] < rankTree[xRoot]) {
        parent[yRoot] = xRoot;
    } else {
        // If rankTrees are same, then make one as root and increment its rankTree by one
        parent[yRoot] = xRoot;
        rankTree[xRoot]++;
    }
}

/**
 * Checks if a graph is bipartite using the union-find algorithm.
 * In current situation, we think the pair of a[i] and a[i+N] regarding the conditions if X_i is 0 or 1.
 * If that X_i is 0 occurs as that X_i is 1 does, it means we cannot create X meeting the problem's condition.
 *
 * @param N The number of vertices in the graph.
 * @param M The number of edges in the graph.
 * @param edges A vector of pairs, where each pair represents an edge between two vertices.
 * @return True if the graph is bipartite, otherwise false.
 */
bool isBipartite(int N, int M, const vector<pair<int, int>>& edges) {
    iota(parent, parent + 2*N, 0); // Initialize each element's parent to itself
    fill(rankTree, rankTree + 2*N, 0); // Initialize each element's rankTree to 0

    for (const auto& edge : edges) {
        // Combine the subsets to which the two vertices belong
        unite(edge.first, edge.second+N);
        unite(edge.first+N, edge.second);
    }

    for (int i = 0; i < N; i++) {
        int xRoot = find(parent[i]);
        int yRoot = find(parent[i+N]);
        if (xRoot == yRoot) {
            return false;
        }
    }

    return true;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<pair<int, int>> edges;

    for (int i = 0; i < M; i++) cin >> A[i], A[i]--;
    for (int i = 0; i < M; i++) cin >> B[i], B[i]--;

    for (int i = 0; i < M; i++) {
        edges.emplace_back(A[i], B[i]);
    }

    cout << (isBipartite(N, M, edges) ? "Yes" : "No") << endl;

    return 0;
}
