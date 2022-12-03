input = open("input.txt", "r")

def gameInput(input):
    score = 0
    input = input.readlines()
    for line in input:
        for element in line.rstrip():
            #print(element)
            if element == "A" or element == "B" or element == "C":
                opponent = element
                #print(opponent)
            elif element == "Y" or element == "X" or element == "Z":
                you = element
                #print(you)
        score += battle(opponent, you)
    print(score)
        #print(opponent)
        #print(you)
        #battle(opponent, you)

def battle(opponent, you):
    match opponent:
        case "A":
            match you:
                case "X":
                    return 3
                case "Y":
                    return 4
                case "Z":
                    return 8
        case "B":
            match you:
                case "X":
                    return 1
                case "Y":
                    return 5
                case "Z":
                    return 9
        case "C":
            match you:
                case "X":
                    return 2
                case "Y":
                    return 6
                case "Z":
                    return 7
    #print(opponent)
    #print(you)

gameInput(input)