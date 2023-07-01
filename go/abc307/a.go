package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var n int
	// https://pkg.go.dev/bufio#example-Scanner-Lines
	for scanner.Scan() {
		// https://pkg.go.dev/strconv#Atoi
		n, _ = strconv.Atoi(scanner.Text())
		break
	}
	var walks []int = make([]int, 7*n, 7*n)
	for scanner.Scan() {
		// https://pkg.go.dev/strings#example-Split
		str_walks := strings.Split(scanner.Text(), " ")
		for i, walk := range str_walks {
			walks[i], _ = strconv.Atoi(walk)
		}
		break
	}
	var results []int = make([]int, n, n)
	var tmp_result int
	for i, walk := range walks {
		tmp_result += walk
		if i%7 == 6 {
			results[i/7] = tmp_result
			tmp_result = 0
		}
	}
	for _, sum_walk := range results {
		fmt.Print(sum_walk)
		fmt.Print(" ")
	}
	fmt.Println()
}
