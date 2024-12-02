package main

import (
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
	var res = 0
	// solve part 1 here
	reports := strings.Split(input, "\n")
	for i := 0; i < len(reports); i++ {
		report := strings.Split(reports[i], " ")
		errIdx := followsRules(report)
		if errIdx == -1 {
			res += 1
		}
		if part2 && errIdx != -1 {
			if followsRules(remove(report, errIdx)) == -1 {
				res += 1
			} else if followsRules(remove(report, errIdx+1)) == -1 {
				res += 1
			} else if errIdx != 0 && followsRules(remove(report, errIdx-1)) == -1 {
				res += 1
			}
		}
	}
	return res
}

func followsRules(report []string) int {
	var isIncreasing bool
	for i := 0; i < len(report)-1; i++ {
		num1, _ := strconv.Atoi(report[i])
		num2, _ := strconv.Atoi(report[i+1])
		if i == 0 {
			isIncreasing = num2 > num1
		}
		if num1 == num2 || Abs(num1-num2) > 3 || ((isIncreasing && num2 < num1) || (!isIncreasing && num1 < num2)) {
			return i
		}
	}
	return -1
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func remove(s []string, index int) []string {
    ret := make([]string, 0)
    ret = append(ret, s[:index]...)
    return append(ret, s[index+1:]...)
}
