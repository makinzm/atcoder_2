#[allow(unused_imports)]
use proconio::{
    fastout, input
};
use std::collections::HashSet;

// Here is b's problem
// [B - Next](https://atcoder.jp/contests/abc329/tasks/abc329_b)

#[fastout]
fn main() {
	input!{
        n: usize,
        a: [usize; n],
	}

	let mut a_set = HashSet::new();
	let mut max_a = 0;

	for i in 0..n {
		let tmp_a = a[i];
		a_set.insert(tmp_a);
		if tmp_a > max_a {
			max_a = tmp_a;
		}
	}
	
	a_set.remove(&max_a);

	let mut second_a = 0;

	for tmp_a in &a_set {
		if tmp_a > &second_a {
			second_a = *tmp_a;
		}
	}

	println!("{}", second_a);
}
