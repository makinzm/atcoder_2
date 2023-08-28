package main

import (
	"fmt"
)

func main() {
	var n, h, x int
	fmt.Scanf("%d %d %d", &n, &h, &x)
	p := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &p[i])
	}
	var min_health int = x - h
	// 値以下の最も大きい値
	var min_i int = -1
	// 値以上の最も小さな値
	var max_i int = n - 1
	for max_i-min_i > 1 {
		var mid_i int = (min_i + max_i) / 2
		// fmt.Print(p[mid_i], min_health)
		if p[mid_i] >= min_health {
			// fmt.Print("A: ")
			max_i = mid_i
		} else {
			// fmt.Print("B: ")
			min_i = mid_i
		}
		// fmt.Print(min_i, max_i, mid_i)
		// fmt.Print("\n")
	}
	fmt.Println(max_i + 1)
}
