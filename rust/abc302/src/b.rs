#[allow(unused_imports)]
use proconio::{
    fastout, input,
	marker::Chars
};

fn min<T: PartialOrd>(a: T, b: T) -> T {
    if a < b {
        a
    } else {
        b
    }
}

#[fastout]
fn main() {
	input! {
        h: i32,
        w: i32,
        m: [Chars; h],
    };
	// only search starting from `s`
	let mut flag = false;
	let minus_one = -1;
	for x in 0..h{
		for y in 0..w{
			if m[x as usize][y as usize] == 's'{
				for dx in -1..=1{
					for dy in -1..=1{
						let xplus = (x as i32 + dx) as usize;
						let yplus = (y as i32 + dy) as usize;
						let xplus4 = (x as i32 + 4*dx) as usize;
						let yplus4 = (y as i32 + 4*dy) as usize;
						if xplus >=0 && xplus4 < w as usize && yplus >= 0 && yplus4 < h as usize {
							if m[xplus][yplus] == 'n' 
							&& m[(x as i32+2*dx) as usize][(y as i32+2*dy) as usize] == 'u' 
							&& m[(x as i32+3*dx) as usize][(y as i32+3*dy) as usize] == 'k' 
							&& m[(x as i32+4*dx) as usize][(y as i32+4*dy) as usize] == 'e'
							{
								for i in 0..=4{
									println!("{} {}",(x+i*dx+1) as usize,(y+i*dy+1) as usize);
								}
								return;
							}
						}
					}
				}
			}
		}
	}
}
