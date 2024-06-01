#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::collections::HashMap;
use std::cmp::min;

#[fastout]
fn main() {
	input! {
        n: usize,
        k: usize,
        p: [usize; n],
    }

    let mut dict_p = HashMap::new();
    for i in 0..n {
        dict_p.insert(p[i], i+1);
    }

    let mut sorted_p = vec![0; n];
    for i in 1..=n {
        sorted_p[i-1] = dict_p[&i];
    }

    let mut ans = n;
    for i in 0..=n-k {
        let cloned_partially_sorted_p = Vec::from_iter(&mut sorted_p[i..i+k].iter().cloned());
        let i_k = cloned_partially_sorted_p.iter().max().unwrap();
        let i_1 = cloned_partially_sorted_p.iter().min().unwrap();
        ans = min(ans, i_k - i_1);
    }

    println!("{}", ans);
}
