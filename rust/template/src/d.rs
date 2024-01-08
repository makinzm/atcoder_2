#[allow(unused_imports)]
use proconio::{
    fastout, input
};
use std::collections::VecDeque;

// Review: I fogot the feature of modulo operation.
// O(q) 
fn main() {
	let module = 998244353;
	input! {
		q: isize,
	}
	let mut state_stack = VecDeque::new();
	state_stack.push_back(1);
	let mut ans = 1;
	// O(q)
	for _ in 0..q{
		input! { order: isize }
		match order {
			1 => {
				input! { x: isize }
				state_stack.push_back(x);
				ans = (ans * 10 + x) % module;
			}
			2 => {
				let popped_state = state_stack.pop_front().unwrap();
				ans -= popped_state * (10_isize.pow(state_stack.len() as u32) % module);
				ans %= module;
			}
			3 => {
				println!("{}", ans);
				continue;
			}
			_ => {
				panic!("invalid order");
			}
		}
	}
}
