#[allow(unused_imports)]
use proconio::{
    fastout, input,
	marker::Chars,
};
use std::collections::HashMap;

#[fastout]
fn main() {
	input! {
		h: usize,
		w: usize,
		n: usize,
		t: Chars,
		s: [Chars; h],
	}
	let mut ans = 0;
	let mut directory_map: HashMap<char, (isize, isize)> = HashMap::new();
	let land_mark: char = '.';
	let sea_mark: char = '#';
	directory_map.insert('L', (-1, 0));
	directory_map.insert('R', (1, 0));
	directory_map.insert('U', (0, -1));
	directory_map.insert('D', (0, 1));
	let mut directories: Vec<(isize,isize)> = vec![];
	for i in 0..n {
		directories.push(directory_map.get(&t[i]).unwrap().clone());
	}
	for i in 0..h {
		for j in 0..w {
			let mut next_i: isize = i as isize;
			let mut next_j: isize = j as isize;
			let mut ok = true;
			if s[i][j] == land_mark {
				for n_step in 0..n {
					next_i += directories[n_step].1;
					next_j += directories[n_step].0;
					if next_i >= h as isize || next_j >= w as isize || next_i < 0 || next_j < 0 {
						ok = false;
						break;
					}
					if s[next_i as usize][next_j as usize] == sea_mark {
						ok = false;
						break;
					}
				}
				if ok {
					ans += 1;
				}
			}
		}
	}
	println!("{}", ans);
}
