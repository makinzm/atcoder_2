package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	var count int
	for n > 0 {
		if n%2 == 0 {
			count++
			n /= 2
		} else {
			break
		}
	}
	fmt.Println(count)
}
