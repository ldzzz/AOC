package main

import (
	"regexp"
	"strconv"

	"github.com/jpillora/puzzler/harness/aoc"
)

func main() {
	aoc.Harness(run)
}

func run(part2 bool, input string) any {
	sum := 0
	mulRegxp := regexp.MustCompile(``)
	mulMatches := mulRegxp.FindAllStringSubmatch(input, -1)

	if part2 {
		donutRegxp := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|(?i)don't\(\)|(?i)do\(\)`)
		mulMatches = donutRegxp.FindAllStringSubmatch(input, -1)
	}

	var action = "do()"
	for i := 0; i < len(mulMatches); i++ {
		if part2 && mulMatches[i][0] == "don't()" || mulMatches[i][0] == "do()" {
			action = mulMatches[i][0]
			continue
		}
		if action == "do()" {
			num1, _ := strconv.Atoi(mulMatches[i][1])
			num2, _ := strconv.Atoi(mulMatches[i][2])
			sum += num1 * num2
		}
	}

	return sum
}
