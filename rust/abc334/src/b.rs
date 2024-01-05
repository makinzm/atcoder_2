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
	let (min_k, max_k): (isize, isize);
	if (l-a) % m == 0 {
		min_k = (l-a).div_euclid(m);
	} else {
		min_k = (l-a).div_euclid(m) + 1;
	}
	max_k = (r-a).div_euclid(m);
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
