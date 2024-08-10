class FenwickTree3D:
    def __init__(self, n):
        self.n = n
        self.BIT = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    def update(self, x, y, z, delta):
        xi = x
        while xi <= self.n:
            yi = y
            while yi <= self.n:
                zi = z
                while zi <= self.n:
                    self.BIT[xi][yi][zi] += delta
                    zi += zi & -zi
                yi += yi & -yi
            xi += xi & -xi

    def sum(self, x, y, z):
        total = 0
        xi = x
        while xi > 0:
            yi = y
            while yi > 0:
                zi = z
                while zi > 0:
                    total += self.BIT[xi][yi][zi]
                    zi -= zi & -zi
                yi -= yi & -yi
            xi -= xi & -xi
        return total

    def range_sum(self, x1, y1, z1, x2, y2, z2):
        return (self.sum(x2, y2, z2)
                - self.sum(x1 - 1, y2, z2)
                - self.sum(x2, y1 - 1, z2)
                - self.sum(x2, y2, z1 - 1)
                + self.sum(x1 - 1, y1 - 1, z2)
                + self.sum(x1 - 1, y2, z1 - 1)
                + self.sum(x2, y1 - 1, z1 - 1)
                - self.sum(x1 - 1, y1 - 1, z1 - 1))

def main():
    N = int(input())
    fenwick_tree = FenwickTree3D(N)

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            values = list(map(int, input().split()))
            for z in range(1, N + 1):
                fenwick_tree.update(x, y, z, values[z - 1])

    Q = int(input())
    for _ in range(Q):
        Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
        result = fenwick_tree.range_sum(Lx, Ly, Lz, Rx, Ry, Rz)
        print(result)

if __name__ == "__main__":
    main()
