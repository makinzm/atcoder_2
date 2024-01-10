#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main(){
	input!{
		n: usize,
		m: usize,
		s: [String; n],
		t: [String; m],
	};
	let mut s_count = 0;
	let mut t_count = 0;
	for _ in 0..n {
		if s[s_count] == t[t_count] {
			println!("Yes");
			s_count += 1;
			t_count += 1;
		} else {
			println!("No");
			s_count += 1;
		}
	}
}
