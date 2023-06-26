#[allow(unused_imports)]
use proconio::{
    fastout, input,
	marker::Chars
};
use std::collections::{
	HashSet, VecDeque
};

/*
前提知識 Premise
	次数(degree, velocity): 頂点の手の数: https://en.wikipedia.org/wiki/Degree_(graph_theory)

方針 Policy
	端からひとつ目は星で, そこから3ついった箇所は必ず星: これの数とこの隣接数をしればよい

	# 他には 3以上のものを数えた後に, その星の次数をnから引いていき, 最後に 3 だけひいいていけば良い.
 */

// 所有権の関係で関数に & をつける
fn process_buffer(visited: &mut HashSet<usize>, buf1: &mut VecDeque<usize>, buf2: &mut VecDeque<usize>, map: &std::vec::Vec<HashSet<usize>>) {
    if let Some(value) = buf1.remove(0) {
        let one: usize = value;
		if !true{
			println!("IN 1 or 2");
			println!("{}", one);
		}
        visited.insert(one);
        for &next_place in &map[one] {
            if !visited.contains(&next_place) {
                buf2.push_back(next_place);
            }
        }
    }
}


#[fastout]
fn main() {
	input! {
        n: usize,
        uv: [[usize; 2]; n-1],
    };
	let mut map = vec![HashSet::new(); n];
	for one_uv in &uv{
		let _u = one_uv[0] - 1;
		let _v = one_uv[1] - 1;
		map[_u].insert(_v);
		map[_v].insert(_u);
	}

	if !true {
		let mut _count = 0;
		for one_map in &map{
			print!("{} : ", _count);
			for one_place in one_map.iter(){
				print!("{} ,", one_place);
			}
			_count +=1;
			println!();
		}
	}
	
	let mut start_point: usize = 0;
	let mut _count = 0;
	for one_map in &map{
		if one_map.len() == 1 {
			start_point = _count;
			break;
		}
		else{
			_count += 1;
		}
	}

	// bfs
	let mut buf0:VecDeque<usize> = VecDeque::new();
	let mut buf1:VecDeque<usize> = VecDeque::new();
	let mut buf2:VecDeque<usize> = VecDeque::new();
	let mut visited:HashSet<usize> = HashSet::new();
	let mut ans_set:HashSet<usize> = HashSet::new();

	visited.insert(start_point);
	if let Some(&val) = map[start_point].iter().next() {
		buf0.push_back(val);
	}

	while visited.len() < n{
		// 1 -> 2
		// get: Option<&T>
		// remove: Option<T>
		process_buffer(&mut visited, &mut buf1, &mut buf2, &map);
		process_buffer(&mut visited, &mut buf2, &mut buf0, &map);

		if let Some(value) = buf0.remove(0) {
			let one: usize = value;
			if !true{
				println!("IN 0");
				println!("{}",one);
			}
			visited.insert(one);
			ans_set.insert(one);
			for &next_place in &map[one] {
				if !visited.contains(&next_place) {
					buf1.push_back(next_place);
				}
			}
		}
	}
	
	let mut output = String::new();
	let mut sorted_ans: Vec<usize> = ans_set.iter().map(|&star_place| map.get(star_place).map(HashSet::len).unwrap_or(0)).collect();
	sorted_ans.sort();
	for (i, ans) in sorted_ans.iter().enumerate() {
		output.push_str(&ans.to_string());
		if i < sorted_ans.len() - 1 {
			output.push(' ');
		}
	}
	println!("{}", output);
}
