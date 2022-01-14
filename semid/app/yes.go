package main

import (
	"os"
)

func main() {
	args := slice(os.Args, 0)
	if len(args) < 1 {

	}
}

func slice(what []string, where int) []string {
	var newArray []string
	for a, b := range what {
		if a == where {
		} else {
			newArray = append(newArray, b)
		}
	}
	return newArray
}

func join(what []string, who string) string {
	returnstr := ""
	for b, a := range what {
		if b == len(what)-1 {
			returnstr += a
		} else {
			returnstr += a + who
		}
	}
	return returnstr

}
