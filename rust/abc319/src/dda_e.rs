// ABC319

#[allow(unused_imports)]
use proconio::{
    fastout, input,
};
use std::cmp::{Ord, Eq, Ordering};
use std::collections::{BinaryHeap,HashMap};


#[derive(Debug)]
struct VertualState{
	/// We have to think vertual condition
	/// Strength
	/// EnemyQueue
	strength: usize,
	enemy_queue: BinaryHeap<Enemy>,
}

#[derive(Debug)]
struct Enemy {
	/// You need power which is bigger than condition.
	/// You can get benefit.
	/// next position
	condition: usize,
	benefit: usize,	
	children: Vec<usize>,
	parent: usize,
	my_index: usize,
}
impl PartialOrd for Enemy {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Enemy {
    fn eq(&self, other: &Self) -> bool {
        self.condition == other.condition
    }
}

impl Eq for Enemy {}

impl Ord for Enemy {
    fn cmp(&self, other: &Self) -> Ordering {
        self.condition.cmp(&other.condition)
    }
}

#[derive(Debug)]
struct Medicine{
	/// Your power become 
	/// next position
	effect: usize,
	children: Vec<usize>,
	parent: usize,
	my_index: usize,
	medicine_index: usize,
}
#[allow(dead_code)]
#[derive(Debug)]
struct InitialPoint{
	/// Initial Point is special
	/// next position
	my_index: usize,
	children: Vec<usize>,
}
#[derive(Debug)]
enum Vertex{
	/// For vertex, Enemy or Medicine
	Enemy(Enemy),
	Medicine(Medicine),
	InitialPoint(InitialPoint),
}
impl Vertex{
	fn get_children(&mut self) -> &mut Vec<usize>{
		match self {
            Vertex::Enemy(e) => &mut e.children,
            Vertex::Medicine(m) => &mut m.children,
            Vertex::InitialPoint(ip) => &mut ip.children,
        }
	}
	fn check_children(&self) -> &Vec<usize>{
		match self {
            Vertex::Enemy(e) => &e.children,
            Vertex::Medicine(m) => &m.children,
            Vertex::InitialPoint(ip) => &ip.children,
        }
	}
}

fn insert_inputs_to_vertices_and_send_num_medicines_and_biggest_condition(vs: &mut Vec<Vertex>, inps: Vec<Vec<usize>>) -> (usize,usize){
	// insert inputs to vertices
	let mut count = 1;
	let mut medicine_index = 0;
	let mut biggest_condition = 0;
	for inp in inps{
		match inp[1] {
			1 => {
				// why I can remove `mut` though children differs later.
				let enemy = Enemy{
					condition: inp[2],
					benefit: inp[3],	
					children: Vec::new(),
					parent: inp[0],
					my_index: count,
				};
				if biggest_condition < enemy.condition {
					biggest_condition = enemy.condition;
				}
				vs.push(Vertex::Enemy(enemy));
			},
			2 => {
				let medicine = Medicine{
					effect: inp[3],
					children: Vec::new(),
					parent: inp[0],
					my_index: count,
					medicine_index
				};
				vs.push(Vertex::Medicine(medicine));
				medicine_index += 1;
			},
			_ => panic!("This is a terrible problem!")
		}
		count += 1;
	}
	(medicine_index, biggest_condition)
}

fn update_children(vs: &mut Vec<Vertex>){

	// rustc --explain E0499
	// for vertex in vs.iter_mut(){
	// 	if let Vertex::Enemy(enemy) = vertex{
	// 		vs[enemy.parent].get_children().push(enemy.my_index);
	// 	}
	// }

	// rustc --explain E0499
	// let len = vs.len();
    // for i in 0..len {
    //     if let Vertex::Enemy(enemy) = &mut vs[i] {
    //         vs[enemy.parent].get_children().push(enemy.my_index);
    //     }
    // }

	let len = vs.len();
	for i in 0 ..len{
		let parent;
		let my_index;
		let mut get_parent_flag = false;
		if let Vertex::Enemy(enemy) = &vs[i] {
			parent = enemy.parent - 1;
			my_index = enemy.my_index;
			get_parent_flag = true
		} else if let Vertex::Medicine(medicine) = &vs[i] {
			parent = medicine.parent - 1;
			my_index = medicine.my_index;
			get_parent_flag = true
		} else {
			parent = 0;
			my_index = 0;
		}
		if get_parent_flag {
			vs[parent].get_children().push(my_index);
		}
	}
}

fn update_dp(
	dp: &mut HashMap<i32, usize>, 
	pq: &mut BinaryHeap<&Enemy>,
	value: &i32, 
	n: &usize,
	vertices: &Vec<Vertex>
){
	let mut max_value = 0;
	for j in 0..*n {
		let previous_state = value ^ (1 << j);
		// if だから 所有権を奪わない.
		if previous_state < *value {
			let mut current_state = dp[&previous_state];
			// 検索性...
			// TODO: どのように薬が取られるか,
			// Indexをどのように振るべきか考えながら設計する.
			current_state *= vertices[];
			while(pq.len() > 0){
				let enemy = pq.pop();

			}

			let bit_str = format!("{:0width$b}", value, width = n);
			let modified_str = format!("{:0width$b}", previous_state, width = n);
			println!("Value: {}, Modified Binary: {}", bit_str, modified_str);
		}
	}
}

// #[fastout]
#[allow(unused_doc_comments)]
fn main() {
	input!{
		n: usize,
		inps: [[usize;4];n-1],
	}; 
	println!("{:?}",inps);
	let mut vertices = Vec::<Vertex>::new();
	vertices.push(Vertex::InitialPoint(InitialPoint { children: Vec::new(), my_index: 0 }));
	let (num_medicine, biggest_condition) = insert_inputs_to_vertices_and_send_num_medicines_and_biggest_condition(&mut vertices, inps);
	update_children(&mut vertices);

	/// Policy
	/// dp[bit(num_medicine)] = MaxStrength
	
	let ans_bit: i32 = 1 << num_medicine - 1;

	let mut dp: HashMap<i32, usize> = HashMap::new();
	let mut pq = BinaryHeap::<&Enemy>::new();

	let first_point = &vertices[0];
	if let Vertex::InitialPoint(_) = first_point{
		for vertex_index in first_point.check_children(){
			// I want to remove the implementation of Copy.
			// Using slice not vec.
			if let Vertex::Enemy(enemy) = &vertices[*vertex_index] {
				pq.push(enemy);
			}
		}
		println!("FP {:?}", first_point);
	} else {
		panic!("This is a teriible problem");
	}

	let mut bit_dp_orders = vec![];
    for i in 0..=ans_bit {
        let bit_count = (i as i32).count_ones();
        bit_dp_orders.push((i, bit_count));
    }
	bit_dp_orders.sort_by_key(|&(_, bit_count)| bit_count);

	for (value, _) in bit_dp_orders {
		// 所有権を奪わない.
		println!("PQ: {:?}, {}", pq, value);
		update_dp(&mut dp,&mut pq, &value, &num_medicine, &vertices);
    }

	println!("Num of Medicines: {}",num_medicine);
	println!("{:?}",vertices);

	if let Some(dp_value) = dp.get(&ans_bit){
		if biggest_condition > *dp_value {
			println!("No");
		}else {
			println!("Yes")
		}
	} else {
		println!("?????")
	}
	println!("DP: {:?}",dp);
}
