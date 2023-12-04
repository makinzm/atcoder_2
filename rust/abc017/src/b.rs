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

	// separate a into a lot of increasing sequences
	let mut a_seq = vec![];
	let mut a_seq_len = 0;
	for i in 0..n-1 {
		if a[i] < a[i+1] {
			a_seq_len += 1;
		} else {
			a_seq.push(a_seq_len);
			a_seq_len = 0;
		}
	}
	a_seq.push(a_seq_len);
	
	for i in 0..a_seq.len() {
		if a_seq[i] >= k-1 {
			a_count += (a_seq[i] + 1) - k + 1;
		}
	}

	println!("{}", a_count);
}
