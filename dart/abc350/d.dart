import 'dart:io';

class UnionFind {
    int num;
    List<int> parent = [];

    UnionFind(this.num) {
        parent = List<int>.generate(num, (i) => -1);
    }

    int root(int x) {
        return parent[x] < 0 ? x : parent[x] = root(parent[x]);
    }

    bool unite(int x, int y) {
        x = root(x);
        y = root(y);
        if (x == y) return false;
        if (parent[x] > parent[y]) {
            final tmp = x;
            x = y;
            y = tmp;
        }
        parent[x] += parent[y];
        parent[y] = x;
        return true;
    }

    int size(int x) {
        return -parent[root(x)];
    }
}

int solve(int n, List<List<int>> friendsPairs) {
    final uf = UnionFind(n);
    List<List<int>> firstFriends = List.generate(n, (_) => []);
    for (final pair in friendsPairs) {
        uf.unite(pair[0], pair[1]);
        firstFriends[pair[0]].add(pair[1]);
        firstFriends[pair[1]].add(pair[0]);
    }

    int ans = 0;
    for (int i = 0; i < n; i++ ) {
        int size = uf.size(i);
        ans += size - firstFriends[i].length - 1;
    }
    return ans ~/ 2;
}

void main() {
    final input = stdin.readLineSync()!.split(' ');
    int n = int.parse(input[0]);
    int m = int.parse(input[1]);

    final friendsPairs = <List<int>>[];
    for (int i = 0; i < m; i++) {
        final pair = stdin.readLineSync()!.split(' ').map((e) => int.parse(e) - 1).toList();
        friendsPairs.add(pair);
    }

    print(solve(n, friendsPairs));
}

