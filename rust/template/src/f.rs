#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

fn concat(a: &std::collections::HashMap<usize, usize>, b: &std::collections::HashMap<usize, usize>) -> std::collections::HashMap<usize, usize> {
	let mut c = std::collections::HashMap::new();
	for (k, v) in a.iter() {
		c.insert(*k, *v);
	}
	for (k, v) in b.iter() {
		if c.contains_key(k) {
			*c.get_mut(k).unwrap() += *v;
		} else {
			c.insert(*k, *v);
		}
	}
	if c.len() > 2 {
		let mut c = c.into_iter().collect::<Vec<(usize, usize)>>();
		c.sort_by(|a, b| b.0.cmp(&a.0));
		c.truncate(2);
		return c.into_iter().collect();
	}
	c
}

fn change(p: usize, x: usize, data: &mut Vec<std::collections::HashMap<usize, usize>>) {
	let st_size = (data.len() + 1) / 2;
	let mut p = p + st_size - 1;
	data[p] = std::collections::HashMap::new();
	data[p].insert(x, 1);
	while p > 0 {
		p = (p - 1) / 2;
		data[p] = concat(&data[p * 2 + 1], &data[p * 2 + 2]);
	}
}

fn output(p: usize, x: usize, k: usize, l: usize, r: usize, data: &Vec<std::collections::HashMap<usize, usize>>) -> std::collections::HashMap<usize, usize> {
	if r <= p || x <= l {
		return std::collections::HashMap::new();
	}
	if p <= l && r <= x {
		return data[k].clone();
	}
	let vl = output(p, x, k * 2 + 1, l, (l + r) / 2, data);
	let vr = output(p, x, k * 2 + 2, (l + r) / 2, r, data);
	concat(&vl, &vr)
}

fn solve(n: usize, _q:usize, a: Vec<usize>, queries: Vec<(usize, usize, usize)>) -> Vec<usize> {
	let st_size = 1 << (n - 1).next_power_of_two();
	let mut data = vec![std::collections::HashMap::new(); 2 * st_size - 1];
	for i in 0..n {
		data[i + st_size - 1] = std::collections::HashMap::new();
		data[i + st_size - 1].insert(a[i], 1);
	}
	for i in (0..st_size - 1).rev() {
		data[i] = concat(&data[i * 2 + 1], &data[i * 2 + 2]);
	}
	let mut answers = Vec::new();
	for query in queries {
		let (status, p, x) = query;
		if status == 1 {
			change(p - 1, x, &mut data);
		} else {
			let ans = output(p - 1, x, 0, 0, st_size, &data);
			if ans.len() == 0 {
				panic!("No such element");
			} else if ans.len() == 1 {
				answers.push(0);
			} else {
				let mut ans = ans.into_iter().collect::<Vec<(usize, usize)>>();
				ans.sort_by(|a, b| b.0.cmp(&a.0));
				answers.push(ans[1].1);
			}
		}
	}
	answers
}

#[fastout]
fn main() {
	input! {
		n: usize,
		q: usize,
		a: [usize; n],
		queries: [(usize, usize, usize); q],
	}
	let ans: Vec<usize> = solve(n, q, a, queries);
	for a in ans {
		println!("{}", a);
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn test_sample_1() {
		let n = 5;
		let q = 4;
		let a = vec![3,3,1,4,5];
		let queries = vec![(2,1,3), (2,5,5), (1,3,3), (2,2,4)];
		let expected = vec![1, 0, 2];

		let answers = solve(n, q, a, queries);
		assert_eq!(answers, expected);
	}

	#[test]
	fn test_sample_2() {
		let n = 1;
		let q = 1;
		let a = vec![1000000000];
		let queries = vec![(2,1,1)];
		let expected = vec![0];

		let answers = solve(n, q, a, queries);
		assert_eq!(answers, expected);
	}

	#[test]
	fn test_sample_3() {
		let n = 8;
		let q = 9;
		let a = vec![2,4,4,3,9,1,1,2];
		let queries = vec![
			(1,5,4),
			(2,7,7),
			(2,2,6),
			(1,4,4),
			(2,2,5),
			(2,2,7),
			(1,1,1),
			(1,8,1),
			(2,1,8)
		];
		let expected = vec![0,1,0,2,4];

		let answers = solve(n, q, a, queries);
		assert_eq!(answers, expected);
	}

	#[test]
	fn original_sample_2() {
		/* N is equals to 2 */
		let n = 2;
		let q = 3;
		let a = vec![1, 2];
		let queries = vec![(2, 1, 2), (1, 1, 2), (2, 1, 2)];
		let expected = vec![1, 0];

		let answers = solve(n, q, a, queries);
		assert_eq!(answers, expected);
	}
}
