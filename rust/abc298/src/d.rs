#[allow(unused_imports)]
use proconio::{
    fastout, input
};

// I have to care overflow...
// O(q) 
fn main() {
	let module = 998244353;
	input! {
		q: usize,
	}
	let mut start = 0;
	let mut stop = 1; // not included
	let mut state_stack = vec![1];
	let mut ans = (0, 1, 1, 1); // (start, stop, ans, ans % module)
	// O(2q) = O(q)
	for _ in 0..q{
		input! { order: usize }
		match order {
			1 => {
				input! { x: usize }
				stop += 1;
				state_stack.push(x);
			}
			2 => {
				start += 1;
			}
			3 => {
				let (pre_start, pre_stop, printed_ans, pre_ans) = ans;
				if pre_start == start && pre_stop == stop{
					println!("{}", printed_ans);
					continue;
				}
				let mut ans_up = pre_ans;
				if pre_start != start{
					ans_up %= 10_i32.pow((pre_stop - start) as u32);
				}
				ans_up *= 10_i32.pow((stop - pre_stop) as u32);
				let mut ans_down = 0;
				let mut count = 1;
				// O(stop - pre_stop) means O(q) in total
				for i in (pre_stop..stop).rev(){
					ans_down += state_stack[i] * count;
					count *= 10;
				}
				let true_ans = ans_up + ans_down as i32;
				ans = (start, stop, true_ans, true_ans % module);
				println!("{}", ans.3);
			}
			_ => {
				panic!("invalid order");
			}
		}
	}
}
