word_map = {
    'o' : [("one", "1")],
    't' : [("two", "2"), ("three", "3")],
    'f' : [("four", "4"), ("five", "5")],
    's' : [("six", "6"), ("seven", "7")],
    'e' : [("eight", "8")],
    'n' : [("nine", "9")]
}
total = 0

test_puzzle = open("./assets/star2test.txt", "r")
test_content = test_puzzle.read()

puzzle = open("./assets/star1puzzle.txt", "r")
puzzle_content = puzzle.read()

def numSifter(input):
    lines = input.splitlines()
    total = 0
    for line in lines:
        result = parseLine(line)
        total += result
    return total


def parseLine(line):
    numbers_in_line = []
    for (index, character) in enumerate(line):
        if character.isdigit():
            numbers_in_line.append(character)
            continue
        if character in word_map:
            for num_list in word_map[character]:
                num_str = num_list[0]
                line_tester = line[index:len(num_str) + index]
                if line_tester == num_str:
                    numbers_in_line.append(num_list[1])
    return int(numbers_in_line[0] + numbers_in_line[-1])

#Test Results
print(numSifter(test_content))

#Puzzle Results
print(numSifter(puzzle_content))