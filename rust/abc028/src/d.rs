#[allow(unused_imports)]
use proconio::{
    fastout, input
};

#[fastout]
fn main() {
	input! {
		n: usize,
		k: usize,
	}

	let numerator = (n - k) * (k - 1) * 6 + (n - 1) * 3 + 1;

	let denominator = n * n * n;
	
	println!("{}", numerator as f64 / denominator as f64);
}
