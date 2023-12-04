#[allow(unused_imports)]
use proconio::{
    fastout, input
};

#[fastout]
fn main() {
	input!{
        n: usize, k: usize,
        a: [usize; n],
	}

	let mut a_count = 0;

	for i in 0..(n-k+1) {
		let partial_a = &a[i..(i+k)];
		// check whether partial_a is an increasing array
		if partial_a.windows(2).all(|w| w[0] < w[1]) {
			a_count += 1;
		}
	}

	println!("{}", a_count);
}
