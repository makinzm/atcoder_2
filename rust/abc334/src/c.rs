#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::cmp::{min};

#[fastout]
fn main(){
	input!{
		_n: usize,
		k: usize,
		a: [isize; k],
	};
	if k < 2{
		println!("{}",0);
		return;
	}
	/*
	Basically, it is ok to only think about k because complete pair loss become 0 and it is best.
	If k is odd, there is one sock which is not paired.
	*/
	let mut _sum_diff_all = 0;
	let mut sum_diff_odd = 0;
	let mut sum_diff_even = 0;
	for i in 0..k-1{
		_sum_diff_all += (a[i] - a[i+1]).abs();
		if i % 2 == 0{
			sum_diff_even += (a[i] - a[i+1]).abs();
		} else {
			sum_diff_odd += (a[i] - a[i+1]).abs();
		}
	}
	let mut min_ans = sum_diff_even;

	let mut current_sum_even = 0;
	let mut current_sum_odd = 0;
	let mut current_sum_even_last = sum_diff_even;
	let mut current_sum_odd_last = sum_diff_odd;
	if k % 2 == 0{
		println!("{}", min_ans);
		return;
	}
	for i in 0..k{
		// println!("min_ans {}, current_sum_even {}, current_sum_odd {}, current_sum_even_last {}, current_sum_odd_last {}", min_ans, current_sum_even, current_sum_odd, current_sum_even_last, current_sum_odd_last);
		if i % 2 == 0{
			min_ans = min(
				min_ans,
				current_sum_odd_last + current_sum_even
			);
			if i == k-1{
				break;
			}
			current_sum_even += (a[i] - a[i+1]).abs();
			current_sum_even_last -= (a[i] - a[i+1]).abs();
		} else {
			min_ans = min(
				min_ans,
				current_sum_even_last + current_sum_odd
			);
			if i == k-1{
				break;
			}
			current_sum_odd += (a[i] - a[i+1]).abs();
			current_sum_odd_last -= (a[i] - a[i+1]).abs();
		}
		// println!("{} {} {} {}", current_sum_even, current_sum_odd, current_sum_even_last, current_sum_odd_last);
		// println!("{}", min_ans);
	}
	
	println!("{}", min_ans);
}
