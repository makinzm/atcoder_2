#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
	input! {
        n: usize,
        l: usize,
        r: usize,
    }
    for i in 1..=l-1 {
        a.push(i);
    }
    for i in (l..=r).rev() {
        a.push(i);
    }
    for i in r+1..=n {
        a.push(i);
    }
    println!("{}", a.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" "));
}
