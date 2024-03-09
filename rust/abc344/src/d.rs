#[allow(unused_imports)]
use proconio::{
    fastout, input, marker::Chars
};
use std::collections::VecDeque;


#[fastout]
fn main() {
	input! {
		t: Chars,
		n: usize,
	}
	let mut a = vec![];
	for _ in 0..n {
		input! {
			ai_n: usize,
			ai: [Chars; ai_n]
		}
		a.push(ai);
	}

	let n_t = t.len();
	let a_used = vec![vec![]; n];
	let mut ans = 200;

	let mut q = VecDeque::new();
	q.push_back((0, 0, a_used.clone()));

	while let Some((how_much, now, a_used)) = q.pop_front() {
		for i in 0..n {
			if a_used[i].len() != a[i].len() {
				for (j, a_j) in a[i].iter().enumerate() {
					if now + a_j.len() <= n_t && a_j.iter().eq(&t[n_t - now - a_j.len()..n_t - now]) {
						let mut _a_used = a_used.clone();
						_a_used[i].push(j);
						if now + a_j.len() < n_t {
							q.push_back((how_much + 1, now + a_j.len(), _a_used));
						} else {
							ans = ans.min(how_much + 1);
						}
					}
				}
			}
		}
	}

	println!("{}", if ans != 200 { ans } else { -1 });
}
