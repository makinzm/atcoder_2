#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

fn round_up_quotient(a: usize, b: usize) -> usize {
    (a + b - 1) / b
}

#[fastout]
fn main() {
	input! {
		a: usize,
		b: usize
	}
	println!("{}", round_up_quotient(a, b));
}
