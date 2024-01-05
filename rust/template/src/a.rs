// Here is a's problem
#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
		b: usize,
		g: usize,
	};
	if b > g{
		println!("Bat");
	}else{
		println!("Glove");
	}
}
