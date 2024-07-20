#[allow(unused_imports)]
use proconio::{
    fastout, input,
};

#[fastout]
fn main() {
    input! {
        num: usize,
        kaibun_length: usize,
        base_string: String,
    }

    let mut count = 0;

    fn is_palindrome(s: &str) -> bool {
        s == s.chars().rev().collect::<String>()
    }

    fn is_k_palindrome(s: &str, k: usize) -> bool {
        let n = s.len();
        for i in 0..n - k + 1 {
            if is_palindrome(&s[i..i + k]) {
                return true;
            }
        }
        false
    }
    
    fn permutations(s: &str) -> Vec<String> {
        let mut perms = Vec::new();
        let chars: Vec<char> = s.chars().collect();
        let mut perm = String::new();
        let mut used = vec![false; s.len()];
        fn dfs(chars: &Vec<char>, perm: &mut String, perms: &mut Vec<String>, used: &mut Vec<bool>) {
            if perm.len() == chars.len() {
                perms.push(perm.clone());
                return;
            }
            for i in 0..chars.len() {
                if used[i] {
                    continue;
                }
                used[i] = true;
                perm.push(chars[i]);
                dfs(chars, perm, perms, used);
                perm.pop();
                used[i] = false;
            }
        }
        dfs(&chars, &mut perm, &mut perms, &mut used);
        perms
    }

    let mut visited = std::collections::HashSet::new();
    for perm in permutations(&base_string) {
        let new_string = perm;
        if visited.contains(&new_string) {
            continue;
        }
        visited.insert(new_string.clone());
        if !is_k_palindrome(&new_string, kaibun_length) {
            count += 1;
        }
    }

    println!("{}", count);

}

