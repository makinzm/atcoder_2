#[allow(unused_imports)]
use proconio::{
    fastout, input
};

fn create_bin_vec(n: usize, max_digit: usize) -> Vec<usize>{
	let mut n = n;
	let mut bin_vec = vec![0; max_digit];
	for i in 0..max_digit{
		bin_vec[i] = n % 2;
		n /= 2;
	}
	bin_vec
}

#[fastout]
fn main() {
	input! {
		t: usize,
		as_lst: [[usize; 2]; t],
	}
	let max_digit = 63;
	for as_ in as_lst{
		let and = as_[0];
		let sum = as_[1];
		let and_vec = create_bin_vec(and, max_digit);
		let sum_vec = create_bin_vec(sum, max_digit);
		let mut carry = 0;
		let mut is_ok = true;
		let mut ans = 0;
		for i in 0..max_digit{
			if and_vec[i] == 1 && sum_vec[i] == 0 {
				if carry == 0 {
					carry = 1;
				} else {
					is_ok = false;
					break;
				}
			} else if and_vec[i] == 1 && sum_vec[i] == 1 {
				if carry == 1 {
					carry = 1;
					ans += 2usize.pow(i as u32);
				} else {
					is_ok = false;
					break;
				}
			} else if and_vec[i] == 0 && sum_vec[i] == 1 {
				carry = 0;
				ans += 2usize.pow(i as u32);
			} else if and_vec[i] == 0 && sum_vec[i] == 0 {
				carry = carry;
			}
		}
		if carry == 1 {
			ans += 2usize.pow(max_digit as u32);
		}
		if is_ok && ans == sum {
			println!("Yes");
		} else {
			println!("No");
		}
	}
}
