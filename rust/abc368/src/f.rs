use proconio::{fastout, input};

const MAX_N: usize = 100_000;

fn eratosthenes(n: usize) -> (Vec<bool>, Vec<usize>) {
    let mut is_prime = vec![true; n + 1];
    is_prime[0] = false;
    is_prime[1] = false;
    let mut primes = Vec::new();

    for i in 2..=(n as f64).sqrt() as usize {
        if is_prime[i] {
            primes.push(i);
            for j in (i * i..=n).step_by(i) {
                is_prime[j] = false;
            }
        }
    }
    (is_prime, primes)
}

fn grundy_number(mut x: usize, primes: &[usize]) -> usize {
    let mut res = 0;
    for &p in primes {
        if p * p > x {
            break;
        }
        while x % p == 0 {
            res += 1;
            x /= p;
        }
    }
    if x > 1 {
        res += 1;
    }
    res
}

#[fastout]
fn main() {
    let debug = false;
    input! {
        n: usize,
        a: [usize; n],
    }

    let (_, primes) = eratosthenes(MAX_N);

    let mut grundy = 0;
    for ai in a {
        let ai_grundy_number = grundy_number(ai, &primes);
        if debug {
            println!("{}: {}", ai, ai_grundy_number);
        }
        grundy ^= ai_grundy_number;
    }

    println!("{}", if grundy == 0 { "Bruno" } else { "Anna" });
}
