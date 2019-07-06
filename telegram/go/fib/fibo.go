package main

import (
	"fmt"
	"os"
	"strconv"
)

func Fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return Fibonacci(n-1) + Fibonacci(n-2)
}
func main() {
	i, _ := strconv.Atoi(os.Args[1])
	fmt.Println(Fibonacci(i))
}
