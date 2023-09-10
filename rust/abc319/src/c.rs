// ABC 319

#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

use itertools::Itertools;

// use factorial::Factorial;

// #[derive(Debug)]
struct Line {
	first: Option<usize>,
	second: Option<usize>,
	third: Option<usize>,
}

impl Clone for Line {
    fn clone(&self) -> Self {
        Line {
            first: self.first.clone(),
            second: self.second.clone(),
            third: self.third.clone(),
        }
    }
}

impl Line{
	fn insert_to_next(&mut self, value: usize){
		// https://doc.rust-lang.org/std/option/enum.Option.html#method.is_none
		// https://doc.rust-lang.org/std/option/enum.Option.html#method.as_mut
		// if let Some(first) = self.first.as_mut()
		if self.first.is_none() {
			self.first = Some(value);
		} else if self.second.is_none() {
			self.second = Some(value);
		} else if self.third.is_none() {
			self.third = Some(value);
		} else {
			panic!("This is a terrible mistake!");
		}
	}

	fn check_safe(&self) -> bool {
		let judge;
		if let (Some(first), Some(second), Some(third)) = (self.first, self.second, self.third) {
			judge = first == second && first != third;
			// println!("first,second,third: {},{},{} -> {}", first,second,third, judge);
			return !judge;
		}
		panic!("This is a terrible mistake!");
	}
}

// #[derive(Debug)]
struct Diagonal{
	downward: Line,
	upward: Line,
}

// #[derive(Debug)]
#[allow(dead_code)]
struct Field {
	n: usize,
	// the size of square
	horizontals: Vec<Line>,
	// If values have the same quotient of n, each of them belongs to the same group.
	verticals: Vec<Line>,
	// If values have the same remainder of n, each of them belongs to the same group.
	diagonals: Diagonal,
	// there are just two patterns,
	// For a value, if a remaindar is equals to a quotient => downward
	// For a value, let value be Q x n + (n-1) - R , if a remaindar is equals to a quotient => upward
}

impl Field{
	fn check(&self) -> bool{
		for horizontal in &self.horizontals{
			if !(horizontal.check_safe()){
				return false;
			}
		}
		for vertical in &self.verticals{
			if !(vertical.check_safe()){
				return false;
			}
		}
		if ! (self.diagonals.downward.check_safe()){
			return false;
		}
		if ! (self.diagonals.upward.check_safe()){
			return false;
		}
		true
	}
}

const N: usize = 3;
const NN: usize = N * N;

#[fastout]
fn main(){
	input!{
		c: [usize;NN]
	};
	let ans = calculate(c);
	println!("{}", ans);
}

fn calculate(c: Vec<usize>) -> f64 {
	// println!("{:?}", c);

	let mut factorial_9 = 0;
	let mut num_safe = 0;
	// https://docs.rs/itertools/0.11.0/itertools/trait.Itertools.html#method.permutations
	for p in (0..NN).permutations(NN) {
		// for mut p in (0..NN).permutations(NN) {
		// p = (0..=8).rev().collect();

		factorial_9 += 1;
		// ERROR: the trait `std::marker::Copy` is not implemented for `Line`
		// let mut horizontals = [Line{first: None, second: None, third: None}; N].to_vec();
		let horizontals = vec![Line{first: None, second: None, third: None}; N];
		let verticals = vec![Line{first: None, second: None, third: None}; N];
		let diagonals = Diagonal{
			downward: Line{first: None, second: None, third: None}, 
			upward: Line{first: None, second: None, third: None}
		};
		let mut field = Field{
			n: N,
			horizontals,
			verticals,
			diagonals
		};
		for i in 0..NN {
			let place = p[i];
			let q = place / N;
			let r = place % N;
			let rev_place = q * N + (N-1) - r;
			let rev_q = rev_place / N;
			let rev_r = rev_place % N;
			field.horizontals[q].insert_to_next(c[p[i]]);
			field.verticals[r].insert_to_next(c[p[i]]);
			if q == r{
				field.diagonals.downward.insert_to_next(c[p[i]]);
			}
			if rev_q == rev_r{
				field.diagonals.upward.insert_to_next(c[p[i]]);
			}
		}
		if field.check(){
			num_safe += 1;
		}
		// println!("p: {:?}", p);
		// println!("Field: {:?}", field);
		// break; // println
	}
	let ans = (num_safe as f64) / (factorial_9 as f64);
	return ans;
}
