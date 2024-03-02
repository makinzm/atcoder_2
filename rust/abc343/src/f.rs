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

#[fastout]
fn main() {
	input! {
		n: usize,
		q: usize,
		a: [usize; n],
		queries: [(usize, usize, usize); q],
	}
	let st_size = 1 << (n - 1).next_power_of_two();
	let mut data = vec![std::collections::HashMap::new(); 2 * st_size - 1];
	for i in 0..n {
		data[i + st_size - 1] = std::collections::HashMap::new();
		data[i + st_size - 1].insert(a[i], 1);
	}
	for i in (0..st_size - 1).rev() {
		data[i] = concat(&data[i * 2 + 1], &data[i * 2 + 2]);
	}
	for query in queries {
		let (status, p, x) = query;
		if status == 1 {
			change(p - 1, x, &mut data);
		} else {
			let ans = output(p - 1, x, 0, 0, st_size, &data);
			if ans.len() == 0 {
				println!("0");
			} else if ans.len() == 1 {
				println!("0");
			} else {
				let mut ans = ans.into_iter().collect::<Vec<(usize, usize)>>();
				ans.sort_by(|a, b| b.0.cmp(&a.0));
				println!("{}", ans[1].1);
			}
		}
	}
}
