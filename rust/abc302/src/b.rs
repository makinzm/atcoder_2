#[allow(unused_imports)]
use proconio::{
    fastout, input,
	marker::Chars
};

#[fastout]
fn main() {
	input! {
        h: i32,
        w: i32,
        m: [Chars; h],
    };
	// only search starting from `s`
	for x in 0..h{
		for y in 0..w{
			if m[x as usize][y as usize] == 's'{
				for dx in -1..=1{
					for dy in -1..=1{
						if dx < 0{
							if x < (4*(dx as i32).abs()){
								continue;
							}
						}
						if dy < 0{
							if y < (4*(dy as i32).abs()){
								continue;
							}
						}
						let xplus4 = (x as i32 + 4*dx) as usize;
						let yplus4 = (y as i32 + 4*dy) as usize;
						if xplus4 < w as usize && yplus4 < h as usize {
							// println!("{},{} -> {},{}",x,y,xplus4,yplus4);
							if m[(x as i32+1*dx) as usize][(y as i32+1*dy) as usize] == 'n' 
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
