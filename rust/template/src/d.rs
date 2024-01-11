#[allow(unused_imports)]
use proconio::{
    fastout, input
};
use std::cmp::max;

/// Full Search by DFS
/// 
/// `a` means adjacency list
/// `pairs` means pairs of vertexes
/// `visited` means whether vertex is visited or not
/// 
/// Returns the maximum value among all possible combinations that can be considered after pairs is passed.
/// 
/// # Warning
/// The variable `first` is the minimum value in unvisited vertexes i.e. fixed vertex given by `pairs` and `visited`.
/// However, the variable `second` is not fixed vertex given by `pairs` and `visited`.
/// 
/// The changes of `pairs` and `visited` are reflected in the caller of `dfs` because of passing by reference.
/// Therefore, we don't need to return `pairs` and `visited`.
fn dfs(a: &Vec<Vec<usize>>, pairs: &mut Vec<(usize, usize)>, visited: &mut Vec<bool>) -> usize {
	let mut max_value = 0;
	if visited.iter().all(|&x| x) {
		for pair in pairs.iter() {
			max_value ^= a[pair.0][pair.1 - pair.0 - 1];
		}
		return max_value;
	}
	let mut first = 200;
	for i in 0..visited.len() {
		if !visited[i] {
			first = i;
			break;
		}
	}
	visited[first] = true;
	for second in first + 1..visited.len() {
		if !visited[second] {
			visited[second] = true;
			pairs.push((first, second));
			max_value = max(max_value, dfs(a, pairs, visited));
			pairs.pop();
			visited[second] = false;
		}
	}
	visited[first] = false;
	max_value
}

fn main() {
	input! {
		n: usize,
	}
	let mut a = Vec::new();
	for i in 0..2*n - 1 {
		let mut a_i = Vec::new();
		for _ in 0..2*n - i - 1 {
			input! {
				tmp: usize,
			}
			a_i.push(tmp);
		}
		a.push(a_i);
	}

	let mut pairs = Vec::new();
	let mut visited = vec![false; 2*n];
	println!("{}", dfs(&a, &mut pairs, &mut visited));
}
