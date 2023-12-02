def main():
    puzzle = open("./assets/star1puzzle.txt", "r")
    puzzle_content = puzzle.read()
    lines = puzzle_content.splitlines()
    total = 0
    for line in lines:
        result = parseLine(line)
        total = total + result
    print(total)
    
def parseLine(line):
    first_number = None
    last_number = None
    for character in line:
        if character.isdigit():
            first_number = character
            break
    for index in range(len(line) -1, -1, -1):
        character = line[index]
        if character.isdigit():
            last_number = character
            break
    return int(first_number + last_number)

if __name__ == "__main__":
    main()