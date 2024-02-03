#[allow(unused_imports)]
use proconio::{
    fastout, input
};
use std::cmp::min;
use num::checked_pow;
use std::collections::VecDeque;

#[fastout]
fn main() {
	input! {
		n: usize,
		s_list: [String; n]
	}

	let mut s_list = s_list;
	let mut visited_matrix = vec![vec![vec![vec![false; n]; n]; n]; n];

	for i in 0..n {
		if s_list[i].contains("P") {
			s_list[i] = s_list[i].replace("P", "Q");
			break;
		}
	}

	let mut p_x = 0 as isize;
	let mut p_y = 0 as isize;
	let mut q_x = 0 as isize;
	let mut q_y = 0 as isize;

	for i in 0..n {
		for j in 0..n {
			if s_list[i].chars().nth(j).unwrap() == 'P' {
				p_x = i as isize;
				p_y = j as isize;
			}
			if s_list[i].chars().nth(j).unwrap() == 'Q' {
				q_x = i as isize;
				q_y = j as isize;
			}
		}
	}

	let mut binary_heap = VecDeque::new();
	binary_heap.push_back([p_x, p_y, q_x, q_y, 0]);

	let mut ans_count = checked_pow(2, 30).unwrap();
	visited_matrix[p_x as usize][p_y as usize][q_x as usize][q_y as usize] = true;

	while binary_heap.len() > 0 {
		let [p_x, p_y, q_x, q_y, minus_count] = binary_heap.pop_front().unwrap();
		// println!("{:?}", [p_x, p_y, q_x, q_y, minus_count]);
		let count = - minus_count + 1;
		if count >= ans_count {
			continue;
		}
		for i in 0..4 {
			let mut new_p_x = p_x + [-1, 0, 1, 0][i];
			let mut new_p_y = p_y + [0, 1, 0, -1][i];
			let mut new_q_x = q_x + [-1, 0, 1, 0][i];
			let mut new_q_y = q_y + [0, 1, 0, -1][i];
			if new_p_x < 0 || new_p_x >= n as isize || new_p_y < 0 || new_p_y >= n as isize {
				new_p_x = p_x;
				new_p_y = p_y;
			} else if s_list[new_p_x as usize].chars().nth(new_p_y as usize).unwrap() == '#' {
				new_p_x = p_x;
				new_p_y = p_y;
			}
			if new_q_x < 0 || new_q_x >= n as isize || new_q_y < 0 || new_q_y >= n as isize {
				new_q_x = q_x;
				new_q_y = q_y;
			} else if s_list[new_q_x as usize].chars().nth(new_q_y as usize).unwrap() == '#' {
				new_q_x = q_x;
				new_q_y = q_y;
			}
			if new_p_x == new_q_x && new_p_y == new_q_y {
				ans_count = min(ans_count, count);
			} 
			if visited_matrix[new_p_x as usize][new_p_y as usize][new_q_x as usize][new_q_y as usize] {
				continue;
			}
			visited_matrix[new_p_x as usize][new_p_y as usize][new_q_x as usize][new_q_y as usize] = true;
			binary_heap.push_back([new_p_x, new_p_y, new_q_x, new_q_y, -count]);
		}
	}

	if ans_count == checked_pow(2, 30).unwrap() {
		println!("-1");
	} else {
		println!("{}", ans_count);
	}
}
