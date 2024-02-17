#[allow(unused_imports)]
use proconio::{
    fastout, input
};

fn gcd(x: usize, y: usize) -> usize {
	if x < y {
		return gcd(y, x);
	}
	if y == 0 {
		return x;
	} else {
		return gcd(y, x % y);
	}
}

fn lcm(x: usize, y: usize) -> usize {
	return (x * y) / gcd(x, y);
}

#[fastout]
fn main() {
	input! {
		mut n: usize,
		mut m: usize,
		k: usize,
	}
	if n > m {
		let tmp = n;
		n = m;
		m = tmp;
	}
	let lcm_nm = lcm(n, m);
	let what_n = lcm_nm / n - 1;
	let what_m = lcm_nm / m - 1;
	let what = what_n + what_m;
	let turn = k / what;
	let min_turn = k % what;
	let base_ans = turn * lcm_nm;
	let mut current_n = base_ans;
	let mut current_n_index = 0;
	let mut current_m = base_ans;
	let mut current_m_index = 0;
	let mut ans_n = true;
	if min_turn == 0 {
		println!("{}", base_ans - n);
	} else {
		for _ in 0..min_turn {
			if current_n == current_m {
				current_n += n;
				current_n_index += 1;
				ans_n = true;
			} else {
				if current_n + n < current_m + m {
					current_n += n;
					current_n_index += 1;
					ans_n = true;
				} else {
					current_m += m;
					current_m_index += 1;
					ans_n = false;
				}
			}
		}
		if ans_n {
			println!("{}", base_ans + current_n_index * n);
		} else {
			println!("{}", base_ans + current_m_index * m);
		}
	}
}
