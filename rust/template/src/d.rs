#[allow(unused_imports)]
use proconio::{
    fastout, input
};

use std::collections::{
	HashMap
};

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

	println!("{}",s);

	for (t,x,c) in txc{
		for (key, value) in &current_upper {
			println!("Key: {}, Value: {}", key, value);
		}
		if t == 1 {
			println!("1");
			let x_minus_one = x - 1;
			current_upper.insert(
				x_minus_one,
				c.is_uppercase()
			);
			current_string.insert(
				x_minus_one,
				c
			);
		} 
		if t == 2 {
			println!("2");
			for i in 0..n{
				current_upper.insert(
					i,
					true
				);
			}
		} 
		if t == 3{
			println!("3");
			for i in 0..n{
				current_upper.insert(
					i,
					false
				);
			}
		}
	}

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
