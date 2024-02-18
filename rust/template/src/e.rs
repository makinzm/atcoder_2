#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::clone::Clone;
use std::fmt::Debug;

trait Monoid {
	type S: Clone + Debug;
	fn op(a: &Self::S, b: &Self::S) -> Self::S;
	fn e() -> Self::S;
}

struct SegmentTree<M: Monoid> {
	n: usize,
	data: Vec<M::S>,
}

impl <M: Monoid> Debug for SegmentTree<M> {
	fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
		write!(f, "SegmentTree {{ n: {:?}, data: {:?} }}", self.n, self.data)
	}
}

impl <M: Monoid> SegmentTree<M> {
	fn new(n: usize) -> Self {
		let mut n_ = 1;
		while n_ < n {
			n_ *= 2;
		}
		SegmentTree {
			n: n_,
			data: vec![M::e(); 2 * n_ - 1],
		}
	}

	// set a[i] = x
	fn set(&mut self, i: usize, x: M::S) {
		let mut i = i as isize;
		i += self.n as isize - 1;
		self.data[i as usize] = x;
		while i > 0 {
			i = (i - 1) / 2;
			self.data[i as usize] = M::op(&self.data[i as usize * 2 + 1], &self.data[i as usize * 2 + 2]);
		}
	}

	// get op-Value in [l, r)
	fn get(&self, l: usize, r: usize) -> M::S {
		self.get_sub(l, r, 0, 0, self.n)
	}

	// get op-Value in [l, r)
	// k is the starting point
	// il, ir is the range which k-th node represents
	fn get_sub(&self, l: usize, r: usize, k: usize, il: usize, ir: usize) -> M::S {
		if ir <= l || r <= il {
			M::e()
		} else if l <= il && ir <= r {
			self.data[k].clone()
		} else {
			let x = self.get_sub(l, r, k * 2 + 1, il, (il + ir) / 2);
			let y = self.get_sub(l, r, k * 2 + 2, (il + ir) / 2, ir);
			M::op(&x, &y)
		}
	}
}

type Add = ();

impl Monoid for Add {
	type S = usize;
	fn op(a: &Self::S, b: &Self::S) -> Self::S {
		a + b
	}
	fn e() -> Self::S {
		0
	}
}

#[fastout]
fn main() {
	input! {
		n: usize,
		q: usize,
		s: usize,
		queries: [(usize, usize, usize); q],
	}
	let mut a = vec![0; n-1];
	let mut count = 0;
	for i in (1..=n-1).rev() {
		if s >> i & 1 == s >> (i - 1) & 1 {
			a[count] =  0;
		} else {
			a[count] = 1;
		}
		count += 1;
	}
	let mut st = SegmentTree::<Add>::new(n);
	for i in 0..n-1 {
		st.set(i, a[i]);
	}
	for (t, l, r) in queries {
		let l = l - 1;
		let r = r - 1;
		if t == 1 {
			if l != 0 && l != n-1 {
				let l_value = st.get(l-1, l);
				st.set(l-1, (l_value ^ 1) as usize);
			}
			if r != 0 && r != n-1 {
				let r_value = st.get(r, r+1);
				st.set(r, (r_value ^ 1) as usize);
			}
		} else {
			let get_sum = st.get(l, r);
			if get_sum == r - l {
				println!("Yes");
			} else {
				println!("No");
			}
		}
	}
}
