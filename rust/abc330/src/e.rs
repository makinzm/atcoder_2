// ABC330

#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::collections::BTreeSet;
use std::iter::FromIterator;

#[fastout]
#[allow(unused_doc_comments)]
fn main() {
	input!{
		n: usize,q: usize,
		mut a: [usize;n],
		ixs: [(usize,usize);q],
	};
	// to manage the number of each value in a
	let mut cnt = vec![0; n+1];
	// to get the min value which is in set which is not in a and less than n + 1
	let mut set_not_in_a = BTreeSet::from_iter(0..n+1);
	for i in 0..n {
		if a[i] <= n {
			cnt[a[i]] += 1;
			set_not_in_a.remove(&a[i]);
		}
	}
	for (mut i,x) in ixs {
		i -= 1;
		if a[i] <= n {
			cnt[a[i]] -= 1;
			if cnt[a[i]] == 0 {
				set_not_in_a.insert(a[i]);
			}
		}
		if x < n {
			cnt[x] += 1;
			if cnt[x] == 1 {
				set_not_in_a.remove(&x);
			}
		}
		a[i] = x;
		println!("{}", set_not_in_a.iter().next().unwrap());
	}
}
