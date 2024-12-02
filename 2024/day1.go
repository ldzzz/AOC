package main

import (
	"sort"
	"strconv"
	"strings"

	"github.com/jpillora/puzzler/harness/aoc"
)

func main() {
	aoc.Harness(run)
}

// on code change, run will be executed 4 times:
// 1. with: false (part1), and example input
// 2. with: true (part2), and example input
// 3. with: false (part1), and user input
// 4. with: true (part2), and user input
// the return value of each run is printed to stdout
func run(part2 bool, input string) any {
	// when you're ready to do part 2, remove this "not implemented" block
	// solve part 1 here
	res := 0
	splinput := strings.Fields(input)

	var l1 []int
	var l2 []int
	for i := 0; i < len(splinput); i++ {
		if i%2 == 0 {
			l1 = append(l1, string2num(splinput[i]))
		} else {
			l2 = append(l2, string2num(splinput[i]))
		}
	}
	
	if part2 {
		for i := 0; i < len(l1); i++ {
			res += l1[i] * count(l2, func(x int) bool {return x== l1[i]})
		}
	}else {
		sort.Ints(l1)
		sort.Ints(l2)
		for i := 0; i < len(l1); i++ {
			res += Abs(l1[i] - l2[i])
		}
	}
	return res
}

func string2num(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return i
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func count[T any](slice []T, f func(T) bool) int {
    count := 0
    for _, s := range slice {
        if f(s) {
            count++
        }
    }
    return count
}
