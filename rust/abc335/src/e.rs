#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::collections::BTreeSet;

#[fastout]
#[allow(unused_doc_comments)]
fn main() {
	input! {
		n: usize,
		m: usize,
		a: [usize; n],
		edges: [(usize, usize); m],
	}
	let mut graph = vec![vec![]; n];
	for edge in edges{
		graph[edge.0-1].push(edge.1-1);
		graph[edge.1-1].push(edge.0-1);
	}
	let mut visited = vec![false; n];
	let mut ans = 0;
	for i in 0..n{
		if visited[i]{
			continue;
		}
		let mut current_set = BTreeSet::new();
		let mut Q = vec![];
		Q.push((i, visited.clone(), current_set.clone()));
		visited[i] = true;
		while Q.len() > 0{
			let (current, mut visited, mut current_set) = Q.pop().unwrap();
			current_set.insert(a[current]);
			if current == n - 1 {
				if current_set.len() > 1{
					ans = std::cmp::max(ans, current_set.len());
				}
			}
			for next in graph[current].clone(){
				if visited[next]{
					continue;
				}
				if a[next] >= a[current]{
					visited[next] = true;
					Q.push((next, visited.clone(), current_set.clone()));
				}
			}
		}
	}
	println!("{}", ans);
}
