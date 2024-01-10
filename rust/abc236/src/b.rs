#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
		n: usize,
		a: [usize; 4*n-1],
    };
	let mut sum = (n * (n + 1))*2;
	for a_i in a {
		sum -= a_i;
	}
	println!("{}", sum);
}
