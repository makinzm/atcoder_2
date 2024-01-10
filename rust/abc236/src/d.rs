#[allow(unused_imports)]
use proconio::{
    fastout, input
};
use std::collections::VecDeque;
use itertools::Itertools;

trait Factorial {
	fn factorial(self) -> Self;
}
impl Factorial for usize {
	fn factorial(self) -> Self {
		(1..=self).product()
	}
}

fn main() {
	input! {
		n: usize,
	}
	let mut a = VecDeque::new();
	for i in 0..2*n - 1 {
		let mut a_i = VecDeque::new();
		for _ in 0..2*n - i - 1 {
			input! {
				tmp: usize,
			}
			a_i.push_back(tmp);
		}
		a.push_back(a_i);
	}
	// Number of pattterns is (2n)! / (2^n * n!)
	// Just in case, add 100
	let num_of_patterns = 1000000 + ((2*n).factorial()).div_euclid(2usize.pow(n as u32) * (n.factorial()));

	let mut ans = 0;
	let mut count = 0;
	for perm in (0..2*n).permutations(2*n as usize) {
		count += 1;
		if count > num_of_patterns {
			break;
		}
		let mut sum = 0;
		for j in (0..2*n).step_by(2) {
			let mut first = perm[j];
			let mut second = perm[j + 1];
			if first > second {
				let tmp = first;
				first = second;
				second = tmp;
			}
			sum ^= a[first][second - first - 1];
		}
		ans = std::cmp::max(ans, sum);
	}
	println!("{}", ans);
}
