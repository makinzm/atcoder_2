package main

import (
	"fmt"
)

const MIN_VALUE = -50 * 50

// https://atcoder.jp/contests/abc031/tasks/abc031_c
func main() {
	var n int
	fmt.Scan(&n)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}
	/*
		I think we can calculate all the possible combination.
	*/
	// Takahashi = i
	var ans = MIN_VALUE
	for i := 0; i < n; i++ {
		var aoki_max = MIN_VALUE
		var takahashi_max = MIN_VALUE
		// Aoki = j
		// println(i, "   START!!!")
		for j := 0; j < n; j++ {
			if i == j {

			} else {
				var s = min(i, j)
				var g = max(i, j)
				subarray := arr[s : g+1]
				var tmp_aoki = 0
				var tmp_takahashi = 0
				for t := 0; t < len(subarray); t++ {
					// starting index is 0
					if t%2 != 0 {
						tmp_aoki += subarray[t]
					} else {
						tmp_takahashi += subarray[t]
					}
				}
				// println(j, i, tmp_aoki, tmp_takahashi, "|", aoki_max)
				// We can consider leftest side in max values.
				if tmp_aoki > aoki_max {
					takahashi_max = tmp_takahashi
					aoki_max = tmp_aoki
				}
			}
		}
		if takahashi_max >= ans {
			ans = max(takahashi_max, ans)
		}
	}
	println(ans)
}

func max(i int, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}

func min(i int, j int) int {
	if i < j {
		return i
	} else {
		return j
	}
}
