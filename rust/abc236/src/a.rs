#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
		s: String,
		a: usize,
		b: usize,
	}
	let (a, b) = (a - 1, b - 1);
	let mut s = s.chars().collect::<Vec<char>>();
	s.swap(a, b);
	println!("{}", s.into_iter().collect::<String>());
}
