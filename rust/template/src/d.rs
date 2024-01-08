#[allow(unused_imports)]
use proconio::{
    fastout, input
};
use std::collections::VecDeque;

// Review: I fogot the feature of modulo operation.
// O(q) 
fn main() {
	let module = 998244353;
	let overflow_limit = 200000;
	let mut pows_lst = vec![1];
	for _ in 0..overflow_limit{
		let last = *pows_lst.last().unwrap() as isize;
		pows_lst.push(last.checked_mul(10).unwrap().checked_rem_euclid(module).unwrap());
	}
	input! {
		q: isize,
	}
	let mut state_stack = VecDeque::new();
	state_stack.push_back(1);
	let mut ans: isize = 1;
	// O(q)
	for _ in 0..q{
		input! { order: isize }
		match order {
			1 => {
				input! { x: isize }
				state_stack.push_back(x);
				ans = (ans.checked_mul(10).unwrap() + x).checked_rem_euclid(module).unwrap();
			}
			2 => {
				let mut x = state_stack.pop_front().unwrap();
				x = x.checked_mul(pows_lst[state_stack.len()]).unwrap();
				ans = ans.checked_sub(x).unwrap_or_else(|| ans + module - x);
				ans = ans.checked_rem_euclid(module).unwrap();
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
