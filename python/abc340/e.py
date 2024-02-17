from typing import Callable

n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

class LazySegmentTree:
    def __init__(self, n: int, op: Callable[[int, int], int], e: int, v: list):
        """
        Parameters
        ----------
        n : int
            要素数
        op : Callable[[int, int], int]
            クエリの演算
            例: min, max, gcd, lcm, +, *, ...
        e : int
            op の単位元
            例: 0, 1, inf, -inf
        v : list
            初期値

        Attributes
        ----------
        log : int
            n の 2 冪
        size : int
            セグメント木のサイズ
        data : list
            セグメント木のデータ
            区間の値と区間の長さを持つ
        lazy : list
            遅延データ
        """
        self.n = n
        self.op = op
        self.e = e
        self.log = (self.n - 1).bit_length()
        self.size = ( 1 << (self.log + 1) )
        self.data = [self.e] * self.size
        self.lazy = [self.id] * self.size

        for i in range(self.n):
            self.data[self.size//2+i] = v[i]
        for i in range(self.size//2-1, 0, -1):
            self.data[i] = self.op(self.data[i*2], self.data[i*2+1])
