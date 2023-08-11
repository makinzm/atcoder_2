#[allow(unused_imports)]
use proconio::{
    fastout, input
};
// Here is b's problem
// https://atcoder.jp/contests/arc042/tasks/arc042_b

/// Calculate line coefficients given the two points.
fn calculate_line_coefficients(point1: &(i8, i8), point2: &(i8, i8)) -> (i64, i64, i64) {
	let (x, y) = *point1;
    let (z, w) = *point2;

    let a: i64 = (w as i64) - (y as i64);
    let b: i64= (x as i64) - (z as i64);
    let c: i64 = (z as i64) * (y as i64) - (w as i64) * (x as i64);

	assert!(a*(x as i64)+b*(y as i64)+c == 0);
	assert!(a*(z as i64)+b*(w as i64)+c == 0);
    (a, b, c)
}

/// Calculate the distance between a point and a line.
fn calculate_distance(point: &(i8, i8), line: &(i64, i64, i64)) -> f64 {
	let (x,y) = *point;
    let (a,b,c) = *line;
	
	let x_64: i64 = x as i64;
	let y_64: i64 = y as i64;

	// Using cast
	let denominator: f64 = ((a as f64).powf(2.0) + (b as f64).powf(2.0)).sqrt();
	let numerator: f64 = ((a*x_64 + b*y_64 + c) as f64).abs();

	numerator/denominator
}


#[fastout]
fn main() {
	input!{
		x: i8,
        y: i8,
        n: usize,
        xy: [(i8, i8); n],
	}
	// XYs are given orderd by rotatting anticlockwise
	// So we just calculate distances between point and line
	let mut ans: f64 = std::f64::MAX;
	for i in 0..n{
		let abc: (i64, i64, i64);
		if i != n-1 {
			abc = calculate_line_coefficients(&xy[i], &xy[i+1])
		} else {
			abc = calculate_line_coefficients(&xy[i], &xy[0])
		}
		let tmp = calculate_distance(&(x,y), &abc);
		ans = ans.min(tmp);
	}
	println!("{}", ans);
}
