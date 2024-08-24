use proconio::{
    fastout, input,
};
use std::collections::{HashSet};

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        ab: [(usize, usize); n-1],
        mut targets: [usize; k],
    }

    let mut graph = vec![vec![]; n];
    for (a, b) in ab {
        graph[a-1].push(b-1);
        graph[b-1].push(a-1);
    }

    // minus targets
    for i in 0..k {
        targets[i] -= 1;
    }

    // Use a HashSet to ensure unique target nodes
    let targets_set: HashSet<usize> = targets.iter().cloned().collect();

    fn minimize_subtree(v: usize, p: i32, graph: &Vec<Vec<usize>>, targets_set: &HashSet<usize>) -> (usize, usize) {
        let mut subtree_size = 1;
        let mut target_count = if targets_set.contains(&v) { 1 } else { 0 };

        for &u in graph[v].iter() {
            if u as i32 == p {
                continue;
            }
            let (child_size, child_count) = minimize_subtree(u, v as i32, graph, targets_set);
            if child_count > 0 {
                subtree_size += child_size;
                target_count += child_count;
            }
        }

        if target_count == 0 {
            return (0, 0);
        }

        return (subtree_size, target_count);
    }

    let start_node = *targets_set.iter().next().unwrap();

    let (result, _) = minimize_subtree(start_node, -1, &graph, &targets_set);
    println!("{}", result);
}
