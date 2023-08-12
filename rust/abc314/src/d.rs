#[allow(unused_imports)]
use proconio::{
    fastout, input
};

use std::collections::{
	HashMap
};

use std::cmp;

// https://atcoder.jp/contests/abc314/tasks/abc314_d
#[fastout]
fn main() {
	input! {
		n: usize,
		s: String,
		q: usize,
		txc: [(usize, usize, char); q],
	}

	let bytes = s.as_bytes();
	let mut current_upper = HashMap::new();

	for i in 0..n{
		let byte_at_index = bytes[i];
		let character = char::from(byte_at_index);
		current_upper.insert(
			i,
			character.is_uppercase()
		);
	}

	let mut current_string = HashMap::new();
	for i in 0..n{
		let byte_at_index = bytes[i];
		let character = char::from(byte_at_index);
		current_string.insert(i,character);
	}

	let mut last_time = 0;

	for (iter,element) in txc.iter().enumerate(){
		match element {
            (t, _x, _c) => {
				if *t == 2 {
					last_time = cmp::max(last_time, iter);
				} 
				if *t == 3{
					last_time = cmp::max(last_time, iter);
				}
			}
		}
	}

	for (iter,element) in txc.iter().enumerate(){
		// for (key, value) in &current_upper {
		// 	println!("Key: {}, Value: {}", key, value);
		// }
		// for (key, value) in &current_string {
		// 	println!("Key: {}, Value: {}", key, value);
		// }
		match element {
            (t, x, c) => {
				if *t == 1 {
					let x_minus_one = x - 1;
					if iter >= last_time {
						current_upper.insert(
							x_minus_one,
							c.is_uppercase()
						);
					}
					current_string.insert(
						x_minus_one,
						*c
					);
				} 
				if *t == 2 && iter >= last_time {
					for i in 0..n{
						current_upper.insert(
							i,
							false
						);
					}
				} 
				if *t == 3 && iter >= last_time{
					for i in 0..n{
						current_upper.insert(
							i,
							true
						);
					}
				}
			}
		}
	}

	// for (key, value) in &current_upper {
	// 	println!("Key: {}, Value: {}", key, value);
	// }
	// for (key, value) in &current_string {
	// 	println!("Key: {}, Value: {}", key, value);
	// }

	for i in 0..n {
		let current_upper_value = current_upper.get(&i).expect("Value not found");
		let current_string_value = current_string.get(&i).expect("Value not found");
		
		if *current_upper_value {
			print!("{}", current_string_value.to_ascii_uppercase());
		} else {
			print!("{}", current_string_value.to_ascii_lowercase());
		}
	}
	
	println!("");
}
