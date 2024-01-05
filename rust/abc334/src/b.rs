#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
		a: isize,
		m: isize,
		l: isize,
		r: isize,
    };
	let min_k: isize = (((l as f64)-(a as f64))/(m as f64)).ceil() as isize;
	let max_k: isize = (((r as f64)-(a as f64))/(m as f64)).floor() as isize;
	// println!("min_k: {}, max_k: {}", min_k, max_k);
	if min_k > max_k {
		println!("{}", 0);
		return;
	} else if min_k == max_k {
		if a + min_k*m >= l && a + min_k*m <= r {
			println!("{}", 1);
			return;
		} else {
			println!("{}", 0);
			return;
		}
	}
	println!("{}", max_k - min_k + 1);
}
