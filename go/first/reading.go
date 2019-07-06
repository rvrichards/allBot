package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	b, err := ioutil.ReadFile("file.txt")
	if err != nil {
		fmt.Print("Error detected:", err)
	}
	str := string(b)
	fmt.Println(str)
}
