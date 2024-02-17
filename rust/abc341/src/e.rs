#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main(){
	input!{
		n : usize,
		q : usize,
		mut s : u64,
	}
	let mut next_bit = 0;
	for _ in 0..q {
		input!{
			t: usize,
			mut l: usize,
			mut r: usize,
		}
		l = n - (l);
		r = n - (r);
		if t == 1 {
			for i in r..=l {
				next_bit ^= (1 << i);
			}
		} else {
			s ^= next_bit;
			next_bit = 0;
			let mut ans = "Yes";
			let mut current_bit = (s >> r) & 1;
			for i in r+1..=l {
				let mut next_bit = (s >> i) & 1;
				if current_bit == next_bit {
					ans = "No";
					break;
				}
				current_bit = next_bit;
			}
			println!("{}", ans);
		}
	}
}
