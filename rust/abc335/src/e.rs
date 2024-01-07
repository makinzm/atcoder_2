#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::cmp::{max};
use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct UnionFind {
  data: Vec<isize>,
}

impl UnionFind {
  fn new(size: usize) -> UnionFind {
	/*
	data means:
	- if data[i] < 0, i is root and |data[i]| is the size of the group
	- if data[i] >= 0, i is not root and data[i] is the parent of i
	 */
	UnionFind{data: vec![-1; size]}
  }
  fn root(&mut self, x: usize) -> usize {
	if self.data[x] < 0 {
		x
	} else {
		let parent = self.data[x] as usize;
		let root = self.root(parent);
		self.data[x] = root as isize;
		root
	}
  }
  fn unite(&mut self, x: usize, y: usize){
		let mut x = self.root(x) as usize;
		let mut y = self.root(y) as usize;
		if x == y {
		return;
		} else {
		if self.data[x] > self.data[y] {
			std::mem::swap(&mut x, &mut y);
		}
		self.data[x] += self.data[y];
		self.data[y] = x as isize;
		}
	}
}

#[fastout]
#[allow(unused_doc_comments)]
fn main() {
	input! {
		n: usize,
		m: usize,
		a: [usize; n],
		edges: [(usize, usize); m],
	}
	let mut uf = UnionFind::new(n);
	// In this official answer, they use Vector<Vector<(usize,usize)>> (vector[a_u] = [(u, v_1), (u, v_2), ...])
	// It can guarantee that the order of edges is ascending order of a_u.
	let mut vector: BinaryHeap<Reverse<(usize, usize, usize)>> = BinaryHeap::new();
	for edge in edges{
		let (u, v) = edge;
		let (a_u ,a_v) = (a[u-1], a[v-1]);
		if a_u > a_v{
			vector.push(Reverse((a[v-1], v-1, u-1)));
		} else if a_u < a_v{
			vector.push(Reverse((a[u-1], u-1, v-1)));
		} if a_u == a_v{
			uf.unite(u-1, v-1);
		}
	}
	let mut dp = vec![0; n];
	dp[uf.root(0)]=1;
	while let Some(Reverse(value)) = vector.pop() {
		let (_, u, v) = value;
		let (u_root, v_root) = (uf.root(u), uf.root(v));
		if dp[u_root] > 0 {
			dp[v_root] = max(dp[v_root], dp[u_root] + 1);
		}
    }
	println!("{}", dp[uf.root(n-1)]);
}
