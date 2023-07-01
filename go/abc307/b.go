package main

import (
	"bufio"
	"fmt"
	"os"
)

func reverseStr(str string) string {
	bytes := []byte(str)
	for i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1 {
		bytes[i], bytes[j] = bytes[j], bytes[i]
	}
	var reversedStr string = string(bytes)
	return reversedStr
}

var scanner = bufio.NewScanner(os.Stdin)

func main() {
	var n int
	fmt.Scan(&n)

	var s []string = make([]string, n)
	var _count int
	for scanner.Scan() {
		if _count > n-1 {
			break
		} else {
			s[_count] = scanner.Text()
			_count++
			if _count == n {
				break
			}
		}
	}
	// fmt.Println(s)

	var flag bool = false
Result:
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			// fmt.Println(i, j)
			var strIj string = s[i] + s[j]
			var reverseIj string = reverseStr(strIj)

			var strJi string = s[j] + s[i]
			var reverseJi string = reverseStr(strJi)

			if (strIj == reverseIj) || (strJi == reverseJi) {
				// fmt.Println("ANS")
				// fmt.Println(i, j)
				// fmt.Println(strJi, strIj)
				flag = true
				break Result
			}
		}
	}
	var result string = map[bool]string{true: "Yes", false: "No"}[flag]
	fmt.Println(result)
}
