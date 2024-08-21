#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
        n: usize,
        mut k: usize,
        x: [usize; n],
        a: [usize; n],
	}
    // p[i][j]: When 2^i-th move of j-th node
    let mut p = vec![vec![0; n]; 60];
    for i in 0..n {
        p[0][i] = x[i] - 1;
    }
    for i in 1..60 {
        for j in 0..n {
            p[i][j] = p[i - 1][p[i - 1][j]];
        }
    }
    // q[i]: current position of i-th node
    let mut q = vec![0; n];
    for i in 0..n {
        q[i] = i;
    }
    for i in 0..60 {
        if (k%2) == 1 {
            for j in 0..n {
                q[j] = p[i][q[j]];
            }
        }
        k /= 2;
    }

    for i in 0..n {
        print!("{} ", a[q[i]]);
    }
    println!();
}
