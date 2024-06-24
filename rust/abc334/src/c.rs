#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
        _n: usize,
        k: usize,
        a: [usize; k],
    };

    if k % 2 == 0 {
        let mut ans = 0;
        for i in 0..k {
            if i % 2 == 0 {
                ans += a[i].abs_diff(a[i + 1]);
            }
        }
        println!("{}", ans);
    } else {
        let mut left = vec![0; k];
        let mut left_current = 0;
        for i in 1..k {
            if i % 2 == 1 {
                left[i] = left_current;
            } else {
                left_current += a[i-1].abs_diff(a[i-2]);
                left[i] = left_current;
            }
        }
        let mut right = vec![0; k];
        let mut right_current = 0;
        for i in (0..k-1).rev() {
            if i % 2 == 0 {
                right[i] = right_current;
            } else {
                right_current += a[i].abs_diff(a[i+1]);
                right[i] = right_current;
            }
        }
        let mut ans = std::usize::MAX;
        for i in 0..k {
            if i % 2 == 0 {
                ans = ans.min(left[i] + right[i]);
            } else {
                ans = ans.min(left[i] + right[i] + a[i-1].abs_diff(a[i+1]));
            }
        }
        println!("{}", ans);
    }
}
