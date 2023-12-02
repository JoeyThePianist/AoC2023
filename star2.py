def main():
    #Dictionary defining spelled out numbers and their numeric counterparts
    numberwords = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    #Reading and breaking apart the provided puzzle into individual lines
    puzzle = open("./assets/star1puzzle.txt", "r")
    puzzle_content = puzzle.read()
    lines = puzzle_content.splitlines()
    total = 0
    
if __name__ == "__main__":
    main()